import aws_cdk as core
import aws_cdk.assertions as assertions

from stacks.production_stack import ProductionStack


# example tests. To run these tests, uncomment this file along with the example
# resource in infrastructure/infrastructure_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProductionStack(app, "ProductionStack")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
