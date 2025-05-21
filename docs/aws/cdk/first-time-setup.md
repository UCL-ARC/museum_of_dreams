# Setting up the AWS Cloud Development Kit

## Prerequisites

Before starting, you will need to have the following installed:

- [Node.js](https://nodejs.org/en/download)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)

Once these are in place, you can start working by:

```bash
$ cd infrastructure # ensures that you are working from the cdk project directory

# installing the python cdk libraries
$ pip install -r requirement.txt
$ pip install -r requirement-dev.txt
```

The `cdk` command should be now callable in your terminal given you are in the correct working directory.

## Note

For the Museum of Dreamworlds Project, the cdk directory would be `/infrastructure`. In other cases, it will usually be where app.py is located in your cdk project.

## Setting up profile (wip)

```bash
$ aws configure sso
```
