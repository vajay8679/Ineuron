################################################################################################

Section - 1 - Introduction

1. Course Introduction

2. Course Structure


3. Course Resources Download


4. Course Slides Download

################################################################################################

Section - 2 - Azure Subscription (Optional)

5. Creating Azure Free Account


6. Azure Portal Overview

https://login.microsoftonline.com/

https://portal.azure.com/#home


################################################################################################

Section 3 - Azure Databricks Overview

7. Introduction to Azure Databricks

distributed computing engine - spark

databircks - developed by spark  to make easy 

microsoft azure - it give databricks as attached servie to useall three makes azure databricks

8. Creating Azure Databricks Service

https://www.databricks.com/product/azure-pricing

https://portal.azure.com/#create/Microsoft.Databricks

Resource group - databrickscourse-rg
Workspace name - databrickscourse-ws
Prcing tier - Premium

then create databricks

create and pin - 'Databricks Course Dashboard'


click on 'resource group' and then 'launch Workspace'
after clicking on 'launch workspace' ->

https://adb-2860423160921495.15.azuredatabricks.net/onboarding?o=2860423160921495


9. Databricks User Interface Overview

https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#joblist/pipelines
https://accounts.azuredatabricks.net/


10. Azure Databricks Architecture Overview



################################################################################################

Section 4 - Databricks Cluster

Databricks Workspace

Please create the workspace in the region UK South. If you have already created a workspace in another region, please delete that and create in the UK South Region.



Databricks Cluster


Please use the following configuration for the databricks cluster.

Cluster Type - Single Node

Node Type - Standard_D4a_v4

13. Azure Databricks Cluster Types
1- all purpose
2- job cluster


14. Azure Databricks Cluster Configuration

15. Creating Azure Databricks Cluster

cluster name - 'databricks-course-cluster'
single node,
14GB Memory, 4core cpu
1 driver 0 worker node


16. Azure Databricks Pricing

https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/linux/#pricing
https://azure.microsoft.com/en-gb/pricing/details/databricks/



17. Azure Cost Control

set budget alert on your subscription

go to 'cost management' then 'invoice' and then 'cost alert' and from 'budget' create alert

https://portal.azure.com/#view/Microsoft_Azure_CostManagement/Menu/~/budgets/openedBy/AzurePortal

18. Azure Databricks Cluster Pool

inside databricks -> compute -> pool -> create pool

https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#setting/clusters/instance-pools/create

we create cluster pool to speed up restarting or creating cluster 


19. Azure Databricks Cluster Policy - 5 default policy by azure databricks

Job Compute,Legacy Shared Compute,Personal Compute,Power User Compute,Shared Compute


create policy to restrict users to limited services of cluster

https://docs.microsoft.com/azure/databricks/administration-guide/clusters/policies#policy-def

fixed policy

https://learn.microsoft.com/en-us/azure/databricks/administration-guide/clusters/policy-definition#fixed

policy  set  - while creating cluster

Databricks runtime version


https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#setting/clusters/cluster-policies/view/0007D6D6CF532F6D

Learing-policy

{
  "spark_version": {
    "type": "fixed",
    "value": "auto:latest-lts",
    "hidden": true
  }
}


we can use json for policy from file 'Learning+Compute+Cluster+Policy.json'


we can use their default policy and edit our changes

Personal Policy 2



################################################################################################

Section - 5 : Databricks Notebooks


21. Azure Databricks Notebooks Introduction

create cluster first - 'Databricks-course-cluster'
then go to workspace -inside user - create folder- 'databricks-course' and then create notebook


22. Magic commands

https://www.markdownguide.org/cheat-sheet/#basic-synta

it allow single notebook with multiple languages    

commands

%md
# Databricks-introduction
## UI Introduction
### Magic Commands
- %python
- %sql
- %scala
- %md

%sql

%fs
ls

%sh
ps


23. Databricks Utilities

1. File System Utilities - %fs , dbutils.fs.ls('/')
2. Secrets Utilities
3. Widget Utilities
4. Notebook Workflow Utilities

databricks-course/Databricks-utility.ipynb


24. Project Solution Download - Databricks Notebooks

import file 'Formula1-Project-Solutions.dbc' in workspace

25. Project Solution Download - Python/SQL Files



################################################################################################

Section - 6 : Accessing Azure Data lake from databricsk

26. Accessing Azure Data Lake Overview

27. Creating Azure Data Lake Storage Gen2

create a storage account - ADLS Gen2 - 'formula1dlajay'
resource group - 'databrickscourse-rg'
click on herarchical adlsgen2


https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts


create container

1. raw
2. processed
3. presentation


28. Azure Storage Explorer Overview

install azure Storage Explorer desktop

https://azure.microsoft.com/en-us/products/storage/storage-explorer/

snap connect storage-explorer:password-manager-service :password-manager-service


29. Access Azure Data Lake using Access Keys

https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-abfs-driver


spark.conf.set("fs.azure.account.key.<storage-account>.dfs.core.windows.net","<access-key>" )

https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-abfs-driver


go to storage container -> Access keys -> copy key and paste below
connect with databricks

#authenticate our access key


steps 1. spark.conf.set("fs.azure.account.key.formula1dlajay.dfs.core.windows.net",
               "i49cKHszeU4Pn+qcQ6jji+RxNjxfmOiFcCw+GlgqCjz6prDowWCOJhLhQOD+ZGAe4j98RXzq0gXG+AStkaJ50A==")

steps 2. dbutils.fs.ls('abfss://demo@formula1dlajay.dfs.core.windows.net/')

30. Access Azure Data Lake using SAS Token

https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview

https://learn.microsoft.com/en-us/azure/databricks/connect/storage/azure-storage#access-azure-data-lake-storage-gen2-or-blob-storage-using-a-sas-token


to generate sas token 
1. go to contianer -> 3 dots and then select get , list and then generate token
2. go to 'STORAGE account' and then go to 'shared access signature' then allow all permission and then generate token and then copy and remove '?'

1. sas token - 'sp=rl&st=2024-01-22T17:58:14Z&se=2024-01-23T01:58:14Z&spr=https&sv=2022-11-02&sr=c&sig=btCROaonpTlk4dbdZtSiyjhUS3f0lj7ow2UdYnQLqfo%3D'

2. sas toekn -> '?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-01-23T01:45:33Z&st=2024-01-22T17:45:33Z&spr=https&sig=V1Y0f06lr8%2BiDaHBu%2FV8yrUZBevCB9GamJj5aYBJCZU%3D'


#authenticate from sas token
spark.conf.set("fs.azure.account.auth.type.formula1dlajay.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dlajay.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dlajay.dfs.core.windows.net", "sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-01-23T01:45:33Z&st=2024-01-22T17:45:33Z&spr=https&sig=V1Y0f06lr8%2BiDaHBu%2FV8yrUZBevCB9GamJj5aYBJCZU%3D")


#this  
spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.<storage-account>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.<storage-account>.dfs.core.windows.net", <sas-token-key>)

#use this
spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.<storage-account>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.<storage-account>.dfs.core.windows.net", dbutils.secrets.get(scope="<scope>", key="<sas-token-key>"))



31. Access Azure Data Lake using Service Principal

https://learn.microsoft.com/en-us/azure/databricks/connect/storage/azure-storage#--access-azure-data-lake-storage-gen2-or-blob-storage-using-oauth-20-with-an-azure-service-principal

https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python


Go to azure active directory - app registration - New Registration
application name - 'formula1-app'
we need this 'client_id' and 'tenant_id' from here
Application (client) ID: 28ecc4a8-1683-472b-b989-e1b58a010be7
Directory (tenant) ID: f4bcbf87-8f54-476e-9ded-e78763f85179


azure active directory -> Certificates & secrets ->New client secret

secret name - 'Formula1 App'
secret_value = '.tM8Q~EBHpwkEkSVPNcoeFltavnx7LCcFEXYdb27'

#authenticate using service principal
spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.<storage-account>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.<storage-account>.dfs.core.windows.net", "<application-id>")
spark.conf.set("fs.azure.account.oauth2.client.secret.<storage-account>.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.<storage-account>.dfs.core.windows.net", "https://login.microsoftonline.com/<directory-id>/oauth2/token")


################################################################################################
client_id = "28ecc4a8-1683-472b-b989-e1b58a010be7"
tenant_id = "f4bcbf87-8f54-476e-9ded-e78763f85179"
client_secret = ".tM8Q~EBHpwkEkSVPNcoeFltavnx7LCcFEXYdb27"

#authenticate using service principal
spark.conf.set("fs.azure.account.auth.type.formula1dlajay.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.formula1dlajay.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.formula1dlajay.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.formula1dlajay.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.formula1dlajay.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

################################################################################################

for IAM role - > go to storage account and then add role 'Storage Blob Data Contributor' and then add member 'Formula 1' from azure active directory


32. Cluster Scoped Authentication

for this we will edit our cluster and go to 'advanced option' -> Spark config -> add details

paste below code and restart cluster

fs.azure.account.key.formula1dlajay.dfs.core.windows.net i49cKHszeU4Pn+qcQ6jji+RxNjxfmOiFcCw+GlgqCjz6prDowWCOJhLhQOD+ZGAe4j98RXzq0gXG+AStkaJ50A==



33. Access Azure Data Lake using Credential Passthrough


for this we will edit our cluster and go to 'advanced option' -> Spark config -> Enable credential passthrough for user-level data access 


and then we have to go storage account and then 'access control (IAM)

select role - 'Storage Blob Data Contributor' 

and after running notebook remove 'Enable credential passthrough for user-level data access ' from cluster



34. Recommended Approach for Course Project

using service principal is best

databricks mounts allows only in service principal so recommended approach

################################################################################################

Section 7 - Securing Access to Azure Data Lake

35. Securing Secrets Overview

  1. Databricks Secret Scope
  2. Azure Key Vault




36. Creating Azure Key Vault

go to create resource then search 'key vault'and click and then create

https://portal.azure.com/#view/Microsoft_Azure_Marketplace/MarketplaceOffersBlade/selectedMenuItemId/home/searchQuery/key%20vault/searchInitiatedFrom/plusNewBladeSearchContext/suggestionCorrelationGuid/f3f46dd6-66a3-495c-900f-ef4562521002/suggestionResponseRequestId/b84e639a-6ef3-46d9-8c20-27b25c1c4de8

 Key vault name - formula1-key-vault-ajay

 soft delete - enabled
 Permission model - Vault access policy


then go to 'resource'

and then go to 'Secrets' in sidebar

and then create 

Name - formula1dl-account-key
value - i49cKHszeU4Pn+qcQ6jji+RxNjxfmOiFcCw+GlgqCjz6prDowWCOJhLhQOD+ZGAe4j98RXzq0gXG+AStkaJ50A==




37. Creating Secret Scope

go to databricks and click on azure icon and then url like this

https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#secrets/createScope

and give name - 'formula1-scope'

and from key-vault go to properties section and copy and paste in scope ->

Vault URI - https://formula1-key-vault-ajay.vault.azure.net/
Resource ID - /subscriptions/49a84c57-21dd-4dde-a744-8c4a8075b500/resourceGroups/databrickscourse-rg/providers/Microsoft.KeyVault/vaults/formula1-key-vault-ajay



38. Databricks Secrets Utility

5.explore_dbutils_secrets_utility.ipynb

dbutils.secrets

dbutils.secrets.help()
dbutils.secrets.listScopes()
dbutils.secrets.list(scope = 'formula1-scope')
dbutils.secrets.get(scope = 'formula1-scope', key = 'formula1dl-account-key')

39. Using Secrets to Access Azure Data Lake using notebooks


formula1dl_account_key = dbutils.secrets.get(scope = 'formula1-scope' , key = 'formula1dl-account-key')

spark.conf.set("fs.azure.account.key.formula1dlajay.dfs.core.windows.net", formula1dl_account_key)

dbutils.fs.ls('abfss://demo@formula1dlajay.dfs.core.windows.net/')


40. Using Secrets to Access Azure Data Lake using notebooks (Assignment)

https://portal.azure.com/#view/Microsoft_Azure_KeyVault/CreateSecretBlade/secret~/null/vaultId/%2Fsubscriptions%2F49a84c57-21dd-4dde-a744-8c4a8075b500%2FresourceGroups%2Fdatabrickscourse-rg%2Fproviders%2FMicrosoft.KeyVault%2Fvaults%2Fformula1-key-vault-ajay

create secret for sas token
copy sas token from container demo from storage account and then paste in place of value

name - formula1dl-demo-sas-token

same we did for service principal

formula1-account-client-secret - client_secret
formula1-account-tenant-id - tenant_id
formula1-account-client-id - client_id



41. Using Secrets Utility in Clusters


go to cluster and edit and advacned option and then paste below line and after complete remove it and restart cluster

fs.azure.account.key.formula1dlajay.dfs.core.windows.net {{secrets/formula1-scope/formula1dl-account-key}}

                                                                   {{secrets/scope/access-key}} 



################################################################################################

section -8 -Mounting Data lake Container to Databricks


43. Databricks File System (DBFS)

setup-using-secret-scope/6.explore_dbfs_root.ipynb

go to admin setting -> Advanced ->Other ->dbfs browser enabled

dbutils.fs.ls('/')
display(dbutils.fs.ls('dbfs:/FileStore/'))
display(spark.read.csv('dbfs:/FileStore/circuits.csv'))
display(spark.read.csv('/FileStore/circuits.csv'))


44. Databricks Mount overview

https://learn.microsoft.com/en-us/azure/databricks/dbfs/mounts

dbfs -> /mnt/stroage1

using 'service principal' from 'azure active directory'

45. Mounting Azure Data Lake Storage Gen2

setup-using-secret-scope/7.mount_adls_using_service_principal.ipynb

Mount Azure Data Lake using Service Principal

https://learn.microsoft.com/en-us/azure/databricks/dbfs/mounts


client_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-id")
tenant_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-tenant-id") 
client_secret = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-secret") 

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

dbutils.fs.mount(
  source = "abfss://demo@formula1dlajay.dfs.core.windows.net/",
  mount_point = "/mnt/formula1dlajay/demo", #we ca give name whatever we want
  extra_configs = configs)

display(dbutils.fs.ls('/mnt/formula1dlajay/demo'))

spark.read.csv("/mnt/formula1dlajay/demo")

display(spark.read.csv("/mnt/formula1dlajay/demo"))

display(dbutils.fs.mounts())

dbutils.fs.unmount('/mnt/formula1dlajay/demo')


46. Mounting Azure Data Lake Storage Gen2 (Assignment)

setup-using-secret-scope/8.mount_adls_container_for_project.ipynb

def mount_adls(storage_account_name,container_name):
    #get secrets from key-vault
    client_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-id")
    tenant_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-tenant-id") 
    client_secret = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-secret") 

    #set spark configurations
    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
    
    #unmount the storage account container
    if any(mount.mountPoint == f"/mnt/{storage_account_name}/{container_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_account_name}/{container_name}")
    
    #Mount the storage account container
    dbutils.fs.mount(
        source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = f"/mnt/{storage_account_name}/{container_name}", #we ca give name whatever we want
        extra_configs = configs)
    display(dbutils.fs.mounts())


mount_adls('formula1dlajay','raw')
mount_adls('formula1dlajay','processed')
mount_adls('formula1dlajay','presentation')

display(dbutils.fs.ls("/mnt/formula1dlajay/demo"))


################################################################################################


