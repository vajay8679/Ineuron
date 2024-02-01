-- Databricks notebook source
select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
group by driver_name
having count(1) > 50
order by avg_points desc;

-- COMMAND ----------

select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2011 and 2020
group by driver_name
having count(1) > 50
order by avg_points desc;

-- COMMAND ----------

select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2001 and 2010
group by driver_name
having count(1) > 50
order by avg_points desc;

-- COMMAND ----------


