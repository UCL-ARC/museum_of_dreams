import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_s3 as s3,
    aws_codebuild as codebuild,
    aws_codepipeline_actions as cpactions,
    aws_ssm as ssm,
)
from constructs import Construct


class CodePipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        artifact_bucket = s3.Buckect(self, "ArtifactBucket")
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
                cpactions.GitHubSourceAction(
                    action_name="GitHub_Source",
                    owner="UCL-ARC",
                    repo="museum_of_dreams",
                    branch="feature/cdk-codepipeline",
                    output=source_output,
                    connection_arn=ssm.StringParameter.value_for_string_parameter(
                        self, "/pipeline/github-connection-arn"
                    ),  # needs to setup a parameter first in system manager
                )
            ],
        )

        # Build stage
        pipeline.add_stage(
            stage_name="Build",
            action=[
                cpactions.CodeBuildAction(
                    action_name="CodeBuild",
                    project=build_project,
                    input=source_output,
                    outputs=[build_output],
                )
            ],
        )
