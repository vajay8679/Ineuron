CREATE EXTERNAL TABLE IF NOT EXISTS corona_table(
`Global_new_confirmed` int,
`Global_new_deaths` int,
`Global_new_recovered` int,
`Global_total_confirmed` int,
`Global_total_deaths` int,
`Global_total_recovered` int,
`Country_code` string,
`Country_name` string,
`Country_new_deaths` int,
`Country_new_recovered` int,
`Country_new_confirmed` int,
`Country_total_deaths` int,
`Country_total_confirmed` int,
`Country_total_recovered` int,
`Country_slug` string,
`Extracted_timestamp` timestamp,
`country_code_hash` string,
`Country_code_final` string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
location '/dezyre_data/corona-table';
