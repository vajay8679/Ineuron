-- Databricks notebook source
-- MAGIC %sql
-- MAGIC DROP table if exists employeeData;
-- MAGIC

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC create table emloyeeData1 USING CSV OPTIONS(path="dbfs:/FileStore/tables/employees1.csv" , header="true")

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC select * from emloyeeData1;

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC select gender, avg(salary) as AvgSalary from emloyeeData1 group by gender;

-- COMMAND ----------



-- COMMAND ----------


