from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_elasticbeanstalk as eb,
    aws_iam as iam,
)

from constructs import Construct


class StagingStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "MyVPC", max_azs=2)
        # pipeline: CfnPipeline, CfnWebhook

        # ELastic beanstalk

        # App
        eb_app = eb.CfnApplication(
            self, "Staging", application_name="MOD-staging-test-app"
        )

        # permissions
        eb_role = iam.Role(
            self,
            "EBRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AWSElasticBeanstalkWebTier"
                )
            ],
        )
        eb_profile = iam.CfnInstanceProfile(
            self, "InstanceProfile", roles=[eb_role.role_name]
        )

        # Environment creation
        eb_env = eb.CfnEnvironment(
            self,
            "MODStagingEnv",
            application_name=eb_app.application_name,
            solution_stack_name="64bit Amazon Linux 2023 v4.5.1 running Python 3.11",
            option_settings=[
                {
                    "namespace": "aws:ec2:vpc",
                    "optionName": "VPCId",
                    "value": vpc.vpc_id,
                },
                {
                    "namespace": "aws:ec2:vpc",
                    "optionName": "Subnets",
                    "value": ",".join([subnet.subnet for subnet in vpc.public_subnets]),
                },
                {
                    "namespace": "aws:ec2:vpc",
                    "optionName": "ELBSubnets",
                    "value": ",".join([subnet.subnet for subnet in vpc.public_subnets]),
                },
                {
                    "namespace": "aws:autoscaling:launchconfiguration",
                    "optionName": "SecurityGroups",
                    "value": eb_profile.ref,
                },
                {
                    "namespace": "aws:elasticbeanstalk:environment",
                    "optionName": "EnvironmentType",
                    "value": "LoadBalanced",
                },
            ],
        )

        eb_env.add_dependency(eb_profile)
        eb_env.add_dependency(
            eb_role.node.default_child
        )  # Convert IAM Role(L2 construct) to CfnRole
