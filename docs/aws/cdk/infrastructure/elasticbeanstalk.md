# Elastic Beanstalk Stack

There will be two different stack for spinning up Elastic Beanstalk Environment Instances: `staging_stack.py` and `production_stack.py`. Specific settings will vary accordingly to serve their purpose.

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
