# Stacks (wip)

(Subject to change)

- VpcStack
- DatabaseStack
- StagingStack/ProductionStack (environment)
- CodePipelineStack

## Deployment order (wip)

Vpc > Database > Environment > CodePipeline

## Naming conventions (wip)

construct ID should be PascalCase or camelCase(this matches with how cloudformation generates resource name)

PascalCase is used in MOD:

`bucket = s3.Bucket(self, "MyAppBucket")`
