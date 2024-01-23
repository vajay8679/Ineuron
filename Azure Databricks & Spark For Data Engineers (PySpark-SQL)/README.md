5. Creating Azure Free Account
6. Azure Portal Overview

################################################
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
after clicking on 'launch workspace' -> https://adb-2860423160921495.15.azuredatabricks.net/onboarding?o=2860423160921495


9. Databricks User Interface Overview
https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#joblist/pipelines
https://accounts.azuredatabricks.net/


10. Azure Databricks Architecture Overview



################################################
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



################################################
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


24. Project Solution Download - Databricks Notebooks

import file 'Formula1-Project-Solutions.dbc' in workspace

25. Project Solution Download - Python/SQL Files



################################################
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


################################
client_id = "28ecc4a8-1683-472b-b989-e1b58a010be7"
tenant_id = "f4bcbf87-8f54-476e-9ded-e78763f85179"
client_secret = ".tM8Q~EBHpwkEkSVPNcoeFltavnx7LCcFEXYdb27"

#authenticate using service principal
spark.conf.set("fs.azure.account.auth.type.formula1dlajay.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.formula1dlajay.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.formula1dlajay.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.formula1dlajay.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.formula1dlajay.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")
###################################

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



######################################
Section 7 - Securing Access to Azure Data Lake

35. Securing Secrets Overview

  1. Databricks Secret Scope
  2. Azure Key Vault




36. Creating Azure Key Vault
