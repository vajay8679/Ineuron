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
LOCATION 's3://etlemr01/';