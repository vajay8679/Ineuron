-- insert statement for final table

SET hive.exec.compress.intermediate=true;
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.mapred.mode = nonstrict;

INSERT OVERWRITE TABLE final_sales_tbl partition(`order_id`)
SELECT
cast(region  as string),
cast(`country` as string),
cast(`item_type` as string),
cast(`sales_channel` as  string),
cast(`order_priority` as string),
coalesce(
 CAST( from_unixtime(unix_timestamp(`order_date`, 'MM/dd/yyyy'), 'yyyy-MM-dd') as string) ,
 CAST( from_unixtime(unix_timestamp(`order_date`, 'dd-MM-yyyy'), 'yyyy-MM-dd') as string)
) ,
coalesce(
 CAST( from_unixtime(unix_timestamp(order_date,  'MM/dd/yyyy'), "yyyy") as string) ,
  CAST(from_unixtime(unix_timestamp(order_date, 'dd-MM-yyyy'), "yyyy")AS STRING)
)as order_year,
coalesce(
 CAST( from_unixtime(unix_timestamp(`ship_date`  , 'MM/dd/yyyy'), 'yyyy-MM-dd') as string) ,
 CAST( from_unixtime(unix_timestamp(`ship_date`  , 'dd-MM-yyyy'), 'yyyy-MM-dd') as string)
) ,
coalesce(
 CAST( from_unixtime(unix_timestamp(`ship_date`  , 'MM/dd/yyyy'), "yyyy") as string) ,
  CAST(from_unixtime(unix_timestamp(`ship_date` , 'dd-MM-yyyy'), "yyyy")AS STRING)
)as shipped_year,
cast(`units_sold` as  int),
cast(`unit_price`as  float),
cast(`unit_cost` as float),
cast(`total_revenue` as  float),
cast(`total_cost`as  float),
cast(`total_profit`as  float),
cast(`order_id` as int)
FROM sales_table ;
