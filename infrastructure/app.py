#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.production_stack import ProductionStack
from stacks.staging_stack import StagingStack
from stacks.vpc_stack import VPCStack
from stacks.database_stack import DatabaseStack

app = cdk.App()

vpc_stack = VPCStack(app, "CdkVPCStack")
database_stack = DatabaseStack(app, "CdkDatabaseStack", vpc=vpc_stack.vpc)
staging_stack = StagingStack(app, "StagingStack")
production_stack = ProductionStack(app, "ProductionStack")

app.synth()
