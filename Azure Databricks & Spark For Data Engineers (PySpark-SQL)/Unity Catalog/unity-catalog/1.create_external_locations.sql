-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC #### Create the external locations required for this Project
-- MAGIC 1. Bronze
-- MAGIC 2. Silver
-- MAGIC 3. Gold
-- MAGIC

-- COMMAND ----------

CREATE EXTERNAL LOCATION databrickscourseextdl_bronze
URL 'abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databrickscourse-ext-storage-credentials`);

-- COMMAND ----------

DESC EXTERNAL LOCATION databrickscourseextdl_bronze

-- COMMAND ----------

-- MAGIC %fs
-- MAGIC ls "abfss://bronze@databrickscourseextdlaj.dfs.core.windows.net/"

-- COMMAND ----------

CREATE EXTERNAL LOCATION databrickscourseextdl_silver
URL 'abfss://silver@databrickscourseextdlaj.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databrickscourse-ext-storage-credentials`);

-- COMMAND ----------

CREATE EXTERNAL LOCATION databrickscourseextdl_gold
URL 'abfss://gold@databrickscourseextdlaj.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL `databrickscourse-ext-storage-credentials`);

-- COMMAND ----------


