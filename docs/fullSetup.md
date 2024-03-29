# If starting from scratch (not cloning repo)

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

Also create [db-migrate.config](../.ebextensions/db-migrate.config).

This will allow migrations and `collectstatic` to automatically run when the app is deployed.

## Settings

We have separate settings files for AWS and local development.
See [settings/local.py](museum_of_dreams_project/settings/local.py) and [settings/aws.py](museum_of_dreams_project/settings/aws.py) for the contents. There is a staging.py which is for the staging environment on AWS to define a separate host.

You also need to point `wsgi.py` and `asgi.py` to the AWS settings file

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

On the next page, turn off (uncheck) managed updates (these so far have only caused issues when they run and fail) and scroll to the `Platform Software` section, it should ask you to define the `WSGI path`, it should be `museum_of_dreams_project.wsgi`.

Next, scroll to the bottom where it should have `Environment Variables` or `Environment Properties`. Add some new ones:

- `DJANGO_SETTINGS_MODULE` (this is the path to your settings/aws.py file <project>.settings.aws)
- `RDS_HOSTNAME` (this is the endpoint for the RDS instance)
- `RDS_PORT` (this should be 3306 unless you changed it)
- `RDS_DB_NAME` (this should be ebdb)
- `RDS_USERNAME` (this should be the username you chose or admin if you didn't change it)
- `RDS_PASSWORD` (this should be the master password you set on the db)

Above this section is a `Static Files` section. You should add `/media` and `/static` as paths, with `media` and `static` as their respective directories.

If you plan to use S3 for your static files, please see [S3 for static files](s3ForStatic.md)

You can review and create the environment. This will take some time.

## Security Groups

Whilst the environment is being created, you can check if the security group you defined is available in the VPC console. It will be in `Security Groups` under the `Security` tab in the left hand menu.

If it's available, click on it and scroll to the bottom to edit inbound rules. Allow MySQl connections through the security group that was created for the scaling group attached to your environment, you may also want to allow SSH from this group.

Ensure that the security group you defined on the RDS instance (and then selected in the EBS setup) has been set for MySQL connections.

## CodePipeline

This step assumes you have code on GitHub for the web app. Go to the CodePipeline console and then `Pipelines`. Create a new pipeline. Choose V2 and create a new service role and name it. Everything else on this page can be left as default.

Choose GitHub v2 for the source, and then select the repo and branch. You may need to create a new connection and sign in to your GH account. Otherwise, select the connection to your GH account.

If the repo is under an organisation, try typing the name as `<org name>/<repo name>`. **If you don't have permissions, you should contact your administrator or relevant AWS advisor to set up a GitHub App to ensure it doesn't disrupt other connections.**

After this, move on to the deploy step (skip build) and choose deploy and select the EBS environment you created.
This will automatically pull in changes to the branch you select and deploy them to the environment.

_**NB**_

If you have more than one environment (one for prod, one for staging for eg.), you should have separate pipelines for each. The current CodePipelines pull from `main` for production and `development` for staging.

## Logging into the Admin

Once you've set everything up, check you can access the website at the domain you set (or through the EBS console: `Go to environment` button). If this seems to be in order, go to the EC2 console and find the associated instance for your EBS environment. Click `connect` and you're free to connect through the browser (default method). Once you're in the shell, you'll need to navigate to the app and create a superuser so you can log in to the admin site.

```
cd /var/app
source venv/staging-LQM1lest/bin/activate
cd current
```

We have to expose the variables from the EBS environment to the shell we're in

```
export $(/opt/elasticbeanstalk/bin/get-config --output YAML environment |  sed -r 's/: /=/' | xargs)
```

If this is the first time setting up this app, you may need to run the migrations (this should be handled automatically in future with the `db-migrate.config` file in `.ebextensions`)

```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

Follow the steps to create a superuser and then you should be able to log into the admin inerface
