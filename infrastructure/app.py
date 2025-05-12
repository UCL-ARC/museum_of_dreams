#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.vpc_stack import VPCStack
from stacks.database_stack import DatabaseStack

app = cdk.App()

vpc_stack = VPCStack(
    app,
    "CdkVPCStack",
)

database_stack = DatabaseStack(
    app,
    "CdkDatabaseStack",
)

app.synth()
