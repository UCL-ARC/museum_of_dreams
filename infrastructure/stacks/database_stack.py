from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct


class DatabaseStack:
    def __init__(
        self, scope: Construct, construct_id: str, env_vpc: ec2.IVpc, **kwargs
    ) -> None:
        super.__init__(scope, construct_id, **kwargs)

        # Security group for RDS
        rds_sg = ec2.SecurityGroup(self, "RDSInstanceSG", vpc=env_vpc)
