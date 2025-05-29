#!/usr/bin/env python3

import aws_cdk as cdk
from stacks.production_stack import ProductionStack
from stacks.staging_stack import StagingStack
from stacks.vpc_stack import VPCStack
from stacks.staging_database_stack import StagingDatabaseStack

app = cdk.App()

vpc_stack = VPCStack(
    app,
    "VPCStack",
    description="Stack for VPC, sets up a VPC network that is used in RDS & EB stacks",
)
staging_db_stack = StagingDatabaseStack(
    app,
    "StagingDbStack",
    description="Stack for staging database(can be deleted), also contains relevant security groups for RDS & EB",
    vpc=vpc_stack.vpc,
)
staging_stack = StagingStack(
    app,
    "StagingStack",
    vpc=vpc_stack.vpc,
    security_group=staging_db_stack.elasticbeanstalk_sg,
    database_name=staging_db_stack.db_name,
    database_instance=staging_db_stack.db_instance,
)
production_stack = ProductionStack(app, "ProductionStack")

staging_pipeline_stack = StagingPipelineStack(
    app,
    "StagingPipelineStack",
    staging_app_name=staging_stack.eb_app.application_name,
    staging_env_name=staging_stack.eb_env.environment_name,
)


app.synth()
