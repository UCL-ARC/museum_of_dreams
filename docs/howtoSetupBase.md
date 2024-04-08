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

You should also create a `.platform` directory, which will execute scripts when an instance starts. **This is not within the `.ebextensions` directory.**

Create [db-migrate script](../.platform/hooks/postdeploy/01_db-migrate.sh) and [nginx upload conf](../.platform/nginx/conf.d/proxy.conf)

These will allow migrations and `collectstatic` to automatically run when the app is deployed and will print some output to the logs, which may assist with debugging; and for the upload amount to be increased.



## Settings

We have separate settings files for AWS and local development.
See [settings/local.py](../museum_of_dreams_project/settings/local.py) and [settings/aws.py](../museum_of_dreams_project/settings/aws.py) for the contents. There is a [staging.py](../museum_of_dreams_project/settings/staging.py) which is for the staging environment on AWS to define a separate host.

You also need to point `wsgi.py` and `asgi.py` to the AWS settings file.

# Recreating AWS Setup

These instructions will walk you through creating one web app. It is recommended you repeat some of the processes so that you can have separate development/staging and production versions.

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
Create a new Role for the EC2 instances and attach the following policies:

- AdministratorAccess-AWSElasticBeanstalk
- AmazonEC2FullAccess
- AmazonRDSFullAccess
- AWSElasticBeanstalkRoleRDS
- AWSElasticBeanstalkWebTier

These will allow for communication betweeen the ElasticBeanstalk application, the EC2 instances it will create to host the application and the RDS database.

You can also create a User called `mod_site` which will allow the app to access other services. Attach the following policies:
- AmazonS3FullAccess
- AmazonSESFullAccess

## RDS

Go to the RDS console. Select `Databases` and then `Create new database`.
Choose standard create and MySQL (not the Aurora one unless you have a spare £800). Choose the free tier. Choose an appropriate identifier for the db and the same for the credentials.

The next thing to change is to attach it to the VPC you created. Choose one of the subnets it will live in. Do not allow public access.

If you already created relevant security groups, select one. Otherwise, create a new one and name it as you see fit, remember you will be creating one for staging and one for production.
The rest you can leave as default.

Allow password authentication.
Under `Additional Configurations` you should see `initial db name`, this should be `ebdb`. The rest can be left as default.

Create the db and wait for it to spin up.
Repeat to create your prod/staging version.

## ElasticBeanstalk

We'll be using ElasticBeanstalk (EB, sometimes EBS) to host our application as the process is a bit more streamlined than with just creating an EC2 instance since EB allows for more abstraction and less manual config.

Go to the EB console and choose `Applications` from the left side menu. Create a new Application with an appropriate name. Then create an environment:

Choose Web tier. I'd recommend customising the domain name for ease of access but you don't need to as you can purchase a custom domain. The platform should be Python. Everything else on that page can be left as default.

On the next page (service access), select `use an existing role` and select the IAM role you created. If you have an EC2 key, feel free to add it (you'll be able to ssh into the EC2 instance from your local machine) but it's not necessary. Select the same IAM role for the EC2 instance profile.

On the next page, select the VPC you created, check that public IP is enabled, and select the subnet you chose for the RDS instance. Don't fill out the database section.

On the next page, select the security group you created for the RDS instance.

On the next page, turn off (uncheck) managed updates (these so far have only caused issues when they run and fail) and scroll to the `Platform Software` section, it should ask you to define the `WSGI path`, it should be `museum_of_dreams_project.wsgi`.

Next, scroll to the bottom where it should have `Environment Variables` or `Environment Properties`. Some of these will vary between staging and production. Add some new ones:

- `DJANGO_SETTINGS_MODULE` (this is the path to your settings/aws.py file <project>.settings.aws)
- `RDS_HOSTNAME` (this is the endpoint for the RDS instance)
- `RDS_PORT` (this should be 3306 unless you changed it)
- `RDS_DB_NAME` (this should be ebdb)
- `RDS_USERNAME` (this should be the username you chose or admin if you didn't change it)
- `RDS_PASSWORD` (this should be the master password you set on the db)
- `PYTHONPATH` This is where the app is hosted on the ec2 instance: `/var/app/venv/staging-LQM1lest`


Above this section is a `Static Files` section. You should add `/static` as paths, with `static` as its respective directory.

If you plan to use S3 for your static files, please see [S3 for static files](s3ForStatic.md)

You can review and create the environment. This will take some time. Repeat for the staging/prod version.


## Security Groups

Go view your available security groups in the EC2 console. It will be in `Security Groups` under the `Networks & Security` tab in the left hand menu.

You should have at least one defined for your database and at least one for the EB environment you created. It may be helpful to rename the EB load balancer group to distinguish it from the main EB app one.

|Security group|Inbound rules|
|---|---|
|for database| allow MySQL TCP from the same sg|
|for eb app| allow ssh from anywhere (optional), allow http from the load balancer group (should be set automatically)|
|for eb load balancer| allow http and https from anywhere (should be set automatically)|
---


## CodePipeline

This step assumes you have code on GitHub for the web app. Go to the CodePipeline console and then `Pipelines`. Create a new pipeline. Choose V2 and create a new service role and name it. Everything else on this page can be left as default.

Choose GitHub v2 for the source, and then select the repo and branch. You may need to create a new connection and sign in to your GH account. Otherwise, select the connection to your GH account.

If the repo is under an organisation, try typing the name as `<org name>/<repo name>`. **If you don't have permissions, you should contact your administrator or relevant AWS advisor to set up a GitHub App to ensure it doesn't disrupt other connections.**

After this, move on to the deploy step (skip build) and choose deploy and select the EB environment you created.
This will automatically pull in changes to the branch you select and deploy them to the environment.

### _**NB**_

You should have separate pipelines for each version of the web app - one for staging and one for production. The current CodePipelines pull from `main` for production and `development` for staging.

## Logging into the Admin

Once you've set everything up, check you can access the website at the domain you set (or through the EB console: `Go to environment` button). If this seems to be in order, go to the EC2 console and find the associated instance for your EB environment. Click `connect` and you're free to connect through the browser (default method). Once you're in the shell, you'll need to navigate to the app and create a superuser so you can log in to the admin site.

```
cd /var/app
source venv/staging-LQM1lest/bin/activate
cd current
```

We have to expose the variables from the EB environment to the shell we're in

```
export $(/opt/elasticbeanstalk/bin/get-config --output YAML environment |  sed -r 's/: /=/' | xargs)
```

If this is the first time setting up this app, you may need to run the migrations (this should be handled automatically in future with the `db-migrate.sh` file in `.platform`)

```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

Follow the steps to create a superuser and then you should be able to log into the admin inerface
