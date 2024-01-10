#Olympic Data Analytics | Azure End-To-End Data Engineering Project



1. create 'storage account' in Azure - https://portal.azure.com/#create/Microsoft.StorageAccount-ARM

 resource group - tokyo-olympic

Storage account name - tokyoolympicdataajay
Enable hierarchical namespace -  enable
create contianer - tokyo-olympic-data
inside container create directory - 1. raw-data , 2. transformed-data

2. create 'azure data factories' - https://portal.azure.com/#create/Microsoft.DataFactory
 
 https://portal.azure.com/#@vajay8679gmail.onmicrosoft.com/resource/subscriptions/49a84c57-21dd-4dde-a744-8c4a8075b500/resourceGroups/tokyo-olympic/providers/Microsoft.DataFactory/factories/tokyo-olympic-ajay-df/overview

 
use same  resource group - tokyo-olympic
name - tokyo-olympic-ajay-df
go to resource group  and launch data factory

go to author -> + icon - pipeline create datapipeline - data-ingestion

link our source to data factory 

source - HTTP
Sink - Azure Data lake storage Gen 2
inside sink -> linked service keep same for all files 

validate and debug and check in storage

3. create databricks

https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Databricks%2Fworkspaces

resource group - tokyo-olympic
resource name - tokyo-olympic-db
tier - premium

click on resource then launch workspace

inside databricks - 
https://adb-2990832392178635.15.azuredatabricks.net/?o=2990832392178635#create/cluster


create compute cluster and create notebook


4.  go to 'app registration' in azure portal
https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/Overview/appId/82b3802a-6150-4858-b6d8-cf63359dae41/objectId/92d2363c-bb1c-4b3f-a8d3-63c9ab92bc32/isMSAApp~/false/defaultBlade/Overview/appSignInAudience/AzureADMyOrg/servicePrincipalCreated~/true

you will get some credentials to connect between azure databrciks and ADLS

app name  - app01

we need client id and tenant id from here


Application (client) ID : 82b3802a-6150-4858-b6d8-cf63359dae41
Directory (tenant) ID : f4bcbf87-8f54-476e-9ded-e78763f85179


go to certificates & secreats in here app regisration page and then create 'new client secreats'

name  - secreatkey

copy secreatkey
secreatkey - isq8Q~CWL5-Cgwdl2U3p0m-doKgY3XchVRJurcb9

4. key vault
we can put secreat id in key vault

#########################################
dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicdataajay.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/tokyoolymic",
extra_configs = configs)
##########################################

5. Access control (IAM)
https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/accesscontrol/storageAccountId/%2Fsubscriptions%2F49a84c57-21dd-4dde-a744-8c4a8075b500%2FresourceGroups%2Ftokyo-olympic%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Ftokyoolympicdataajay/path/tokyo-olympic-data/etag/%220x8DC0D3BE46511DE%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None


click on - add role assignment

'Storage Blob Data Contributor'

select member - use 'app01' that we have created in app registration

%fs
ls "/mnt/tokyoolymic"



6. for transformation follow spark documentation

https://spark.apache.org/docs/latest/rdd-programming-guide.html


read the data from raw-data folder and then perform transformation and then write the data ti transfored data folder


7.  azure synapse anaytics

https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Synapse%2Fworkspaces

resource group - tokyo-olympic
workspace name -   tokyo-olympics-ajay
account name - tokyoolympicdataajay
file system name - tokyo-olympic-data

then go to resource group

then click on 'tokyo-olympics-ajay'
then 'Open Synapse Studio'

data -> + then -> lake database

datbase name - TokyoOlympicDB
table select from data lake

table name - athletes


after creating table refresh and run query

select * from athletes;


run queries

--count the number of athelete from each country
select Country, count(*) as Total_athelete from athletes
GROUP BY Country ORDER BY Total_athelete DESC;

--calculate the total medal won by each country
select Team_Country,SUM(Gold) as Total_Gold,SUM(Silver) as Total_silver,
SUM(Bronze) as Total_silver from medals GROUP by Team_Country ORDER BY Total_Gold DESC;

--calculate the average number of enteries by gender for each disipline:
SELECT Discipline,  AVG(Female) as avg_Female,AVG(Male) as avg_Male
from entriesgender where Discipline= 'Archery' GROUP by Discipline;


connect sysnaps with dashboarding tool for dashboarding


delete resource group




 you will analyze Olympic data using various tools and technologies, including Azure Data Factory, Data Lake Gen 2, Synapse Analytics, and Azure Databricks.