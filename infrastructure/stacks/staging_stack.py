from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_elasticbeanstalk as eb,
    aws_iam as iam,
    # aws_s3_assets,
)

from constructs import Construct

# EB APP AND ENV NAMES SHOULD NOT BE A EMPTY VALUE
STAGING_APP_NAME = "MOD-staging-test-app"
STAGING_ENV_NAME = "MODStagingEnv"


class StagingStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, vpc: ec2.IVpc, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Security Group - EBS
        self.eb_sg = ec2.SecurityGroup(
            self, "EBInstanceSG", vpc=vpc, allow_all_outbound=True
        )
        self.eb_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(80)
        )  # allow public access

        # ELastic beanstalk

        # App
        eb.CfnApplication(self, "Staging", application_name=STAGING_APP_NAME)

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

        eb_env_settings = [
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
                namespace="aws:ec2:vpc", option_name="VPCId", value=vpc.vpc_id
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:ec2:vpc",
                option_name="Subnets",
                value=",".join([subnet.subnet_id for subnet in vpc.public_subnets]),
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:ec2:vpc",
                option_name="ELBSubnets",
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
                value=self.eb_sg.security_group_id,
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:environment",
                option_name="EnvironmentType",
                value="SingleInstance",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:autoscaling:asg",
                option_name="MinSize",
                value="1",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:autoscaling:asg",
                option_name="MaxSize",
                value="1",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:container:python",
                option_name="WSGIPath",
                value="museum_of_dreams_project.wsgi",
            ),
            # Environment variables
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="DJANGO_SETTINGS_MODULE",
                value="museum_of_dream_project.settings.aws",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_HOSTNAME",
                value="",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_PORT",
                value="3306",
            ),
            eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:elasticbeanstalk:application:environment",
                option_name="RDS_DB_NAME",
                value="",
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
        ]

        # Environment creation
        eb_env = eb.CfnEnvironment(
            self,
            "MODStagingEnv",
            application_name=STAGING_APP_NAME,
            environment_name=STAGING_ENV_NAME,
            solution_stack_name="64bit Amazon Linux 2023 v4.5.1 running Python 3.11",
            option_settings=eb_env_settings,
        )

        # Elastic beanstalk dependencies (to ensure correct order of creation/deployment/deletion)
        eb_env.add_dependency(eb_profile)
        eb_env.add_dependency(
            eb_role.node.default_child
        )  # Convert IAM Role(L2 construct) to CfnRole

        # For easier cdk destroys, need to setup environment to delete before the app
        # eb_app.node.add_dependency(eb_env)
