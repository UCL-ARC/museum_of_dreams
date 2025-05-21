# Relational Database Service

RDS stacks should be deployed after VPC stack and before Elastic Beanstalk environments, this is because the Elastic Beanstalk Stack will need information from database to use as environment variables.

## Security Group:

Security group for both database and elastic beanstalk environment are set up in `database_stack.py`

## Defining a database instance:

```python
from aws_cdk aws_rds as rds

rds.DatabaseInstance(
    self,
    "CdkSQLDatabase",
    # include any additional parameters
)
```

View [Official AWS doc on DatabaseInstance](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_rds/DatabaseInstance.html) for parameters options

## Example configuration:

Below is a list of parameters we have used for configuring a database instance:

- `database_name`: your database name (Only alpha-numeric characters allowed)
- `engine`: database engine type (e.g. `rds.DatabaseInstanceEngine.mysql`)
- `version`: databse engine version ( e.g. `rds.MysqlEngineVersion.VER_8_0_41`)
- `credentials`: `rds.Credentials.from_generated_secret("admin")`(this uses aws secret manager which generates credentials like username/password automatically),
- `vpc`: select the vpc the database will be using,
- `vpc_subnets`: select the subnets the databse will be using (e.g. `ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)`)
- `instance_type`: chooses the database instance type, related with performance (e.g. `ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.MICRO)`)
- `allocated_storage`: specific the capacity of the database in GiB (e.g.`20`)
- `security_groups`: select the security group the database will be using (e.g.)`[self.database_sg]`
- `publicly_accessible`: should be set to `False` at all time for security
- `deletion_protection`: Prevents users from deleting the database. Set to `False` for staging, `True` for production
- `multi_az`: specify number of availability zones to host in. Set to `False` for single availability zone.
- `parameters`: additional parameters for the database itself`{"sql_mode": "STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION"}`
