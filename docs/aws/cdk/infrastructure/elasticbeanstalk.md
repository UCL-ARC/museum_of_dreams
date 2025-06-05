# Elastic Beanstalk Stack

There will be two different stack for spinning up Elastic Beanstalk Environment Instances: `staging_stack.py` and `production_stack.py`. Specific settings will vary accordingly to serve their purpose.

## Important:

## Setting environment variables for S3 bucket static files

In the post deploy script, collectstatic will fail if:

- The environment variable `AWS_ACCESS_KEY_ID` and `AWS_SECRET_KEY` is not set

In the current setup, all elastic beanstalk instances are using the access key ID and secret key from IAM user `mod_site`. When spinning up new instance via CDK, we'll need to also manually update the IAM policy `get-put-objets` for this `mod_site` user to allow access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject", "s3:GetObjectAttributes", "s3:DeleteObject", "s3:ListBucket"],
      "Resource": [
        // add your arn of your bucket followed by /*
        // example:
        "arn:aws:s3:::your-cdk-bucket-name/*"
      ]
    }
  ]
}
```

## Stack configuration in `app.py`

The elastic beanstalk stack(s) itself require a few extra arguments to initialise:

- `vpc`: an vpc instance
- `security_group`: an security group for the elastic beanstalk
- `database_name`: an alphanumeric string
- `database_instance`: an database instance

### Example Usage

```python
staging_stack = StagingStack(
    app,
    "StagingStack",
    vpc=vpc_stack.vpc, # referencing the vpc instance defined in VPCStack
    security_group=staging_db_stack.elasticbeanstalk_sg, # referencing the elastic beanstalk security group defined in StagingDatabaseStack
    database_name=staging_db_stack.db_name, # referencing the database name defined in StagingDatabaseStack
    database_instance=staging_db_stack.db_instance, # referencing the database instance defined in StagingDatabaseStack
)
```

## Official AWS documentation/ resources (Python)

- [AWS API reference for Elastic Beanstalk]()
- [Examples/ parameters for the EB construct]()

## Defining an Elastic Beanstalk app & environment:

(coming soon)

## Configurations

```python
# assigns subnets for the ec2 instance, the type of subnet depends on whether you would like it to be publically accessible.
eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:ec2:vpc",
                option_name="Subnets",
                value=",".join([subnet.subnet_id for subnet in vpc.public_subnets]),
            ),

# assigns subnets for loadbalancer, omit if not using loadbalancers
eb.CfnEnvironment.OptionSettingProperty(
                namespace="aws:ec2:vpc",
                option_name="ELBSubnets",
                value=",".join([subnet.subnet_id for subnet in vpc.public_subnets]),
            ),
```
