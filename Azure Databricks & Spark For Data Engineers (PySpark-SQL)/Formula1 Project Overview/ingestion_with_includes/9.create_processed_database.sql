-- Databricks notebook source
create database if not exists f1_processed
location "/mnt/formula1dlajay/processed" -- we choose external path of database

-- COMMAND ----------

desc database f1_processed;

-- COMMAND ----------


