from aws_cdk import (
    RemovalPolicy,
    Stack,
)
from aws_cdk import (
    aws_codepipeline as codepipeline,
)
from aws_cdk import (
    aws_codepipeline_actions as cpactions,
)
from aws_cdk import (
    aws_iam as iam,
)
from aws_cdk import (
    aws_s3 as s3,
)
from aws_cdk import (
    aws_ssm as ssm,
    aws_codebuild as codebuild,
    RemovalPolicy,
)
from constructs import Construct

from stacks.staging_stack import STAGING_APP_NAME, STAGING_ENV_NAME


class StagingPipelineStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        artifact_bucket = s3.Bucket(
            self,
            "StagingArtifactBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        # Grant Permission via IAM Role to Pipeline for Elastic Beanstalk Deployment

        pipeline_role = iam.Role(
            self,
            "EBDeployRole",
            assumed_by=iam.ServicePrincipal("codepipeline.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy"
                ),
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "CloudWatchLogsFullAccess"
                ),
            ],
        )
        # Pipeline
        pipeline = codepipeline.Pipeline(
            self,
            "StagingPipeline",
            role=pipeline_role,
            artifact_bucket=artifact_bucket,
            execution_mode=codepipeline.ExecutionMode.QUEUED,
        )

        # Code build project, can be customised with env var, buildspec, ect.
        build_project = codebuild.PipelineProject(self, "StagingBuildProject")

        # Source stage - to be configured differently for production/staging/dev branches
        pipeline.add_stage(
            stage_name="Source",
            actions=[
                cpactions.CodeStarConnectionsSourceAction(
                    action_name="GitHub_Source",
                    owner="UCL-ARC",
                    repo="museum_of_dreams",
                    branch="feature/cdk-staging-env",
                    output=source_output,
                    connection_arn=ssm.StringParameter.value_for_string_parameter(
                        self, "/pipeline/github-connection-arn"
                    ),
                )
            ],
        )

        # Build stage
        pipeline.add_stage(
            stage_name="Build",
            actions=[
                cpactions.CodeBuildAction(
                    action_name="CodeBuild",
                    project=build_project,
                    input=source_output,
                    outputs=[build_output],
                )
            ],
        )

        # Deploy stage

        pipeline.add_stage(
            stage_name="Deploy",
            actions=[
                cpactions.ElasticBeanstalkDeployAction(
                    action_name="DeployToElasticBeanstalk",
                    application_name=STAGING_APP_NAME,
                    environment_name=STAGING_ENV_NAME,
                    input=build_output,
                )
            ],
        )
