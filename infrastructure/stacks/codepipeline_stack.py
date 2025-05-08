import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_s3 as s3,
    aws_codebuild as codebuild,
    aws_codepipeline_actions as cpactions,
)
from constructs import Construct


class CodePipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        artifact_bucket = s3.Buckect(self, "ArtifactBucket")
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        # Code build project, can be customised with env var, buildspec, ect.
        build_project = codebuild.PipelineProject(self, "CdkProject")

        # Pipeline
        pipeline = codepipeline.Pipeline(
            self, "CdkPipeline", artifact_bucket=artifact_bucket
        )

        # Source stage
        pipeline.add_stage(
            stage_name="Source",
            actions=[
                cpactions.GitHubSourceAction(
                    action_name="GitHub_Source",
                    owner="",
                    repo="",
                    oauth_token=cdk.SecretValue.secrets_manager(""),
                    output=source_output,
                    branch="",
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
