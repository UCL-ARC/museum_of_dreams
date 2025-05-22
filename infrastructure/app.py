#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.vpc_stack import VPCStack
from stacks.staging_database_stack import StagingDatabaseStack

app = cdk.App()

vpc_stack = VPCStack(app, "VPCStack")
database_stack = StagingDatabaseStack(app, "StagingDbStack", vpc=vpc_stack.vpc)

app.synth()
