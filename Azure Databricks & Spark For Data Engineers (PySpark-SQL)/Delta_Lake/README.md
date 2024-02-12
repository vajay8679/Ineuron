###################################################################################

Section - 22 - Delta Lake

136. Section Overview


137. Pitfalls of Data Lakes


pitfalls means drabacks of data lake- acid transactions, versioning, time travel, BI workloads,streaming and batch workloads


138. Data Lakehouse Architecture

lakehouse architecutre



139. Read & Write to Delta Lake

Delta_Lake/set-up/mount_adls_storage - file

#mount demo folder to adls first

# Databricks notebook source
storage_account_name = "formula1dlajay"
client_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-id")
tenant_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-tenant-id") 
client_secret = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-secret")

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

def mount_adls(container_name):
  dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

mount_adls("demo")

dbutils.fs.ls("/mnt/formula1dlajay/demo")

# dbutils.fs.unmount("/mnt/formula1dlajay/demo")


Delta_Lake/set-up/10.delta_lake_demo

Write data to delta lake (managed table)
Write data to delta lake (external table)
Read data from delta lake (Table)
Read data from delta lake (File)


https://docs.delta.io/latest/index.html

https://docs.databricks.com/en/index.html

https://learn.microsoft.com/en-us/azure/databricks/delta/

#write to a table
https://docs.delta.io/latest/delta-batch.html#write-to-a-table

%sql

create database if not exists f1_demo
location '/mnt/formula1dlajay/demo'


result_df = spark.read.option('inferSchema',True).json('/mnt/formula1dlajay/raw/2021-03-28/results.json')

#Write data to delta lake (managed table)
result_df.write.format("delta").mode("overwrite").saveAsTable("f1_demo.results_managed")

%sql
select * from f1_demo.results_managed;

#Write data to delta lake (external table)
result_df.write.format("delta").mode("overwrite").save("/mnt/formula1dlajay/demo/results_external")

%sql
create table f1_demo.results_external
USING DELTA
location '/mnt/formula1dlajay/demo/results_external'


%sql
--Read data from delta lake (Table)
select * from f1_demo.results_external

#Read data from delta lake (File)
results_external_df = spark.read.format("delta").load('/mnt/formula1dlajay/demo/results_external')

display(results_external_df)

#partitioned by
result_df.write.format("delta").mode("overwrite").partitionBy("constructorId").saveAsTable("f1_demo.results_partitoned")


%sql
show partitions f1_demo.results_partitoned;


140. Updates and Deletes on Delta Lake

https://docs.delta.io/latest/delta-update.html#update-a-table

Update Delta Table
Delete From Delta Table

%sql
select * from f1_demo.results_managed;

%sql
--update using sql
update f1_demo.results_managed
  set points = 11 - position
where position <= 10

%sql
select * from f1_demo.results_managed;


#update using pythonic way

from delta.tables import DeltaTable
deltaTable = DeltaTable.forPath(spark, '/mnt/formula1dlajay/demo/results_managed')
# Declare the predicate by using a SQL-formatted string.
# deltaTable.update(condition = "position <= 10", set = { "points": "21 - position" })
deltaTable.update("position <= 10",{ "points": "21 - position" })

%sql
select * from f1_demo.results_managed;

%sql
delete from f1_demo.results_managed
where position > 10;

%sql
select * from f1_demo.results_managed;

#delete using pythonic way
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, '/mnt/formula1dlajay/demo/results_managed')
deltaTable.delete("points = 0");

%sql
select * from f1_demo.results_managed;



141. Merge/ Upsert to Delta Lake

Upsert using merge

drivers_day1_df = spark.read.option("inferSchema",True) \
    .json('/mnt/formula1dlajay/raw/2021-03-28/drivers.json') \
    .filter("driverId <= 10") \
    .select("driverId","dob","name.forename","name.surname")

drivers_day1_df.createOrReplaceTempView("drivers_day1") 

display(drivers_day1_df)


from pyspark.sql.functions import upper

drivers_day2_df = spark.read.option("inferSchema",True) \
    .json("/mnt/formula1dlajay/raw/2021-03-28/drivers.json") \
    .filter("driverId BETWEEN 6 and 15") \
    .select("driverId","dob",upper("name.forename").alias("forename"),upper("name.surname").alias("surname"))

drivers_day2_df.createOrReplaceTempView("drivers_day2")

display(drivers_day2_df)

from pyspark.sql.functions import upper

drivers_day3_df = spark.read.option("inferSchema",True) \
    .json("/mnt/formula1dlajay/raw/2021-03-28/drivers.json") \
    .filter("driverId BETWEEN 1 and 5 or driverId BETWEEN 16 and 20") \
    .select("driverId","dob",upper("name.forename").alias("forename"),upper("name.surname").alias("surname"))

%sql

create table if not exists f1_demo.drivers_merge (
  driverId INT,
  dob Date,
  forename string,
  surname string,
  createdDate date,
  updatedDate date
)
using delta


%sql

MERGE INTO f1_demo.drivers_merge tgt
USING drivers_day1 upd
ON tgt.driverId = upd.driverId
WHEN MATCHED THEN
  UPDATE SET
    tgt.dob = upd.dob,
    tgt.forename = upd.forename,
    tgt.surname = upd.surname,
    tgt.updatedDate = current_timestamp
WHEN NOT MATCHED
  THEN INSERT (
    driverId,
    dob,
    forename,
    surname,
    createdDate
  )
  VALUES (
    driverId,
    dob,
    forename,
    surname,
    current_timestamp
  )

%sql
select * from f1_demo.drivers_merge;

%sql

MERGE INTO f1_demo.drivers_merge tgt
USING drivers_day2 upd
ON tgt.driverId = upd.driverId
WHEN MATCHED THEN
  UPDATE SET
    tgt.dob = upd.dob,
    tgt.forename = upd.forename,
    tgt.surname = upd.surname,
    tgt.updatedDate = current_timestamp
WHEN NOT MATCHED
  THEN INSERT (
    driverId,
    dob,
    forename,
    surname,
    createdDate
  )
  VALUES (
    driverId,
    dob,
    forename,
    surname,
    current_timestamp
  )

%sql
select * from f1_demo.drivers_merge;


from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, '/mnt/formula1dlajay/demo/drivers_merge')

deltaTable.alias('tgt') \
  .merge(
    drivers_day3_df.alias('upd'),
    'tgt.driverId = upd.driverId'
  ) \
  .whenMatchedUpdate(set =
    {
      "dob": "upd.dob",
      "forename": "upd.forename",
      "surname": "upd.surname",
      "updatedDate": "current_timestamp()"      
    }
  ) \
  .whenNotMatchedInsert(values =
    {
      "driverId": "upd.driverId",
      "dob": "upd.dob",
      "forename": "upd.forename",
      "surname": "upd.surname",
      "createdDate": "current_timestamp()"      
    }
  ) \
  .execute()

%sql
select * from f1_demo.drivers_merge;


142. History, Time Travel, Vacuum

History & Versioning
Time Travel
Vaccum - remove data for particular user (but it removes data after 7 days)


%sql
desc history f1_demo.drivers_merge


%sql
select * from f1_demo.drivers_merge version as of 2;

%sql
select * from f1_demo.drivers_merge timestamp as of "2024-02-03T15:32:23Z";


#spark version
df = spark.read.format("delta").option("timestampAsOf","2024-02-03T15:32:23Z").load("/mnt/formula1dlajay/demo/drivers_merge")

display(df)

df = spark.read.format("delta").option("versionAsOf","2").load("/mnt/formula1dlajay/demo/drivers_merge")
display(df)


#Vaccum - remove data for particular user (but it removes data after 7 days)

%sql
vacuum f1_demo.drivers_merge;

#you will see data in below query
%sql
select * from f1_demo.drivers_merge timestamp as of "2024-02-03T15:32:23Z"; -- still show data because it delete after 7 days



#to delete immediately we have to use retain 0 hours

%sql
SET spark.databricks.delta.retentionDurationCheck.enabled = false;
VACUUM f1_demo.drivers_merge RETAIN 0 HOURS

%sql
-- you wont see data in below query - you will get error
select * from f1_demo.drivers_merge timestamp as of "2024-02-03T15:32:23Z";


%sql
-- you can see latest data in below query but you can not see the history data
select * from f1_demo.drivers_merge



%sql
desc history f1_demo.drivers_merge

%sql
--delete from the records and restore with the help of history
delete from f1_demo.drivers_merge where driverId = 1;

%sql
-- you will see 19 records
select * from f1_demo.drivers_merge;

%sql
-- you will see 20 records in last version
select * from f1_demo.drivers_merge version as of 3;

# we will use merge command to restore the deleted data 

%sql
--merge command use to restore deleted record
merge into f1_demo.drivers_merge tgt
using f1_demo.drivers_merge version as of 3 src
on (tgt.driverId = src.driverId)
when not matched then 
insert *


# we will see merge operation after delete
%sql desc history f1_demo.drivers_merge

# you will see restored data and 20 data in below command
%sql 
select * from  f1_demo.drivers_merge


143. Delta Lake Transaction Log

meta store only keeps info of table and attributes
Transaction Logs are not kept in th hive meta store because it is really inefficient to go and read hive meta store and and get all information for everything

delta lake did some clever thing for that (inside delta lake or data lake it creates log folder(_delta_log) and inside that folder .json and crc file where it keeps timestamps userid username,operation,azure account etc )


%sql

create table if not exists f1_demo.drivers_txn (
  driverId INT,
  dob Date,
  forename string,
  surname string,
  createdDate date,
  updatedDate date
)
using delta


%sql desc history f1_demo.drivers_txn;

# different parquet file will create and 00000000000000000001.json file for versioning and when we will read data for version then it will read parquet file of this operation

%sql
insert into f1_demo.drivers_txn
select * from f1_demo.drivers_merge
where driverId = 1;

%sql desc history f1_demo.drivers_txn;


# different parquet file will create and 00000000000000000002.json file for versioning and when we will read data for version then it will read parquet file of this operation

%sql
insert into f1_demo.drivers_txn
select * from f1_demo.drivers_merge
where driverId = 2;


%sql
delete from f1_demo.drivers_txn
where driverId = 1;


# it wil create 18 .json file and 2-3 compacted.json file will create in transaction log file


for driver_id in range(3,20):
    spark.sql(f"""insert into f1_demo.drivers_txn
              select * from f1_demo.drivers_merge
              where driverId = {driver_id}""")


# it wil create 1 .json file inside log folder and 2-3 partition file

%sql
insert into f1_demo.drivers_txn
select * from f1_demo.drivers_merge;

# transaction log stays for 30 days after that azure deletes it because it cost and slower the process



144. Convert from Parquet to Delta

# convert parquet file or table to delta table

%sql

create table if not exists f1_demo.drivers_convert_to_delta (
  driverId INT,
  dob Date,
  forename string,
  surname string,
  createdDate date,
  updatedDate date
)
using parquet

%sql
insert into f1_demo.drivers_convert_to_delta
select * from f1_demo.drivers_merge

%sql
--convert parquet table to delta table
convert to delta f1_demo.drivers_convert_to_delta


df  = spark.table("f1_demo.drivers_convert_to_delta")

# create a parquet file into delta table (it will create transaction log files .josn and .crc file after converting we can do our own operations as we want)
df.write.format("parquet").save('/mnt/formula1dlajay/demo/drivers_convert_to_delta_new')

%sql
convert to delta parquet.`/mnt/formula1dlajay/demo/drivers_convert_to_delta_new`


145. Data Ingestion - Circuits File


utils/1.prepare_for_incremental_load - file
run all command for this file because we want to delete all tables;


Delta_Lake/ingestion_with_includes/1.ingest_circuits_file 
Delta_Lake/ingestion_with_includes/2.ingest_races_file
Delta_Lake/ingestion_with_includes/3.ingest_constructors_file
Delta_Lake/ingestion_with_includes/4.ingest_drivers_file

only change we have to do

%run "../../includes/configuration"
%run "../../includes/common_functions"
circuits_final_df.write.mode("overwrite").format("delta").saveAsTable("f1_processed.circuits")


146. Data Ingestion - Results File

Delta_Lake/ingestion_with_includes/5.ingest_results_file - file

%run "../../includes/configuration"
%run "../../includes/common_functions"

#by using partition column in merge statement then query will be quiker -> tgt.race_id = src.race_id

spark.conf.set("spark.databricks.optimizer.dynamicPartitionPruning","true")
from delta.tables import DeltaTable

if (spark._jsparkSession.catalog().tableExists("f1_processed.results")):
   deltaTable = DeltaTable.forPath(spark,"/mnt/formula1dlajay/processed/results")
   deltaTable.alias('tgt').merge(
       results_final_df.alias("src"),
       "tgt.result_id = src.result_id and tgt.race_id = src.race_id") \
       .whenMatchedUpdateAll() \
       .whenNotMatchedInsertAll() \
       .execute() 
else:
      results_final_df.write.mode("overwrite").partitionBy("race_id").format("delta").saveAsTable("f1_processed.results")


147. Data Ingestion - Results File Improvements


includes/common_functions - file

# add below function

def merge_delta_data(input_df, db_name,table_name,partition_column,folder_path,merge_condition):
  
  spark.conf.set("spark.databricks.optimizer.dynamicPartitionPruning","true")
  from delta.tables import DeltaTable
  
  if (spark._jsparkSession.catalog().tableExists(f"{db_name}.{table_name}")):
    deltaTable = DeltaTable.forPath(spark,f"{folder_path}/{table_name}")
    deltaTable.alias('tgt').merge(
    input_df.alias("src"),
    merge_condition) \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute() 
  else:
      input_df.write.mode("overwrite").partitionBy(partition_column).format("delta").saveAsTable(f"{db_name}.{table_name}")


# in below file add below code and call function
Delta_Lake/ingestion_with_includes/5.ingest_results_file - file

merge_condition = "tgt.result_id = src.result_id and tgt.race_id = src.race_id"
merge_delta_data(results_final_df, "f1_processed", "results", "race_id",processed_folder_path, merge_condition)


148. Data Ingestion - All Other Files (Assignment)

# https://ergast.com/docs/f1db_user_guide.txt - only take primary id and partition column in merge condition
Delta_Lake/ingestion_with_includes/6.ingest_pit_stops_file

merge_condition = "tgt.race_id = src.race_id and tgt.driver_id = src.driver_id and tgt.stop = src.stop and tgt.race_id = src.race_id"
merge_delta_data(pit_stops_with_columns_df, "f1_processed", "pit_stops", "race_id", processed_folder_path, merge_condition)


%sql
select race_id, count(1) from f1_processed.pit_stops
group by race_id
order by race_id desc;



# https://ergast.com/docs/f1db_user_guide.txt -> only take primary id and partition column in merge condition
merge_condition = "tgt.race_id = src.race_id and tgt.driver_id = src.driver_id and tgt.lap = src.lap and tgt.race_id = src.race_id"
merge_delta_data(lap_times_with_columns_df, "f1_processed", "lap_times", "race_id", processed_folder_path, merge_condition)

%sql
select * from f1_processed.lap_times;

Delta_Lake/ingestion_with_includes/8.ingest_qualifying_file
# https://ergast.com/docs/f1db_user_guide.txt -> only take primary id and partition column in merge condition
merge_condition = "tgt.qualify_id = src.qualify_id and tgt.race_id = src.race_id"
merge_delta_data(qualifying_with_columns_df, "f1_processed", "qualifying", "race_id", processed_folder_path, merge_condition)

%sql
select * from f1_processed.qualifying;


149. Data Ingestion - Fix Duplicates in Results Data


Delta_Lake/ingestion_with_includes/5.ingest_results_file
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.dropDuplicates.html


# De-dupe the Dataframe -> remove duplicates values

results_deduped_df = results_final_df.dropDuplicates(["race_id","driver_id"])

merge_condition = "tgt.result_id = src.result_id and tgt.race_id = src.race_id"
merge_delta_data(results_deduped_df, "f1_processed", "results", "race_id",processed_folder_path, merge_condition)

%sql
-- give no result becuase we create data frame for no duplicates
select race_id,driver_id, count(1) from f1_processed.results
group by race_id,driver_id
having count(1) > 1
order by race_id, driver_id desc;

%sql
select count(1) from f1_processed.results; #give count

%sql
select * from f1_processed.results where race_id = 540 and driver_id = 229; # remove duplcate result

%sql
select count(1) from f1_processed.results;  


150. Data Transformation - All PySpark Notebooks


Delta_Lake/trnas/1.race_results

# read all the delta dataframe from above file

drivers_df = spark.read.format("delta").load(f"{processed_folder_path}/drivers") \
    .withColumnRenamed("number","driver_number") \
    .withColumnRenamed("name","driver_name") \
    .withColumnRenamed("nationality", "driver_nationality")



merge_condition = "tgt.driver_name = src.driver_name and tgt.race_id = src.race_id"
merge_delta_data(final_df, "f1_presentation", "race_results", "race_id",presentation_folder_path, merge_condition)


%sql
select * from f1_presentation.race_results ;


%sql
select race_id, count(1) from f1_presentation.race_results
group by race_id
order by race_id desc;


Delta_Lake/trnas/2.driver_standings 

race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") 

race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))

merge_condition = "tgt.driver_name = src.driver_name and tgt.race_year = src.race_year"
merge_delta_data(final_df, "f1_presentation", "driver_standings", "race_year",presentation_folder_path, merge_condition)


%sql
select * from f1_presentation.driver_standings where race_year = 2021;


%sql
select race_year,count(1) from f1_presentation.driver_standings
group by race_year
order by race_year desc;



Delta_Lake/trnas/3.constructor_standings


race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") 


race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))

merge_condition = "tgt.team = src.team and tgt.race_year = src.race_year"
merge_delta_data(final_df, "f1_presentation", "constructor_standings", "race_year",presentation_folder_path, merge_condition)

%sql
select * from f1_presentation.constructor_standings where race_year = 2021;

%sql
select race_year,count(1) from f1_presentation.driver_standings
group by race_year
order by race_year desc;

151. Data Transformation - SQL Notebook

Delta_Lake/trnas/4.calculated_race_result

dbutils.widgets.text("p_file_date","2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")


spark.sql(f"""
          create table if not exists f1_presentation.calculated_race_results(
          race_year int,
          team_name string,
          driver_id int,
          driver_name string,
          race_id int,
          position int,
          points int,
          calculated_points int,
          created_date TIMESTAMP,
          updated_date TIMESTAMP
          )
          using delta
    """)

spark.sql(f"""
                create or replace temp view race_result_updated
                as
                select races.race_year,
                constructors.name as team_name,
                drivers.driver_id,
                drivers.name as driver_name,
                races.race_id,
                results.position,
                results.points,
                11 - results.position as calculated_points
                from f1_processed.results
                join f1_processed.drivers on (drivers.driver_id = results.driver_id)
                join f1_processed.constructors on (constructors.constructor_id = results.constructor_id)
                join f1_processed.races on (races.race_id = results.race_id)
                where results.position <= 10 and results.file_date = '{v_file_date}'                 
          
    """)

# %sql select * from race_result_updated where race_year = 2021;


#by running below command we will get incremental data in table - f1_presentation.calculated_race_results

spark.sql(f"""
        MERGE INTO f1_presentation.calculated_race_results tgt
        USING race_result_updated upd
        ON (tgt.driver_id = upd.driver_id and tgt.race_id = upd.race_id)
        WHEN MATCHED THEN
        UPDATE SET
            tgt.position = upd.position,
            tgt.points = upd.points,
            tgt.calculated_points = upd.calculated_points,
            tgt.updated_date = current_timestamp
        WHEN NOT MATCHED
        THEN INSERT (
            race_year,
            team_name,
            driver_id,
            driver_name,
            race_id,
            position,
            points,
            calculated_points,
            created_date
        )
        VALUES (
            race_year,
            team_name,
            driver_id,
            driver_name,
            race_id,
            position,
            points,
            calculated_points,
            current_timestamp
        )
   """)

%sql select count(1) from race_result_updated;

%sql select count(1) from f1_presentation.calculated_race_results;



###################################################################################

Section - 23 - Azure Data Factory

152. Section Overview

it use to schedule and execute databricks notebook



153. Azure Data Factory Overview

a fully managed, serverless data integration solution for ingesting, preparing and transforming all your data at scale.

data coming from clouds(AWS,azure,GCP)  ,saas, on prime applications in different data formats

Azure Datafactory Provides end to end dat ingestion , transformation and orchestration

What Datafactory is 
1. Fully Managed service
2. serverless
3. Data Integration service
4. Data transformation service
5. Data orchestration service

What Datafactory is not
1. Data migration tool
2. Data Streaming service
3. Suitable for Complex Data transformation
4. Data Storage service


154. Create Azure Data Factory Service

https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.DataFactory%2FdataFactories

resource group - databrickscourse-rg
name - databricks-course-adf-ajay
region - central india


Resource group : databrickscourse-rg

# Go to launch studio

Location:Central India
Subscription:Azure subscription 1
Subscription ID:49a84c57-21dd-4dde-a744-8c4a8075b500
Type:Data factory (V2)

data factory interface


155. Azure Data Factory Components

Components - storage(adls,sql database) -> linked Service -> datasets -> Activity -> Pipeline -> trigger
Components - compute(azure databricks,azure hdinsights) -> linked Service  -> Activity -> Pipeline -> trigger

156. Create Pipeline - Circuits File

go inside data factory -> author -> pipeline -> new pipeline

pipeline name - pl_ingest_formula1_data

drag jupyter notebook
 name  - 

# linked service
 subscription name -Azure subscription 1 (49a84c57-21dd-4dde-a744-8c4a8075b500)
 name - ls_databrickscourse_ws
 Account selection method* - From Azure subscription
 Select cluster - Existing interactive cluster
 Authentication type - managed service type 

and copy Managed identity name
Managed identity name: databricks-course-adf-ajay

Managed identity name:databricks-course-adf-ajay
Managed identity object ID:540ae937-0dbe-4002-82a2-85ecf1f4edbc
Grant Data Factory service managed identity access to your Resources.

Choose from existing clusters - Databricks-course-cluster


# job cluster  - destory automatically after job is finished

https://portal.azure.com/#view/Microsoft_Azure_AD/AddRoleAssignmentsLandingBlade/scope/%2Fsubscriptions%2F49a84c57-21dd-4dde-a744-8c4a8075b500%2FresourceGroups%2Fdatabrickscourse-rg%2Fproviders%2FMicrosoft.Databricks%2Fworkspaces%2Fdatabrickscourse-ws/abacSettings~/%7B%7D/priorityRoles~/%5B%5D

Go inside -> databrickscourse-ws | Access control (IAM) -> Privileged administrator roles -> Contributor -> then select -> databricks-course-adf-ajay 

and then create so databricks will be connected to datafactory

in setting select notebook 'Delta_lake/ingestion_with_includes/1.ingest_circuits_file' -> notebook

go to setting of pipeline after clicking outside of notebook 
got to -> variable - v_data_source - Ergapt
got to -> parameter - p_window_end_date


inside parameter of setting of pipeline -> p_window_end_date - 
go to settin of notebook -> base parameter ->   p_data_source - @variables('v_data_source') (selected dynamically)
go to settin of notebook -> base parameter ->   p_file_date - @formatDateTime(pipeline().parameters.p_window_end_date,'yyyy-MM-dd') (selected formatdate function and then select parameter -> p_window_end_date and then format datasets)


157. Debugging a Pipeline

go to debug option on top and then it will ask for date 'p_window_end_date' -> 2021-04-18




158. Update Pipeline - Ingest All Other Files

duplicate all other files from folder -Delta_lake/ingestion_with_includes/all 8 files


159. Improve Pipeline - Handle Missing Files

in ADF - Activity-> general -> metadata -
Name - 'Get Folder Data'


Settings - select ADLS Gen2 ->
 format - json ->
 properties -> name : ds_formula1_raw

 new link service 
 name -ls_formula1_storage
 Authentication type - Account key
Storage account name* -  formula1dlajay

@formatDateTime(dataset().p_window_end_date,'yyy-MM-dd')

@pipeline().parameters.p_window_end_date


Get Folder Data -> Setting ->Dataset properties
Name	p_window_end_date	
Value	@pipeline().parameters.p_window_end_date	

Field list * -> Exists

in ADF - Activity-> iteration & conditiona -> if condition ->

name - If Folder Exists
Expression (dynamic) - @activity('Get Folder Data').output.exists   


now copy all notebook and put inside if condition and debug with - false condtion -> 2021-03-20 
                                                                  then true condtion -> 2021-03-21


and then publish

160. Create Pipeline - Transformation Notebooks

Delta_Lake/trans/all four files

clone first pipeline
name - pl_transform_formula1_data

we only need base parameter p_file_date
p_file_date - @formatDateTime(pipeline().parameters.p_window_end_date,'yyy-MM-dd')



we will connect both pipeline with pipeline with -> pl_process_formula1_data

3.pl_process_formula1_data -> 1.pl_ingest_formula1_data -> 2.pl_transform_formula1_data


search

Adf -> Execute pipeline

pipeline :- Execute Ingestion -> Execute Transformation
p_window_end_date -> @pipeline().parameters.p_window_end_date


161. Create ADF Trigger

https://learn.microsoft.com/en-us/azure/data-factory/

https://learn.microsoft.com/en-us/azure/data-factory/control-flow-system-variables

use for parameter - p_window_end_date -  @trigger().outputs.windowEndTime	

create trigger
name -tr_process_formula1_data


type - 1.schedule - every day 10am monday to frienday
       2. Tumbling window - from 6-12am , 12-6pm (regular interval, or we can schedule based on required date for our purposes)
       3. storage event -(anything happend inside storage - add,delete,update then trigger will run)


       choose - Tumbling window
       choose start date and end date 
       every 168 hour - minute
       max concurancy - 1
       retry policy - 30
       status - No

add trigger to -> pl_process_formula1_data pipeline
use for parameter - p_window_end_date -  @trigger().outputs.windowEndTime	



then go to monitior tab in left and trigger run

go to trigger run -> its setting -> add end date column and then ok 

and then run the trigger




#######################################################################################################

Section - 24 -  Connect other services


162. Power BI


to connect databricks with power bi -we have to go to get data and then azure and then databricks

inside power bi 

 get data -> azure -> databricks -> cluster -> advanced setting -> jdbc/odbc -> server name -> http path 

 then connect with  import -> azure active direcotry / personal access token


 personal access token - dapi132162c63883c265c2b85163d7678670


