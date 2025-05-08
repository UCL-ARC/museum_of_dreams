from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_s3 as s3,
    aws_codebuild as codebuild,
    aws_codepipeline_actions as cpactions,
    aws_iam as iam,
)
from constructs import Construct


class CodePipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        artifact_bucket = s3.Bucket(self, "ArtifactBucket")
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()
        build_spec = codebuild.BuildSpec.from_source_filename("buildspec.yaml")

        # Code build project, can be customised with env var, buildspec, ect.
        build_project = codebuild.PipelineProject(
            self, "CdkProject", build_spec=build_spec
        )

        # Pipeline
        pipeline = codepipeline.Pipeline(
            self, "CdkPipeline", artifact_bucket=artifact_bucket
        )

        # Source stage - configured different for production/staging/dev branches
        pipeline.add_stage(
            stage_name="Source",
            actions=[
                cpactions.CodeStarConnectionsSourceAction(
                    action_name="GitHub_Source",
                    owner="UCL-ARC",
                    repo="museum_of_dreams",
                    branch="feature/cdk-codepipeline",
                    output=source_output,
                    connection_arn="",
                    # needs to setup a parameter first in system manager
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

        # Grant Permission via IAM Role to Pipeline for Elastic Beanstalk Deployment

        eb_deploy_role = iam.Role(
            self,
            "EBDeployRole",
            assumed_by=iam.ServicePrincipal("codepipeline.amazonzws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSElasticBeanstalkFullAccess"
                )  # to be limited
            ],
        )

        # Deploy stage

        pipeline.add_stage(
            stage_name="Deploy",
            actions=[
                cpactions.ElasticBeanstalkDeployAction(
                    action_name="DeployToElasticBeanstalk",
                    application_name="",
                    environment_name="",
                    input=build_output,
                )
            ],
        )
