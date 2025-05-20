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

        # Security group

        # EB
        self.elasticbeanstalk_sg = ec2.SecurityGroup(
            self,
            "CDkElasticBeanstalkSG",
            vpc=vpc,
            security_group_name="CdkElasticBeanstalkSG",
            allow_all_outbound=True,
        )

        self.elasticbeanstalk_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(80)
        )  # allow public access

        self.elasticbeanstalk_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(443), "Allow HTTPS"
        )

        # Database
        self.database_sg = ec2.SecurityGroup(
            self,
            "CdkDatabaseSG",
            vpc=vpc,
            security_group_name="CdkDatabaseSG",
        )
        # expose elasticbeanstalk's security group to the database
        self.database_sg.add_ingress_rule(
            self.elasticbeanstalk_sg, ec2.Port.tcp(3306), "Allow EB access to MySQL"
        )

        self.database_name = "CdkDatabase"

        self.db_instance = rds.DatabaseInstance(
            self,
            "CdkSQLDatabase",
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
