-- Databricks notebook source
-- MAGIC %md
-- MAGIC #### Create Bronze tables
-- MAGIC 1. drivers.json
-- MAGIC 2. results.json Bronze folder path - abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/

-- COMMAND ----------

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

-- COMMAND ----------

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

-- COMMAND ----------


