#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.vpc_stack import VPCStack
from stacks.staging_database_stack import StagingDatabaseStack

app = cdk.App()

vpc_stack = VPCStack(
    app,
    "VPCStack",
    description="Stack for VPC, sets up a VPC network that is used in RDS & EB stacks",
)
database_stack = StagingDatabaseStack(
    app,
    "StagingDbStack",
    description="Stack for staging database(can be deleted), also contains relevant security groups for RDS & EB",
    vpc=vpc_stack.vpc,
)

app.synth()
