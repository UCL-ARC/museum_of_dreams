from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_elasticbeanstalk as eb,
    aws_iam as iam,
    aws_s3 as s3,
    aws_codebuild as codebuild,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpactions,
)

from constructs import Construct


class StagingStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # bucket: s3.Bucket()
        # pipeline: CfnPipeline, CfnWebhook

        # ELastic beanstalk

        # App
        eb_app = eb.CfnApplication(self, "Staging", application_name="Staging")

        # permissions
        eb_role = iam.Role(
            self, "EBRole", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )
        eb_profile = iam.CfnInstanceProfile(
            self, "InstanceProfile", roles=[eb_role.role_name]
        )

        # Environment creation
        eb_env = eb.CfnEnvironment(
            self,
            "MODStagingEnv",
            environment_name="MODStagingEnv",
            application_name=eb_app.application_name,
            solution_stack_name="64bit Amazon Linux 2023/4.0.9 running Python 3.11",
        )
