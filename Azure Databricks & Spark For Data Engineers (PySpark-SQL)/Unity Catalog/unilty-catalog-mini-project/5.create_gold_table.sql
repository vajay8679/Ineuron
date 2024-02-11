-- Databricks notebook source
-- MAGIC %md
-- MAGIC #### Create Managed table in the Gold table
-- MAGIC Joins Drivers and results to identify the number of wins per drivers

-- COMMAND ----------

drop table if exists formula1_dev.gold.driver_wins;

create table formula1_dev.gold.driver_wins
as 
select d.name, count(1) as number_of_wins
from formula1_dev.silver.drivers  d
join formula1_dev.silver.results  r
on (d.driver_id = r.driver_id)
where r.position = 1
group by d.name;      

-- COMMAND ----------

select * from formula1_dev.gold.driver_wins
order by number_of_wins desc;

-- COMMAND ----------


