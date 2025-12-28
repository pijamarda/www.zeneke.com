# Deployment

With the Managed Identities already deployed and with the correct access of the repositories to them using Federated Access its time to actually deploy the resources.

The final version of the example can be checked here:

[Example Infrastructure](https://gitlab.com/zeneke-tech/azure/automated-cicd-deployment/infrastructure)

## CI/CD Pipeline:

One of the most importan part of the automatic deployment is the [configuration of the pipeline](https://gitlab.com/zeneke-tech/azure/automated-cicd-deployment/infrastructure/-/blob/main/.gitlab-ci.yml?ref_type=heads)

The pipeline itself expects the following Variables already configured automatically in the Bootstrap:

* AZURE_TENANT_ID <- Your Azure tenant
* AZURE_RO_CLIENT_ID <- The ClientID of your Read-Only Managed Identity (used for the plan)
* AZURE_CLIENT_ID <- The ClientID of the Managed Identity that will deploy the resources
* AZURE_SUBSCRIPTION_ID <- The subscriptionid where the resources will be deployed

The other fundamental configuration is the TFVARS and CONFIG files for Terraform on the [Config folder](https://gitlab.com/zeneke-tech/azure/automated-cicd-deployment/infrastructure/-/tree/main/config?ref_type=heads)

Here you should add your own values

After that the PIPELINE should create a simple Resource Group, but you can add aditional resources to test it.