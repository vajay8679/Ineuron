-- Databricks notebook source
-- MAGIC %md
-- MAGIC ##### Lesson Objectives
-- MAGIC 1. Spark SQL documentation
-- MAGIC 2. Create Database demo
-- MAGIC 3. Data tab in the UI
-- MAGIC 4. SHOW command
-- MAGIC 5. DESCRIBE command
-- MAGIC 6. Find the current database

-- COMMAND ----------

create database if not exists demo;

-- COMMAND ----------

show databases;

-- COMMAND ----------

describe database demo;

-- COMMAND ----------

describe database extended demo;

-- COMMAND ----------

select current_database();

-- COMMAND ----------

show tables;

-- COMMAND ----------

show tables in demo;

-- COMMAND ----------

use demo;

-- COMMAND ----------

show tables;

-- COMMAND ----------

select current_database();

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Managed Tables
-- MAGIC ##### Learning Objectives
-- MAGIC 1. Create managed table using Python
-- MAGIC 2. Create managed table using SQL
-- MAGIC 3. Effect of dropping a managed table
-- MAGIC 4. Describe table 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### 1.Create managed table using SQL

-- COMMAND ----------

-- MAGIC %run "../includes/configuration"

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_result")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC race_result_df.write.format("parquet").saveAsTable("demo.race_result_python")

-- COMMAND ----------

use demo;
show tables;

-- COMMAND ----------

desc extended race_result_python;

-- COMMAND ----------

select * from demo.race_result_python where race_year = 2020;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### 2.Create managed table using SQL

-- COMMAND ----------

create table demo.race_result_sql
as
select * from demo.race_result_python where race_year = 2020;

-- COMMAND ----------

desc extended race_result_sql --this table is 'managed' table and location - dbfs:/user/hive/warehouse/demo.db/race_result_sql


-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### 3.Effect of dropping a managed table

-- COMMAND ----------

drop table demo.race_result_sql; -- if we drop this table then it will delete table with metadata and all data as well

-- COMMAND ----------

show tables in demo;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### External Tables
-- MAGIC ##### Learning Objectives
-- MAGIC 1. Create external table using Python
-- MAGIC 2. Create external table using SQL
-- MAGIC 3. Effect of dropping an external table

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ##### 1.Create external table using Python

-- COMMAND ----------

-- MAGIC %python
-- MAGIC race_result_df.write.format("parquet").option("path",f"{presentation_folder_path}/race_result_ext_py").saveAsTable("demo.race_result_ext_py")

-- COMMAND ----------

desc extended demo.race_result_ext_py;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### 2.Create external table using SQL

-- COMMAND ----------

CREATE TABLE demo.race_results_ext_sql
(race_year INT,
race_name STRING,
race_date TIMESTAMP,
circuit_location STRING,
driver_name STRING,
driver_number INT,
driver_nationality STRING,
team STRING,
grid INT,
fastest_lap INT,
race_time STRING,
points FLOAT,
position INT,
created_date TIMESTAMP
)
USING PARQUET
LOCATION '/mnt/formula1dlajay/presentation/race_results_ext_sql'

-- COMMAND ----------

show tables in demo;

-- COMMAND ----------

-- we have to insert data into external table then we will get data
insert into demo.race_results_ext_sql
select * from demo.race_result_ext_py where race_year = 2020;

-- COMMAND ----------

select count(1) from demo.race_results_ext_sql;

-- COMMAND ----------

show tables in demo;

-- COMMAND ----------

drop table demo.race_results_ext_sql;

-- COMMAND ----------

show tables in demo;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Views on tables
-- MAGIC ##### Learning Objectives
-- MAGIC 1. Create Temp View
-- MAGIC 2. Create Global Temp View
-- MAGIC 3. Create Permanent View

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ##### 1.Create Temp View

-- COMMAND ----------

create or replace temp view v_race_results
as
select * from demo.race_result_python
where race_year = 2018;

-- COMMAND ----------

select * from v_race_results;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ##### 2.Create Global Temp View

-- COMMAND ----------

create or replace global temp view gv_race_results
as 
select * from demo.race_result_python
where race_year = 2012;

-- COMMAND ----------

select * from global_temp.gv_race_results; -- we can run this notebook from other notebook and detech and attach and read data from this table

-- COMMAND ----------

show tables in global_temp;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ##### 3. Create Permanent View

-- COMMAND ----------

--this view tale will stay permanent whenever we need we can have
create or replace view demo.pv_race_results
as 
select * from demo.race_result_python
where race_year = 2000;

-- COMMAND ----------

show tables in demo;

-- COMMAND ----------

select * from demo.pv_race_results;

-- COMMAND ----------


