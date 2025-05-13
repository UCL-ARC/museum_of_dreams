from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_s3 as s3,
    aws_codepipeline_actions as cpactions,
    aws_iam as iam,
    aws_ssm as ssm,
    RemovalPolicy,
)

from constructs import Construct

from stacks.staging_stack import STAGING_APP_NAME, STAGING_ENV_NAME


class CodePipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        artifact_bucket = s3.Bucket(
            self,
            "ArtifactBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        source_output = codepipeline.Artifact()

        # Pipeline
        pipeline = codepipeline.Pipeline(
            self, "CdkPipeline", artifact_bucket=artifact_bucket
        )

        # Source stage - to be configured differently for production/staging/dev branches
        pipeline.add_stage(
            stage_name="Source",
            actions=[
                cpactions.CodeStarConnectionsSourceAction(
                    action_name="GitHub_Source",
                    owner="UCL-ARC",
                    repo="museum_of_dreams",
                    branch="feature/cdk-codepipeline",
                    output=source_output,
                    connection_arn=ssm.StringParameter.value_for_string_parameter(
                        self, "/pipeline/github-connection-arn"
                    ),
                )
            ],
        )

        # Grant Permission via IAM Role to Pipeline for Elastic Beanstalk Deployment

        iam.Role(
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

        # Deploy stage

        pipeline.add_stage(
            stage_name="Deploy",
            actions=[
                cpactions.ElasticBeanstalkDeployAction(
                    action_name="DeployToElasticBeanstalk",
                    application_name=STAGING_APP_NAME,
                    environment_name=STAGING_ENV_NAME,
                    input=source_output,
                )
            ],
        )
