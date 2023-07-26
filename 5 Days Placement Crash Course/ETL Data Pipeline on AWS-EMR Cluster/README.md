#1. create EMR Cluster - 'emrclusterStarting'  
https://ap-south-1.console.aws.amazon.com/elasticmapreduce/home?fn=1690219485731&region=ap-south-1#cluster-list:



#2. select key value pair or create    
https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#KeyPairs:

#security group - select master  
https://ap-south-1.console.aws.amazon.com/ec2/home?fn=1690219485731&region=ap-south-1#SecurityGroups:search=sg-061bfc018223c853b

click on master security group and then inbound rules then add IP 
ssh -> myIP


#3. create S3 bucket
'emretldatapipeline' and upload file 'sales_data copy.csv'


#4. on terminal after creating EMR cluster
1. chmod 400 emrdatapipeline.pem
2. ssh -i ~/Desktop/Ajay/Ineuron/5\ Days\ Placement\ Crash\ Course/Data_Pipeline/emrdatapipeline.pem hadoop@ec2-3-110-218-220.ap-south-1.compute.amazonaws.com



[hadoop@ip-172-31-12-74 ~]$ hive

Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j2.properties Async: false
hive> create database emrDb;
OK
Time taken: 1.167 seconds, Fetched: 1 row(s)
hive> use emrDb; 


#1st

CREATE EXTERNAL TABLE IF NOT EXISTS sales_table
(
`region` string,
`country`  string,
`item_type`  string,
`sales_channel`  string,
`order_priority`  string,
`order_date`  string,
`order_id` string,
`ship_date`  string,
`units_sold`  string,
`unit_price`  string,
`unit_cost`  string,
`total_revenue` string,
`total_cost`  string,
`total_profit`  string
) ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
LOCATION 's3://emretldatapipeline/';


#2nd

CREATE TABLE IF NOT EXISTS final_sales_tbl
(
`region` string,
`country`  string,
`item_type`  string,
`sales_channel`  string,
`order_priority`  string,
`order_date`  string,
`order_year` string,
`ship_date`  string,
`shipped_year`  string,
`units_sold`  int,
`unit_price`  float,
`unit_cost`  float,
`total_revenue`  float,
`total_cost`  float,
`total_profit`  float
) PARTITIONED BY (`order_id` int)
STORED AS ORC;


#3rd

-- insert statement for final table

SET hive.exec.compress.intermediate=true;
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.mapred.mode = nonstrict;



#4th

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
FROM sales_table limit 30;


#Tez UI  
https://p-2s4hhxi0tkwm0-tezui.emrappui-prod.ap-south-1.amazonaws.com/tez-ui/


hive> show tables;
OK
final_sales_tbl
sales_table
Time taken: 0.053 seconds, Fetched: 2 row(s)
hive> select * from final_sales_tbl limit 10;
hive> show partitions final_sales_tbl;





#for visualization we can use tablue

