#!/usr/bin/env python3
import os

import aws_cdk as cdk
from stacks.production_stack import ProductionStack
from stacks.staging_stack import StagingStack
from stacks.codepipeline_stack import CodePipelineStack
from stacks.database_stack import DatabaseStack

app = cdk.App()
staging_stack = StagingStack(
    app,
    "StagingStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)

production_stack = ProductionStack(
    app,
    "ProductionStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.
    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */
    # env=cdk.Environment(account='123456789012', region='us-east-1'),
    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
)
pipeline_stack = CodePipelineStack(
    app,
    "CodePipelineStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)
database_stack = DatabaseStack(
    app,
    "DatabaseStack",
    vpc=staging_stack.vpc,
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)

pipeline_stack.add_dependency(staging_stack)
database_stack.add_dependency(staging_stack)
app.synth()
