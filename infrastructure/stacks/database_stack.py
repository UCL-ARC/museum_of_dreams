from aws_cdk import aws_ec2 as ec2, aws_rds as rds, RemovalPolicy

from constructs import Construct


class DatabaseStack:
    def __init__(
        self, scope: Construct, construct_id: str, env_vpc: ec2.IVpc, **kwargs
    ) -> None:
        super.__init__(scope, construct_id, **kwargs)

        # Security group for RDS
        rds_sg = ec2.SecurityGroup(self, "RDSInstanceSG", vpc=env_vpc)

        rds.DatabaseInstance(
            self,
            "CdkSQLDatabase",
            engine=rds.DatabaseInstanceEngine.mysql(
                "version=rds.MysqlEngineVersion.VER_8_0_34"
            ),
            credentials=rds.Credentials.from_generated_secret("admin"),
            vpc=env_vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO
            ),
            allocated_storage=20,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            security_groups=[rds_sg],
            publicly_accessible=False,
            removal_policy=RemovalPolicy.DESTROY,
            deletion_protection=False,
            multi_az=False,
        )
