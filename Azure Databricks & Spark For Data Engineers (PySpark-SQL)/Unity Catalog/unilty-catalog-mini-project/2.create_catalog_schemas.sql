-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC #### Create Catalog and Schema required for this project
-- MAGIC
-- MAGIC 1. Catalog - formula1_dev (without managed location)
-- MAGIC 2. Schema - bronze,silver,gold (with managed location)

-- COMMAND ----------

create catalog if not exists formula1_dev;

-- COMMAND ----------

use catalog formula1_dev;

-- COMMAND ----------

create schema if not exists bronze
managed location "abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/"

-- COMMAND ----------

create schema if not exists silver
managed location "abfss://silver@databrickscourseextdlaj.dfs.core.windows.net/"

-- COMMAND ----------

create schema if not exists gold
managed location "abfss://gold@databrickscourseextdlaj.dfs.core.windows.net/"

-- COMMAND ----------

show schemas;

-- COMMAND ----------


