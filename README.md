# Museum of Dreams Website Project

This website is hosted at http://museumofdreams.eu-west-2.elasticbeanstalk.com/

Development should be done locally and staged to the website. At present this is not a production version.

## Local Development

Set up the project using the standard django method

```
mkdir museum_of_dreams_project
cd museum_of_dreams_project

python3 -m venv modvenv
source modvenv/bin/activate
pip install django

django-admin startproject mod-app
cd mod-app
python manage.py runserver
```

For AWS, you should create a `.ebextensions` folder in the top level of the project (it should be same level as `manage.py` and `requirements.txt`). In this folder create `01_packages.config` with the following contents:

```
packages:
  yum:
    mariadb105-devel: []
```

This will address issues with setting up the mysql db.

Also create `db-migrate.config` with the following contents:

```
container_commands:
  01_migrate:
    command: "source /var/app/venv/*/bin/activate && python manage.py migrate"
    leader_only: true
  02_collectstatic:
    command: "python manage.py collectstatic"
    leader_only: true
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: museum_of_dreams_project.settings

```

This will allow migrations and `collectstatic` to automatically run when the app is deployed.

In `settings.py` you should change the section on `DATABASES` to look like this:

```
IS_LOCAL_DEV = os.getenv("LOCAL_DEV", False)

if IS_LOCAL_DEV:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ["RDS_DB_NAME"],
            "USER": os.environ["RDS_USERNAME"],
            "PASSWORD": os.environ["RDS_PASSWORD"],
            "HOST": os.environ["RDS_HOSTNAME"],
            "PORT": os.environ["RDS_PORT"],
        }
    }

```

This will look for a local variable on your machine called `LOCAL_DEV` (set this up on your local machine when possible) and if it can't find it, it will use the credentials for the AWS RDS instance. This way, the AWS is default, whereas if we try to look for an environment variable on the EBS instance, it doesn't always compute the code correctly and would create a local sqlite3.db instance on the EC2 machine.

# Recreating AWS Setup

As this website is hosted on AWS you will need an account to access all of these services. There are a few things to set up across different services, namely:

- VPC
- IAM Roles
- Security Groups
- RDS
- ElasticBeanstalk
- CodePipeline

## VPC

Go to the VPC console. Click on `Your VPCs` or `VPCs`.
Create a new VPC with at least two subnets (probably preferably in the European Region).
From the menu on the left, select `Route Tables`. Create one for each subnet (this is best practice)
From the menu on the left, select `Internet Gateways`.Create and attach an Internet Gateway to the VPC you created. This will allow the app to access the internet.

## IAM Roles

Go to the IAM console. Under the `Access Management` heading on the left, select `Roles`.
Create a new Role and attach the following policies:

- AdministratorAccess-AWSElasticBeanstalk
- AmazonEC2FullAccess
- AmazonRDSFullAccess
- AWSElasticBeanstalkRoleRDS
- AWSElasticBeanstalkWebTier

These will allow for communication betweeen the ElasticBeanstalk application, the EC2 instances it will create to host the application and the RDS database.

## RDS

Go to the RDS console. Select `Databases` and then `Create new database`.
Choose standard create and MySQL (not the Aurora one unless you have a spare £800). Choose the free tier. Choose an appropriate identifier for the db and the same for the credentials.

The next thing to change is to attach it to the VPC you created. Choose one of the subnets it will live in. Do not allow public access.

You can check if there are any security groups available and select `rds-ec2-1` if you have access to it, otherwise, if you haven't created any security groups yourself, choose create new security group, I named mine `rds-ec2-1` since it will allow the `rds` instance to connect to the `ec2` instance, in `subnet 1` but you can choose another appropriate name. The rest you can leave as default.

Just allow password authentication.
Under `Additional Configurations` you should see `initial db name`, this should be `ebdb`. The rest can be left as default.

Create the db and wait for it to spin up.

## ElasticBeanstalk

We'll be using ElasticBeanstalk (EBS) to host our application as the process is a bit more streamlined than with just creating an EC2 instance since EBS allows for more abstraction and less manual config.

Go to the EBS console and choose `Applications` from the left side menu. Create a new Application with an appropriate name. Then create an environment:

Choose Web tier. I'd recommend customising the domain name for ease of access but you don't need to. The platform should be Python. Everything else on that page can be left as default.

On the next page (service access), select `use an existing role` and select the IAM role you created. If you have an EC2 key, feel free to add it (you'll be able to ssh into the EC2 instance from your local machine) but it's not necessary. Select the same IAM role for the EC2 instance profile.

On the next page, select the VPC you created, check that public IP is enabled, and select the subnet you chose for the RDS instance. Don't fill out the database section.

On the next page, select the security group you created for the RDS instance.

On the next page, scroll to the bottom where it should have `Environment Variables`. Add some new ones:

- RDS_HOSTNAME (this is the endpoint for the RDS instance)
- RDS_PORT (this should be 3306 unless you changed it)
- RDS_DB_NAME (this should be ebdb)
- RDS_USERNAME (this should be the username you chose or admin if you didn't change it)
- RDS_PASSWORD (this should be the master password you set on the db)

You can review and create the environment. This will take some time.

## Security Groups

Whilst the environment is being created, you can check if the security group you defined is available in the VPC console. It will be in `Security Groups` under the `Security` tab in the left hand menu.

If it's available, click on it and scroll to the bottom to edit inbound rules. Allow MySQl connections through the security group that was created for the scaling group attached to your environment, you may also want to allow SSH from this group.

Ensure that the security group you defined on the RDS instance (and then selected in the EBS setup) has been set for MySQL connections.

## CodePipeline

This step assumes you have code on GitHub for the web app. Go to the CodePipeline console and then `Pipelines`. Create a new pipeline. Choose V2 and create a new service role and name it. Everything else on this page can be left as default.

Choose GitHub v2 for the source, and then select the repo and branch. You may need to sign in to your GH account. If the repo is under an organisation, try typing the name as `<org name>/<repo name>`. If you don't have permissions, you should contact your administrator or relevant AWS advisor to set up a GitHub App to ensure it doesn't disrupt other connections.

After this, move on to the deploy step (skip build) and choose deploy and select the EBS environment you created.
This will automatically pull in changes to the branch you select and deploy them to the environment.
