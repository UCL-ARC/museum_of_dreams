from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    RemovalPolicy,
)

from constructs import Construct


class DatabaseStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: ec2.IVpc,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Setting up Security Group for Elastic Beanstalk, adding appropriate ingress rules
        self.elasticbeanstalk_sg = ec2.SecurityGroup(
            self,
            "CDkElasticBeanstalkSG",
            vpc=vpc,
            security_group_name="CdkElasticBeanstalkSG",
            description="Security Group for ElasticBeanstalk environment, created via CDK",
            allow_all_outbound=True,
        )

        self.elasticbeanstalk_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow inbound access via HTTP from any Ipv4 address",
        )

        self.elasticbeanstalk_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow inbound access via HTTPS from any Ipv4 address",
        )

        # Setting up Security Group for MySQL, adding appropriate ingress rules
        self.database_sg = ec2.SecurityGroup(
            self,
            "CdkDatabaseSG",
            vpc=vpc,
            security_group_name="CdkDatabaseSG",
            description="Security Group for CdkDatabase, created via CDK",
        )

        self.database_sg.add_ingress_rule(
            peer=self.elasticbeanstalk_sg,
            connection=ec2.Port.tcp(3306),
            description="Allow inbound access of the database from the ElasticBeanstalk security group",
        )

        # Defining MySQL database
        self.database_name = "CdkDatabase"

        self.db_instance = rds.DatabaseInstance(
            self,
            "CdkDatabase",
            database_name=self.database_name,
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_41
            ),
            credentials=rds.Credentials.from_generated_secret("admin"),
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.MICRO
            ),
            allocated_storage=20,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            security_groups=[self.database_sg],
            publicly_accessible=False,
            removal_policy=RemovalPolicy.DESTROY,
            deletion_protection=False,
            multi_az=False,
            parameters={"sql_mode": "STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION"},
        )
