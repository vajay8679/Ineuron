-- Databricks notebook source
use f1_processed;

-- COMMAND ----------

select races.race_year,
       constructors.name as team_name,
       drivers.name as driver_name,
       results.position,
       results.points,
       11 - results.position as calculated_points
  from results
  join drivers on (drivers.driver_id = results.driver_id)
  join constructors on (constructors.constructor_id = results.constructor_id)
  join races on (races.race_id = results.race_id)
  where results.position <= 10;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### put above query in a table inside table in  f1_presentation database

-- COMMAND ----------

create table f1_presentation.calculated_race_results
using parquet
as
select races.race_year,
       constructors.name as team_name,
       drivers.name as driver_name,
       results.position,
       results.points,
       11 - results.position as calculated_points
  from f1_processed.results
  join f1_processed.drivers on (drivers.driver_id = results.driver_id)
  join f1_processed.constructors on (constructors.constructor_id = results.constructor_id)
  join f1_processed.races on (races.race_id = results.race_id)
  where results.position <= 10;

-- COMMAND ----------

select * from f1_presentation.calculated_race_results;

-- COMMAND ----------


