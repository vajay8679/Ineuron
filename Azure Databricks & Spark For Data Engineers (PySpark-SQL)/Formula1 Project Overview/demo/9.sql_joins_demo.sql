-- Databricks notebook source
use f1_presentation;

-- COMMAND ----------

desc driver_standings;

-- COMMAND ----------

create or replace temp view v_driver_standings_2018
as
select race_year, driver_name, team, total_points, wins, rank
from driver_standings
where race_year = 2018;

-- COMMAND ----------

select * from v_driver_standings_2018;

-- COMMAND ----------

create or replace temp view v_driver_standings_2020
as
select race_year, driver_name, team, total_points, wins, rank
from driver_standings
where race_year = 2020;

-- COMMAND ----------

select * from v_driver_standings_2020;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Inner join

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Left Join

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  left join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Right Join

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  right join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Full Outer Join

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  full join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Semi Join
-- MAGIC
-- MAGIC it is a inner join but it will give records from left table from the join only

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  semi join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Anti Join
-- MAGIC we will get the data that didnot participate in 2020 from participant of 2018 race

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  Anti join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC #### Cross Join
-- MAGIC each record from left table will join with each record from right table - n X m

-- COMMAND ----------

select * from v_driver_standings_2018 d_2018 
  cross join v_driver_standings_2020 d_2020;
    

-- COMMAND ----------


