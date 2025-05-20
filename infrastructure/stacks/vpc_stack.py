from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)

from constructs import Construct


class VPCStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            "CdkVPC",
            max_azs=2,  # sets the number of availability zones - each avaliabilty zone includes a public and a private subnet
            nat_gateways=0,  # sets the number of nat gateways
            subnet_configuration=[  # sets additional subnet configuration
                ec2.SubnetConfiguration(
                    name="PublicSubnet",  # assign name to public subnet
                    subnet_type=ec2.SubnetType.PUBLIC,
                ),
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",  # assign name to private subnet
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                ),
            ],
        )
