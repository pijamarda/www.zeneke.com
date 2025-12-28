# Deploying automatically using Gitlab CI/CD and Azure MI

With this step by step guide we will learn how to deploy resources automatically in Azure using:

* [Azure Managed Identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
* [Opentofu](https://opentofu.org/)
* [Gitlab CI/CD pipelines](https://docs.gitlab.com/ci/pipelines/)

### Advantages:

* Using CI/CD pipelies we automate and de-centralice the automatic deployment of resources, you dont have to do anything from your local PC.
* With Opentofu with abstract the Infrastructure and define it by Code so we avoid repetition. Ifrastructure as Code (IaC) becomes infrastrucgure self-documented, can be saved in a repository for better tracking
* Managed Identities allow as for passwordless authentication, so there are no secres laying around, and only the allowed respositores -> Branches are allowed to do changes.

