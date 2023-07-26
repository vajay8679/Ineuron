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