-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC ##### Querytable using unity catalog with 3 namespace

-- COMMAND ----------

select * from demo_catalog.demo_schema.circuits;

-- COMMAND ----------

select current_catalog()

-- COMMAND ----------

show catalogs;

-- COMMAND ----------

use catalog demo_catalog;
use schema demo_schema;
select * from circuits;

-- COMMAND ----------

select current_schema()

-- COMMAND ----------

show schemas;

-- COMMAND ----------

show tables;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC display(spark.sql('show tables'));

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df = spark.table("demo_catalog.demo_schema.circuits")

-- COMMAND ----------

-- MAGIC %python display(df)

-- COMMAND ----------


