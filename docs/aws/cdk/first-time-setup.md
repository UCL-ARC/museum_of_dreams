# Setting up the AWS Cloud Development Kit

## Prerequisites

Before starting, you will need to have the following installed:

- [Node.js](https://nodejs.org/en/download)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)

Optional, but highly recommended:

- Installing the AWS Toolkit extension (if using VSCode)

### Using SSO connections & profiles

While it is fine to run `aws configure` to set up a local CDK profile with access keys, for federated users, the recommended way is to set up an SSO connection instead:

```bash
$ aws configure sso
```

You will be prompted the following:

```bash
SSO session name (Recommended): # give a name for this connection
SSO start URL [None]: # provide your AWS access portal link
SSO region [None]: # provide your account region
SSO registration scopes [sso:account:access]: # customises the scope of this session, use the default value "sso:account:access" for this unless instructed otherwise
```

### Example configuration for UCL accounts:

```bash
SSO session name (Recommended): UCL
SSO start URL [None]: https://ucl-cloud.awsapps.com/start
SSO region [None]: eu-west-2
SSO registration scopes [sso:account:access]: sso:account:access
```

This will open you browser to login/authorise access to Application and AWS account. After doing so, in your terminal, you can select the profile you will be using for CDK deploymnets.

### IMPORTANT NOTE(s):

- In order to successfully deploy a CloudFormation Stack, make sure your AWS account have enough permissions - this can be checked from your AWS account access portal.

## Next steps

[Getting started with AWS CDK](./cdk-quick-start.md)
