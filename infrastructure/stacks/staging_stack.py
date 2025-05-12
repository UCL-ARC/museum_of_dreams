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
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "StagingVPC", max_azs=2)

        # Security Group - EBS
        eb_sg = ec2.SecurityGroup(
            self, "EBInstanceSG", vpc=vpc, allow_all_outbound=True
        )
        eb_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80))  # public access

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

        # Environment creation
        eb_env = eb.CfnEnvironment(
            self,
            "MODStagingEnv",
            application_name=STAGING_APP_NAME,
            environment_name=STAGING_ENV_NAME,
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
                    "value": ",".join(
                        [subnet.subnet_id for subnet in vpc.public_subnets]
                    ),
                },
                {
                    "namespace": "aws:ec2:vpc",
                    "optionName": "ELBSubnets",
                    "value": ",".join(
                        [subnet.subnet_id for subnet in vpc.public_subnets]
                    ),
                },
                {
                    "namespace": "aws:autoscaling:launchconfiguration",
                    "optionName": "IamInstanceProfile",
                    "value": eb_profile.ref,
                },
                {
                    "namespace": "aws:autoscaling:launchconfiguration",
                    "optionName": "SecurityGroups",
                    "value": eb_sg.security_group_id,
                },
                {
                    "namespace": "aws:elasticbeanstalk:environment",
                    "optionName": "EnvironmentType",
                    "value": "LoadBalanced",
                },
                {
                    "namespace": "aws:elasticbeanstalk:container:python",
                    "optionName": "WSGIPath",
                    "value": "museum_of_dreams_project.wsgi",
                },
            ],
        )

        # Elastic beanstalk dependencies (to ensure correct order of creation/deployment/deletion)
        eb_env.add_dependency(eb_profile)
        eb_env.add_dependency(
            eb_role.node.default_child
        )  # Convert IAM Role(L2 construct) to CfnRole

        # For easier cdk destroys, need to setup environment to delete before the app
        # eb_app.node.add_dependency(eb_env)
