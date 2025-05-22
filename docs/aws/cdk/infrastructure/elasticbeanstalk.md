# Elastic Beanstalk Stack

(to be changed)

There will be two different stack for spinning up Elastic Beanstalk Environment Instances: `staging_stack.py` and `production_stack.py`, their settings will vary accordingly

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
