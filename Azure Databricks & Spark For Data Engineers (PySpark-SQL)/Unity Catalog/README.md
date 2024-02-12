#######################################################################################################

 Section - 25 - Unity Catalog - Introduction


163. Section Overview

164. Unity Catalog Sections Resource Download


download files


165. Unity Catalog Overview


Unity Catalog is a databricks offered unified solution for implementing data governance in the data lakehouse

data governance - process of availability , usabaility , integrity,and secuirty of the data present in an enterprise

1. controll access of the data for the user
2. ensure data is trustworthy and not misused
3. help imporve privacy regulations such as gdpr, ccpa


with unity catalog - one metastore per region - it improve performance

Unity catalog offers
1. metastore
2. Access controll
3. User management
4. Data Explore
5. Data Lineage (Upstream and downstream flow of data and pipeline)
6. Audit Logs


Unitity catalog is a databricks offered unified solution

Unitity catalog 
->

Data Lineage
Data discoveability
Data Access Control 
Data Audit



166. Unity Catalog Set-up Overview

unity catalog set-up

1. create Azure databircks workspace
2. create azure datalake gen2
3. Create access conncetor
4. Add role storage blob Data contributor
5. create unity catalog metastore
6. Enable databircks workspace for unity catalog



167. Create Unity Catalog Metastore - Prerequisites

step1 - create new azure databricks workspace

https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryItemDetailsBladeNopdl/id/Microsoft.Databricks/selectionMode~/false/resourceGroupId//resourceGroupLocation//dontDiscardJourney~/false/selectedMenuId/home/launchingContext~/%7B%22galleryItemId%22%3A%22Microsoft.Databricks%22%2C%22source%22%3A%5B%22GalleryFeaturedMenuItemPart%22%2C%22VirtualizedTileDetails%22%5D%2C%22menuItemId%22%3A%22home%22%2C%22subMenuItemId%22%3A%22Search%20results%22%2C%22telemetryId%22%3A%226e2b9f32-2d22-4653-89c6-bc930acaa5d5%22%7D/searchTelemetryId/0b25b21e-7132-48a3-b89a-c3bc1a99ae1f


resource group - databricscourse-uc-rg 
workspace name - databrickscourse-uc-ws

premium tier

then create


step2 - create storage account

https://portal.azure.com/#create/Microsoft.StorageAccount-ARM


resource group - databricscourse-uc-rg
name - databrickscoursedlajay
performance - standard
Redundancy - locally storage Redundancy
herarchichal namespace - enabled - to get adls gen2 otherwise you will get blob storage

and then create


step 3 - create Access Connector for Azure Databricks

https://portal.azure.com/#create/Microsoft.AccessConnector

resource group - databricscourse-uc-rg
name - databrickscourse-uc-access


Step - 4 - IAM role

go inside storage -databrickscoursedlajay

https://portal.azure.com/#@vajay8679gmail.onmicrosoft.com/resource/subscriptions/49a84c57-21dd-4dde-a744-8c4a8075b500/resourceGroups/databrickscourse-uc-rg/providers/Microsoft.Storage/storageAccounts/databrickscoursedlajay/overview

inside IAM role - Add role assignment
role - Storage Blob Data Contributor
Assign access to - Managed identity
member - new member - 
select - databrickscourse-uc-access

and then create

how we will connect our access connector with adls gen2 with role asssigned role  Storage Blob Data Contributor



168. Create Unity Catalog Metastore

go to manage account o top left in databricks 

https://accounts.azuredatabricks.net/

go inside data -> create metastore ->

https://accounts.azuredatabricks.net/data


name - databrickscourse_uc_metastore
region - central india

inside azure storage (databrickscoursedlajay) we have to create container

container name - metastore

ADLS Gen2 - metastore@databrickscoursedlajay.dfs.core.windows.net/


inside properties section of -Access Connector 
Access Connector Id - /subscriptions/49a84c57-21dd-4dde-a744-8c4a8075b500/resourceGroups/databrickscourse-uc-rg/providers/Microsoft.Databricks/accessConnectors/databrickscourse-uc-access


create and select workspace - databrickscourse-uc-ws

thats how we will connect metastore to our workspace


169. Cluster Configurations for Unity Catalog

select workspace from top left - 'databrickscourse-uc-ws'

we have to create cluster and select configuration that supports unity catalog


we have to look 'Access mode' - Single user or Shared only 
Databricks runtime version - only choose that enable unity catalog

for which unity catalog should enabled


170. Unity Catalog Object Model Overview


  1. metastore - top level container, only one metastore per region, paired with default adls storage
  2. catalog - newly added to untiy catalog, logical container within metastore
  3. Schema(Database)(one or more) - Next level container within catalog, schema and database are same, use schema instead of database
  4. view/table/function (one or more) - 
  5. table -> external (only meta store in databricks , data in cloud)/managed (metadata and data both inside databricks)

  benefits of unity catalog for managed table

  managed table can only be delta format
  stored in the default storage 
  deleted data retained for 30 days
  Benefits from automatic maintenance and performance improvements


  query -> select * from catalog.schema.table;

  storage credentials, external location , catalog, share , recipient, provider


metastore(formula1)
created 3 catalog(catalog - dev/test/prod) 
3 schema for each catalog (schema - bronze/silver/gold) 
for each schema (tables/view/functions)
   
formula1_sandbox -> Schema -> tables


171. Unity Catalog Object Model Demo (Data Explorer UI)

we have four catalog in catalog section of databricks


catalog name - demo_catalog
schema name - demo_schema

and then create table and upload table file - then check inside storage container inside metastore GUI file name created then table file and delta file



172. Unity Catalog Object Model Demo (SQL/ Python)


create workspace folder -databricks-course -> unity-catalog 

file- 1.query_table_using_unity_catalog

# query

select * from demo_catalog.demo_schema.circuits;

use catalog demo_catalog;
use schema demo_schema;
select * from circuits;

select current_schema()

show schemas;

show tables;

%python
display(spark.sql('show tables'));

%python
df = spark.table("demo_catalog.demo_schema.circuits")

%python display(df)



173. Accessing External Data Lake Overview

inside metastore 

1. storage credentials - credential object store in metastore , used on users behalf to access cloud storage, created using managed identity/service principle, can be assigned access control polices
2. External Location - object stored in centrally at the metastore, combines the adls path with the storage credential, subjected to access control policies

# accessing external location

1. create access connector
2. create azure datalake storage
3. Assign Storage Blob Data contributor role 
4. create storage credential
5. create external location


174. Create Storage Credential

step 1. create access connector
name  - databrickscourse-uc-ext-access

step 2. create azure datalake storage
storage name - databrickscourseextdlaj
performance - standard
Redundancy - locally
herarchical - enabled
create container - demo 
insert - circuits.csv file

step 3. Assign Storage Blob Data contributor role 
create IAM ROLE - Storage Blob Data Contributor
Assign access to - MANAGED identity
select member  - databrickscourse-uc-ext-access

step 4. create storage credential

go to databricks - catalog - external data - create Storage Credentials

name - databrickscourse-ext-storage-credentials
access connector id - /subscriptions/49a84c57-21dd-4dde-a744-8c4a8075b500/resourceGroups/databrickscourse-uc-rg/providers/Microsoft.Databricks/accessConnectors/databrickscourse-uc-ext-access


175. Create External Location

go to databricks - catalog -external location

step 5. create external location
External location name - databrickscourseextdl_demo
 Storage credential - databrickscourse-ext-storage-credentials
path - abfss://demo@databrickscourseextdlaj.dfs.core.windows.net/

test connection


create file inside unity_catalog folder - 2.access_external_location

to check external storage 

dbutils.fs.ls('abfss://demo@databrickscourseextdlaj.dfs.core.windows.net/')

o/p - [FileInfo(path='abfss://demo@databrickscourseextdlaj.dfs.core.windows.net/circuits.csv', name='circuits.csv', size=10044, modificationTime=1707496767000)]


#######################################################################################################

Section - 26 Unity Catalog - Mini project


176. Project Overview
                 
                this will come under workflow
-------------------------------------------------------------
Notebook -> Bronze -> Notebook -> Silver -> Notebook -> Gold -> Power BI Report


drivers & results file

Steps to follow

1. create storage container
2. create external location
3. create catalog and schema
4. create bronze table(External)
5. create silver table(Managed)
6. create Glod table(Managed)
7. create databricks workflow


177. Create External Location

https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/#--create-an-external-location

https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/external-locations

step1 - create storage container insidestorage account(databrickscourseextdlaj) - bronze,silver,gold 

file - 1.create_external_locations
inside bronze - drivers.json, results.json
create folder unity-catalog-mini-project
step2 - create external location


file inside ->unity_catalog_mini_project/1.create_external_locations

Create the external locations required for this Project
Bronze
Silver
Gold

CREATE EXTERNAL LOCATION databrickscourseextdl_bronze
URL 'abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databrickscourse-ext-storage-credentials`);


DESC EXTERNAL LOCATION databrickscourseextdl_bronze

%fs
ls "abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/"

CREATE EXTERNAL LOCATION databrickscourseextdl_silver
URL 'abfss://silver@databrickscourseextdlaj.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databrickscourse-ext-storage-credentials`);

CREATE EXTERNAL LOCATION databrickscourseextdl_gold
URL 'abfss://gold@databrickscourseextdlaj.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databrickscourse-ext-storage-credentials`);


after running all go to external location and test connection in catalog for all 3 catalog


178. Create Catalogs and Schema

external table view

file - 2.create_catalog_schemas

metastore - managed-location(mandatory) - 3. (Default Storage ADLS GEN2 CONTIANER)
catalog (formula1_dev) -  managed-location(optional) - 2. (ADLS GEN2 CONTIANER)
schema(database) (bronze/silver/gold) -managed-location(optional) - 1. (ADLS GEN2 CONTIANER)
table
external 

for this we have specify path

for managed table managed_table -  
metastore - managed-location(mandatory) - 3. (Default Storage ADLS GEN2 CONTIANER)
catalog (formula1_dev)-  managed-location(optional) - 2. (ADLS GEN2 CONTIANER)
schema(database) (bronze/silver/gold)  -managed-location(optional) - 1. (ADLS GEN2 CONTIANER)
table
managed 


we dont have to specify path and retainsion 30days after it table and data will be deleted


schema-of-project

bronze(external- drivers/results) - silver(managed - drivers/results) - gold(managed - drivers_wins)


Create Catalog and Schema required for this project
Catalog - formula1_dev (without managed location)
Schema - bronze,silver,gold (with managed location)

create catalog if not exists formula1_dev;

use catalog formula1_dev;

create schema if not exists bronze
managed location "abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/"

create schema if not exists silver
managed location "abfss://silver@databrickscourseextdlaj.dfs.core.windows.net/"

create schema if not exists gold
managed location "abfss://gold@databrickscourseextdlaj.dfs.core.windows.net/"

show schemas;


179. Create External Tables

file - 3.create_bronze_table

Create Bronze tables
drivers.json
results.json Bronze folder path - abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/

drop table if exists formula1_dev.bronze.drivers;

create table if not exists  formula1_dev.bronze.drivers
(
  driverId INT, 
  driverRef STRING, 
  number INT, 
  code STRING, 
  name STRUCT<forename:STRING, surname:STRING>,
  dob DATE,
  nationality STRING,
  url STRING
)
using json
options (path "abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/drivers.json");


drop table if exists formula1_dev.bronze.results;

create table if not exists  formula1_dev.bronze.results
(
resultId INT,
raceId INT,
driverId INT,
constructorId INT,
number INT,grid INT,
position INT,
positionText STRING,
positionOrder INT,
points INT,
laps INT,
time STRING,
milliseconds INT,
fastestLap INT,
rank INT,
fastestLapTime STRING,
fastestLapSpeed FLOAT,
statusId STRING
)
using json
options (path "abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/results.json");



180. Create Managed Tables

Create Managed table in the schema (by default file will be delta format) - file - 4.create_silver_tables
drviers
results

drop table if exists formula1_dev.silver.drivers;

create table if not exists formula1_dev.silver.drivers
as 
select driverId as driver_id,
       driverRef as driver_ref,
       number,
       code,
       concat(name.forename," ",name.surname) as name,
       dob,
       nationality,
       current_timestamp() as ingetion_date
from formula1_dev.bronze.drivers;


drop table if exists formula1_dev.silver.results;

create table if not exists formula1_dev.silver.results
as 
select 
resultId as result_id,
raceId as race_id,
driverId as driver_id,
constructorId as constructor_id,
number,
grid,
position,
positionText as position_text,
positionOrder as position_order,
points,
laps,
time,
milliseconds,
fastestLap fastest_lap,
rank,
fastestLapTime as fastest_lap_time,
fastestLapSpeed as fastest_lap_speed,
statusId as status_id,
current_timestamp() as ingetion_date
from formula1_dev.bronze.results;



Create Managed table in the Gold table
Joins Drivers and results to identify the number of wins per drivers -  file - 5.create_gold_table


drop table if exists formula1_dev.gold.driver_wins;

create table formula1_dev.gold.driver_wins
as 
select d.name, count(1) as number_of_wins
from formula1_dev.silver.drivers  d
join formula1_dev.silver.results  r
on (d.driver_id = r.driver_id)
where r.position = 1
group by d.name;   


select * from formula1_dev.gold.driver_wins
order by number_of_wins desc;


181. Create Databricks Workflow

name -wf_process_f1_data

go inside databricks and inside workflow create a job and connect all 3 layers file

3.create_bronze_table -> 4.create_silver_tables -> 5.create_gold_table

task name - Create_bronze_table
path - /unity-catalog-mini-project/3.create_bronze_table
cluster -choose your cluster

task name - Create_silver_table
path - /unity-catalog-mini-project/4.create_silver_tables
cluster -choose your cluster
depends on - Create_bronze_table

task name - Create_gold_table
path - /unity-catalog-mini-project/5.create_gold_table
cluster -choose your cluster
depends on - Create_silver_table

then run and then we will see only difference is  Lineage



#######################################################################################################

Section - 27 - Unity Catalog - Key Benefits


182. Section Overview

1. Data Discovery
2. Data audit
3. Data Lineage
4. Data Access Control


183. Data Discovery


unity-catalog-capabilities/1.data_discovery

system.information_schema - gives results of all catalog inside metastore
formula1_dev.information_schema - gives result of only catalog formula1_dev

select * from system.information_schema.tables where table_name = 'results';

select * from formula1_dev.information_schema.tables where table_name = 'results';


184. Data Audit


https://portal.azure.com/#@vajay8679gmail.onmicrosoft.com/resource/subscriptions/49a84c57-21dd-4dde-a744-8c4a8075b500/resourceGroups/databrickscourse-uc-rg/providers/Microsoft.Databricks/workspaces/databrickscourse-uc-ws/overview

go inside - databrickscourse-uc-ws -> Diagnostic settings -> enable databricks unity catalog

we will get all info of how the user is using the data,how often and when it is accessed


185. Data Lineage

it is a process of following/tracking the journey of data within a pipeline

what is the origin
how has it changed/transformed
what is the destination

data-lineage - benefits

Root cause analysis
Improved impact analysis
Trust & Reliability
Better compliance

Data Lineage Limitations

Only availabe for tables registered in unity catalog metastore
availabe only for the last 30 days
Limited columns level lineage



186. Data Access Control Overview


security model

Identity -> Secure -> Securable Object

users (1 or more)
service principal (1 or more)
Groups (users and service principal inside groups)

Role based access

Account admin (main)
Metastore Admin
Object Owner
Object User


privileges

create,select,usage

access -control-list


187. Data Access Control Demo

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/ownership#transfer-ownership

https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/privileges#manage-privileges


inside databricks top right -> go to manage account -> User management -> you will see 'account admin' and some dummy user

inside databricks top right -> go to manage account - data -> we can change permission of 'metastore admin'

inside databricks workspace - catalog - schema -table -> you can see object owner


inheritance permission

give permission to catalog and it will transfer to schema and table

you can give individual permission to table as well but you have to give permission to schema and catalog as well


#######################################################################################################

Section - 28 -  Next Steps

188. Good Luck


189. Bonus Lecture

Bonus Lecture
Many congratulations for completing the course. I hope you found the course useful.

Please checkout my courses on Azure Data Factory & Azure Synapse Analytics if you are interested in learning more about ADF and Synapse.

Please visit www.cloudboxacademy.com for student discount coupons available!

https://www.udemy.com/course/learn-azure-data-factory-from-scratch/?referralCode=E1F8CD7C853094E7652C

https://www.udemy.com/course/azure-synapse-analytics-for-data-engineers/?referralCode=5E5750F8978164E412A1

