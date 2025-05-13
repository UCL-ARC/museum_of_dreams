#!/usr/bin/env python3
import os

import aws_cdk as cdk
from stacks.vpc_stack import CdkVPCStack

app = cdk.App()

vpc_stack = CdkVPCStack(
    app,
    "CdkVPCStack",
)

app.synth()
