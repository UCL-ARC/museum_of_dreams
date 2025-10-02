# Cloudformation Stacks

- VpcStack
- DatabaseStack
- StagingStack/ProductionStack (Elastic Beanstalk environment)
- CodePipelineStack

## Deployment order

Vpc > Database > Environment > CodePipeline

## Naming conventions

Construct IDs should be in PascalCase or camelCase (this matches with how cloudformation generates resource name)

PascalCase is used in MOD:

`bucket = s3.Bucket(self, "MyAppBucket")`

## .ebextension

These files configures the env variables for EB environment when you deploy your code, notably wsgi path and django settings module - this helps avoid spinning up a degraded environment when deploying an EB environment with cdk

Example `.config` file:

```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: museum_of_dreams_project.wsgi

  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: museum_of_dreams_project.settings.staging
```
