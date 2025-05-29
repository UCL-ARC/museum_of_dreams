from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_elasticbeanstalk as eb,
    aws_iam as iam,
    aws_rds as rds,
    aws_s3 as s3,
)

from constructs import Construct


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
            self, "Staging", application_name="MOD-staging-test-app"
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

        staging_bucket = s3.Bucket(
            self,
            "StagingBucket",
            versioned=False,
            public_read_access=False,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=s3.RemovalPolicy.DESTROY,  # Only for dev/test environments
            auto_delete_objects=True,  # Only for dev/test
        )

        staging_bucket.grant_read_write(eb_role)

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
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_DB_NAME",
                value=database_name,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_HOSTNAME",
                value=database_instance.db_instance_endpoint_address,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_PORT",
                value=database_instance.db_instance_endpoint_port,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_USERNAME",
                value="",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_PASSWORD",
                value="",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="BUCKET_NAME",
                value=staging_bucket.bucket_name,
            ),
        ]

        # Environment creation
        eb_env = eb.CfnEnvironment(
            self,
            "MODStagingEnv",
            application_name=eb_app.application_name,
            solution_stack_name="64bit Amazon Linux 2023 v4.5.1 running Python 3.11",
            option_settings=staging_env_settings,
        )

        # Elastic beanstalk dependencies (to ensure correct order of creation/deployment/deletion)
        eb_env.add_dependency(eb_profile)
        eb_env.add_dependency(eb_role.node.default_child)
