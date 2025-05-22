#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.vpc_stack import VPCStack
from stacks.database_stack import DatabaseStack

app = cdk.App()

vpc_stack = VPCStack(app, "VPCStack")
database_stack = DatabaseStack(app, "StagingDbStack", vpc=vpc_stack.vpc)

app.synth()
