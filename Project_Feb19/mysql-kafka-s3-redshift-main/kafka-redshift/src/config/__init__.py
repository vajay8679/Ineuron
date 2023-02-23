from collections import namedtuple
import os


DataSourceInfo = namedtuple("DataSourceInfo",
["bukcet_name",
"root_key_name",
"fact_sales_key",
"dim_product_key",
"dim_customer_key",
"dim_employee_key",
"dim_location_key",
"dim_date_key"])

S3_KEY_FACT_SALE="fact_sales"
S3_KEY_DIM_EMP="dim_employees"
S3_KEY_DIM_CUST="dim_customers"
S3_KEY_DIM_PROD="dim_products"
S3_KEY_DIM_DATE="dim_dates"
S3_KEY_DIM_LOC="dim_locations"
S3_BUCKET_NAME ="eshop-redshift"
S3_ROOT_KEY="kafka-topic"



def get_data_source_info()->DataSourceInfo:
    bucket_name=S3_BUCKET_NAME
    root_key_name=S3_ROOT_KEY
    s3_root_uri = "s3a://%s/%s/"%(bucket_name,root_key_name)
    return DataSourceInfo(bukcet_name=bucket_name,root_key_name=s3_root_uri,
    fact_sales_key="%s%s"%(s3_root_uri,S3_KEY_FACT_SALE),
    dim_customer_key="%s%s"%(s3_root_uri,S3_KEY_DIM_CUST),
    dim_employee_key="%s%s"%(s3_root_uri,S3_KEY_DIM_EMP),
    dim_product_key="%s%s"%(s3_root_uri,S3_KEY_DIM_PROD),
    dim_location_key="%s%s"%(s3_root_uri,S3_KEY_DIM_LOC),
    dim_date_key="%s%s"%(s3_root_uri,S3_KEY_DIM_DATE),
    )