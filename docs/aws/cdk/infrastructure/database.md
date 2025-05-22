# Relational Database Service Stack

## Important:

- RDS stacks should be deployed after VPC stack and before Elastic Beanstalk environments, this is because the Elastic Beanstalk Stack will need to use database credentials as environment variables.

- Security group for both `database` and `elastic beanstalk environment` are created inside `database_stack.py`

## Official AWS documentation/ resources (Python)

- [AWS API reference for RDS](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_rds.html)
- [Examples/ parameters for the DatabaseInstance construct](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_rds/DatabaseInstance.html)

## Defining a database instance:

```python
from aws_cdk import aws_rds as rds

rds.DatabaseInstance(
    self,
    "CdkSQLDatabase", # The database construct ID, must be unique relative to the scope of
    # include any additional parameters
)
```

## Example configuration:

Below is the configuration we have used to set up a minimal MySQL instance:

### Engine, hardware settings:

```python
self.db_instance = rds.DatabaseInstance(
            self,
            id="CdkSQLDatabase", # sets database ID
            database_name="CdkSQLDatabase", # sets database's display name

            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_41
            ), # sets engine type to MySQL, and version to 8.0.41

            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.MICRO
            ), # sets database instance class to db.t4g.micro

            allocated_storage=20, # sets storage capacity to 20 GiB
```

### Credential generation

```python
            credentials=rds.Credentials.from_generated_secret("admin"),
            # this generates a username (admin) and a password in aws secret manager for the database
```

### VPC, security settings

```python
            vpc=vpc, # select the vpc
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ), # assigns database instance to private subnets within your vpc

            security_groups=[self.database_sg], # selects the security group(s) for the instance
            publicly_accessible=False, # disable public access for security purposes
```

### Miscellaneous settings

```python
            removal_policy=RemovalPolicy.DESTROY,
            # enables database items to be deleted along with the database itself
            deletion_protection=False, # enables quick database deletion
            multi_az=False, # uses a single availability zone for the instance
            parameters={"sql_mode": "STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION"}, # enables StrictMode for MySQL
        )

```

## Parameters notes:

- `id`: specifies a construct id for the instance - this must be unique within the Relational Database Service scope.
- `database_name`: your database name as shown (is restricted to only alpha-numeric characters)
- `engine`: database engine type (e.g. `PostgreSQL`,`MySQL`)
- `version`: database engine version (e.g. `8.0.41`)
- `instance_type`: the compute name and memory capacity (e.g `db.t4g.micro`)
- `allocated_storage`: specify the capacity of the database in `gibibytes(GiB)`
- `credentials`: your database's root admin information (usually a username and a generated password from secrets manager)
- `vpc`: selects the vpc the database will be using
- `vpc_subnets`: selects the subnets the database will be using
- `security_groups`: selects the security group the database will be using
- `publicly_accessible`: should be set to `False` at all time for security purposes
- `deletion_protection`: prevents users from deleting the database. Should be set to `False` for staging, `True` for production
- `multi_az`: specifies if the database instance is a multiple Availability Zone deployment
- `parameters`: you can configure additional parameters for the database itself (e.g. enable StrictMode for MySQL)
