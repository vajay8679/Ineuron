CREATE EXTERNAL TABLE IF NOT EXISTS country_table_dezyre(
`country_code` string,
`country_name` string,
`country_total_deaths` int,
`extracted_timestamp` string )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
location '/dezyre_data/dezyre_kafka_out';
