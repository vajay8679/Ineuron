
from src.config.environment import EnvironmentVariable
from src.config.spark_manager import spark_session
from typing import Optional
from pyspark.sql import DataFrame
from datetime import datetime
env = EnvironmentVariable()
from datetime import datetime, date




def read_redshift_table_as_dataframe(table_name)->DataFrame:
    try:
        df = spark_session.read \
        .format("com.databricks.spark.redshift") \
        .option("url", env.redshift.uri) \
        .option("dbtable", table_name) \
        .option("redshift_tmp_dir", "/project/data") \
        .option("tempdir", "s3a://redshift-ineuron/") \
        .load()
        return df

    except Exception as e:
        raise e

def query_redshift_table_as_dataframe(query)->DataFrame:
    try:
        df = spark_session.read \
        .format("com.databricks.spark.redshift") \
        .option("url", env.redshift.uri) \
        .option("query", query) \
        .option("redshift_tmp_dir", "/project/data") \
        .option("tempdir", "s3a://redshift-ineuron/") \
        .load()
        return df

    except Exception as e:
        raise e

def write_df_to_redshift(table_name,df:DataFrame,mode:str="overwrite"):
    try:
        (df.write
        .format("com.databricks.spark.redshift") 
        .option("url", env.redshift.uri) 
        .option("dbtable", table_name) 
        .option("tempdir", "s3a://%s/"%(env.aws.temp_bucket_name)) 
        .mode(mode).save())
    except Exception as e:
        raise e

