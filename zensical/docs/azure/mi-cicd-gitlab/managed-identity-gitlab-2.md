# Bootstrap

The first step is the bootstraping, this means that at least the first of the steps must be done from a local computer, and from someone with enough access/permissions.

## Creation of Managed Identities:

We will create 2 Managed Identities (MIs)

* Read Only MI (can only read, usefull for the plan stages)
* Contributor MI (will actually do the changes and deploy resources)

### Pre-Requisites

#### Opentofu (or Terraform)

```shell
tofu --version
```
should get you something similar to
```shell
OpenTofu v1.10.7
on linux_amd64
```
#### Az cli

```shell
az --version
```
should get you something similar to
```shell
azure-cli 2.79.0 *
core      2.79.0 *
```

## Create 2 Managed Identities

We are going to use as a base-point the following [Gitlab Repository](https://gitlab.com/zeneke-tech/azure/automated-cicd-deployment/bootstrap)

There are 3 fundamental files that we must create/change/modify:

* Create a .env file with the following data:

```shell
export GITLAB_ACCESS_TOKEN="verysecretgitlabtoken"
export TF_STATE_NAME="config/backend-develop.conf"
export TF_VARIABLES_NAME="config/variables-develop.tfvars"
export GITLAB_USER_NAME="yourgitlabusername"
```

* File "config/backend-develop.conf"

    Here you musts configure your own project id number  
    You can check it here: Repository -> Settings

* File "config/variables-develop.conf", change into your proper values:

    * tenant_id <- Azure Tenant id
    * location <- Location for resources (default West Europee)
    * subscription_id <- Your own Sunbscription Id
    * issuer <- you can keep this one
    * subject <- The target repository where your Managed identities should do the changes
    * project_id  <- The targer repository id, this is important because it is where the Gitlab Variables will be automatically created.

### Azure Login

Now login into azure with a user with User Access Administrator and Contributor access to the Subscription

```bash
az login
az account set --subscription "yoursubscriptionid"
```

### Terraform plan

Now lets load the .env file with the correct data to the environment variables, dont forget to include all relevant data
```bash
source .env
```
You can use now the .sh scripts provided

```bash
./tofuinit.sh
```

```bash
./tofuplan.sh
```

```bash
./tofuapply.sh
```