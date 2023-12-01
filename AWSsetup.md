# Current State of Affairs

Currently the AWS system is set up such that:

## VPC

There is one VPC called `MuseumofDreams`
This has 6 subnets across 3 availability zones (eu-west-2 a, b & c)

`eu-west-2a` has subnets `mod_subnet-a1`, `mod_subnet-a2` and `RDS-Pvt-subnet-1`. The `mod_subnet-a`s are used for the production site

`eu-west-2b` has subnets `mod_subnet-b1` and `RDS-Pvt-subnet-3`. This is for the staging site

`eu-west-2c` has `RDS-Pvt-subnet-2`. This isn't really used currently.

`eu-west-2a & b` have internet gateways attached to their respective routing tables and so are available to the internet.

## IAM

The IAM configuration is that laid out in the [IAM Roles section](settingUp.md) of setting up. The role is called `MuseumofDreams_EB_EC2`

## RDS

There are two RDS instances, one for staging (`mod-mysql-dev-db`) and one for prod (`mod-mysql-ebdb-prod`).

They are almost identical in their setup but the production availability zone is `eu-west-2c` and staging is `eu-west-2a` and they have different secondary security groups to connect with their respective environments - `rds-ec2-1` for production and `ec2-rds-1` for staging.

Please note that the subnets in the RDS console are `RDS-Pvt-subnet`

## ElasticBeanstalk

There is one EBS application - Museum od Dreams site and it has 2 environments - ...`env-1` which is production and ...`env-dev` for staging

The workflow is that development is done on a feature branch and this gets merged into `development` and the CodePipeline for the staging site deploys these updates. When these have been reviewed and approved, they can be merged into `main` and the production CodePipeline will deploy a new version of production.

Production uses the `rds-ec2-1` security group and should have availability zones matching `mod-subnet-a` and `RDS-Pvt-subnet-2`

Staging uses `ec2-rds-1` security group and should have availability zones matching `mod-subnet-b` and `RDS-Pvt-subnet-1`

There are saved configurations to launch instances from if issues arise and an environment needs to be terminated. Make sure you detach the security groups before doing this (can be done from the security group console).
The advised configurations are `db site` and `mod dev setup with db`. The difference is in the env variables defined at the end of the config - the `DB_HOSTNAME`s are different. These can always be updated if the wrong one is launched.

## Security Groups

As outlined above, production uses the `rds-ec2-1` security group. This should have rules to allow connections for MYSQL from the same security group (this is why we attach it to the RDS instance) and also one of these from the scaling group security group attached to the prod site environment.

The staging security group `ec2-rds-1` follows the same pattern.
