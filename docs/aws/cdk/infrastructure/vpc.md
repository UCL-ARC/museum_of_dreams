# Virtual Private Cloud

VPC stacks should always be deployed first, this is because most other stacks (e.g. database, elasticbean stalk), are dependent on a VPC.

## Source code location

`project_root/infrastructure/stacks/vpc_stack.py`

## Configuration

```python
class VPCStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # the VPC instance is stored in a class field, this is so that this VPC could be reference later in app.py for other stacks that needs a VPC to attach to
        self.vpc = ec2.Vpc(
            self,
            "CdkVPC", # ID
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

```
