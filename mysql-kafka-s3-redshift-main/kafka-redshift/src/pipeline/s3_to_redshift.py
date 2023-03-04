from src.config.environment import EnvironmentVariable
from src.config.spark_manager import spark_session
from src.config import get_data_source_info
from collections import namedtuple
from pyspark.sql import types as T
from src import entity as E
from pyspark.sql import functions as F
from src import utils as U
from pyspark.sql import DataFrame
env = EnvironmentVariable()

REDSHIFT_SCHEMA="eshop"

def s3_to_redshift_writer(s3_uri:str,schema:T.StructType,redhsift_table_name:str,mode:str="overwrite")->DataFrame:
    df= spark_session.read.schema(schema).parquet(s3_uri)
    for column in df.columns:
        print(column)
        df = df.withColumn(column,F.col(column).cast(T.StringType()))
        if column.lower()=="productDescription".lower():
            df=df.drop(column)
    # df.show()
    # df.printSchema()
    U.write_df_to_redshift(table_name=redhsift_table_name,df=df,mode=mode)
    return df
    


def transfer_data_from_s3_to_redshift():
    #prepare all required s3 uri
    data_source_info = get_data_source_info()
    TABLE_REDSHIFT_DIM_DATES="%s.%s"%(REDSHIFT_SCHEMA,"dim_dates")
    df =s3_to_redshift_writer(s3_uri=data_source_info.dim_date_key,schema=E.DimDateSchema,redhsift_table_name=TABLE_REDSHIFT_DIM_DATES,)

    TABLE_REDSHIFT_DIM_LOCATIONS="%s.%s"%(REDSHIFT_SCHEMA,"dim_location")
    df =s3_to_redshift_writer(s3_uri=data_source_info.dim_location_key,schema=E.DimLocationSchema,redhsift_table_name=TABLE_REDSHIFT_DIM_LOCATIONS,)    
    
    TABLE_REDSHIFT_DIM_PRODUCTS="%s.%s"%(REDSHIFT_SCHEMA,"dim_products")
    df =s3_to_redshift_writer(s3_uri=data_source_info.dim_product_key,schema=E.DimProductSchema,redhsift_table_name=TABLE_REDSHIFT_DIM_PRODUCTS,)    
    
    TABLE_REDSHIFT_DIM_CUSTOMERS="%s.%s"%(REDSHIFT_SCHEMA,"dim_customers")
    df =s3_to_redshift_writer(s3_uri=data_source_info.dim_customer_key,schema=E.DimCustomerSchema,redhsift_table_name=TABLE_REDSHIFT_DIM_CUSTOMERS,)    
    
    TABLE_REDSHIFT_DIM_EMPLOYEES="%s.%s"%(REDSHIFT_SCHEMA,"dim_employees")
    df =s3_to_redshift_writer(s3_uri=data_source_info.dim_employee_key,schema=E.DimEmployeeSchema,redhsift_table_name=TABLE_REDSHIFT_DIM_EMPLOYEES,)    

    TABLE_REDSHIFT_FACT_SALES="%s.%s"%(REDSHIFT_SCHEMA,"fact_sales")
    df =s3_to_redshift_writer(s3_uri=data_source_info.fact_sales_key,schema=E.FactSalesSchema,redhsift_table_name=TABLE_REDSHIFT_FACT_SALES,)

    