# Quickstart with CDK

## Note

For the Museum of Dreamworlds Project, the cdk directory would be `/infrastructure`. In other cases, it will usually be where app.py is located in your cdk project.

## Installing requirements

Once you've completed the steps in
[First time setup](./first-time-setup.md), you can start using the Cloud Development Kit in Museum of Dreamworlds by running the following:

```bash
$ cd infrastructure # ensures that you are working from the cdk project directory

# installing the python cdk libraries
$ pip install -r requirement.txt
$ pip install -r requirement-dev.txt
```

The `cdk` command should be now callable in your terminal given you are in the correct working directory.

## Deploying stacks

### 1. VPC and Database Stacks

These two stacks should be deployed in the following order:

```bash
cdk deploy VPCStack --profile mod # mod is replaced by your profile name you've set for the AWS account
cdk deploy StagingDbStack --profile mod
```

### 2. Elastic Beanstalk Stack

This should be deployed after VPC and StagingDbStack:

```bash
cdk deploy StagingStack --profile mod
```

#### REQUIRED CONFIGURATIONS BEFORE DEPLOYING WITH CODEPIPELINE - Environment Variables

After the this stack is created successfully, in your AWS console, go to:

```
Elastic Beanstalk > Environments > Your CDK Environmnet > configurations > Updates, monitoring, and logging
```

You will need to configure certain environment variables for this instance via the console manually:

- `RDS_USERNAME` : this is generated when you deploy the StagingDbStack, you can find this value in AWS Secret Manager
- `RDS_PASSWORD` : same as `RDS_USERNAME`, you can find this value in AWS Screct Manager
- `AWS_ACCESS_KEY_ID`: used to establish boto3 session for s3 buckets, copy and paste this value from the `env-dev` environment
- `AWS_SECRET_ACCESS_KEY`: same as `AWS_ACCESS_KEY_ID`,copy and paste this value from the `env-dev` environment
- `SECRET_KEY`: Django's session key, copy and paste this value from the `env-dev` environment

#### REQUIRED CONFIGURATIONS BEFORE DEPLOYING WITH CODEPIPELINE - IAM policy

Again, in your AWS console, go to:

```
IAM > Users > mod_site
```

and edit `get_put_object` policy to include your s3 bucket arn:

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

Once these are configured, you can proceed to deploy the application with Codepipeline

### 3. CodePipeline Stack

```
cdk deploy StagingPipelineStack --profile mod
```
