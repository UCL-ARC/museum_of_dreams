#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.production_stack import ProductionStack
from stacks.staging_stack import StagingStack
from stacks.codepipeline_stack import CodePipelineStack
from stacks.database_stack import DatabaseStack
from stacks.vpc_stack import CdkVPCStack

app = cdk.App()

vpc_stack = CdkVPCStack(
    app,
    "CdkVPCStack",
)

database_stack = DatabaseStack(
    app,
    "DatabaseStack",
    vpc=vpc_stack.vpc,
)

staging_stack = StagingStack(
    app,
    "StagingStack",
    vpc=vpc_stack.vpc,
    db_secret=database_stack.secret,
)

production_stack = ProductionStack(
    app,
    "ProductionStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    # env=cdk.Environment(account='123456789012', region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)

pipeline_stack = CodePipelineStack(
    app,
    "CodePipelineStack",
)

database_stack.add_dependency(vpc_stack)
staging_stack.add_dependency(vpc_stack)
pipeline_stack.add_dependency(staging_stack)
app.synth()
