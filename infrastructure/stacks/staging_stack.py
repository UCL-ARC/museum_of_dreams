from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_elasticbeanstalk as eb,
    aws_iam as iam,
    aws_rds as rds,
)

from constructs import Construct

STAGING_APP_NAME = "MODStagingApp"
STAGING_ENV_NAME = "MODStagingEnv"


class StagingStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: ec2.IVpc,
        security_group: ec2.ISecurityGroup,
        database_name: str,
        database_instance: rds.IDatabaseInstance,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defining ELastic Beanstalk App
        eb_app = eb.CfnApplication(
            self,
            "MODStagingApp",
            application_name=STAGING_APP_NAME,
        )

        # Create IAM role with necessary permission for web server environment
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

        # Create Instance Profile for EB, this could then be assumed by EC2 instances when they're launched via beanstalk
        eb_profile = iam.CfnInstanceProfile(
            self, "InstanceProfile", roles=[eb_role.role_name]
        )

        staging_env_settings = [
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:autoscaling:launchconfiguration",
                option_name="InstanceType",
                value="t2.micro",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:autoscaling:launchconfiguration",
                option_name="IamInstanceProfile",
                value=eb_profile.ref,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:ec2:vpc",
                option_name="VPCId",
                value=vpc.vpc_id,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:ec2:vpc",
                option_name="Subnets",
                value=",".join([subnet.subnet_id for subnet in vpc.public_subnets]),
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:autoscaling:launchconfiguration",
                option_name="IamInstanceProfile",
                value=eb_profile.ref,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:autoscaling:launchconfiguration",
                option_name="SecurityGroups",
                value=security_group.security_group_id,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:environment",
                option_name="EnvironmentType",
                value="SingleInstance",
            ),
        ]

        # Environment creation
        eb_env = eb.CfnEnvironment(
            self,
            "MODStagingEnv",
            application_name=STAGING_APP_NAME,
            environment_name=STAGING_ENV_NAME,
            solution_stack_name="64bit Amazon Linux 2023 v4.5.1 running Python 3.11",
            option_settings=staging_env_settings,
        )

        # Elastic beanstalk dependencies (to ensure correct order of creation/deployment/deletion)
        eb_env.add_dependency(eb_profile)
        eb_env.add_dependency(eb_role.node.default_child)
