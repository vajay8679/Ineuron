-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC #### Drop all the tables

-- COMMAND ----------

drop database if exists f1_processed cascade;

-- COMMAND ----------

create database if not exists f1_processed 
Location '/mnt/formula1dlajay/processed';

-- COMMAND ----------

drop database if exists f1_presentation cascade;

-- COMMAND ----------

create database if not exists f1_presentation 
Location '/mnt/formula1dlajay/presentation';
