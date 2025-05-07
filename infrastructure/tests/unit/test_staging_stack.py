import aws_cdk as cdk
import aws_cdk.assertions as assertions

from stacks.staging_stack import StagingStack


# example tests. To run these tests, uncomment this file along with the example
# resource in infrastructure/infrastructure_stack.py
def test_sqs_queue_created():
    app = cdk.App()
    stack = StagingStack(app, "StagingStack")
    template = assertions.Template.from_stack(stack)
    # template.has_resource("AWS::ElasticBeanstalk::Application",)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
