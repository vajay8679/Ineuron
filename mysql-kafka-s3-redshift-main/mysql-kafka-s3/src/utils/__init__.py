from src.config.environment import EnvironmentVariable
from src.config.spark_manager import spark_session
from src.entity import ExportManagementSchema
from typing import Optional
from pyspark.sql import DataFrame
from datetime import datetime
env = EnvironmentVariable()


def get_last_sent_id(topic_name)->Optional[str]:
    try:
        """
        topic_name: kafka topic name
        """
        query=f"select * from export_management where kafka_topic_name='{topic_name}' order by exported_timestamp desc limit 1"
        print(query)
        df = spark_session.read.format("jdbc").options(
            url=env.mysql.uri,
            driver='com.mysql.jdbc.Driver',
            query=query,
            user=env.mysql.user_name,
            password=env.mysql.password).load()
        if df.count()>0:
            return df.collect()[0].last_sent_id
        return None  
    except Exception as e:
        raise e

def get_latest_export_id()->Optional[int]:
    
    """
    returns latest inserted export id
    """
    try:
        query=f"select max(exp_id) exp_id from export_management"
        print(query)
        df = spark_session.read.format("jdbc").options(
            url=env.mysql.uri,
            driver='com.mysql.jdbc.Driver',
            query=query,
            user=env.mysql.user_name,
            password=env.mysql.password).load()
        if df.count()>0:
            return df.collect()[0].exp_id
        return None  
    except Exception as e:
        raise e
        
def update_last_sent_id(topic_name,last_sent_id):
    """
    topic_name: update record in export management table
    last_sent_id:
    """
    try:
        
        record = [[topic_name,last_sent_id,datetime.now()]]
        #create rdd
        rdd = spark_session.sparkContext.parallelize(record)
        df = spark_session.createDataFrame(rdd,schema=ExportManagementSchema)
        df.show()
        df.write.format("jdbc").options(url=env.mysql.uri,
                                        driver='com.mysql.jdbc.Driver',
                                        dbtable='export_management',
                                        user=env.mysql.user_name,
                                        password=env.mysql.password).mode('append').save()
    except Exception as e:
        raise e


def update_columns_as_attr(df):
    for column in df.columns:
        setattr(df,column,column)


def get_mysql_record_as_dataframe(query,update_column_attr=False)->DataFrame:
    try:
        df = (spark_session.read.format("jdbc").option("url", env.mysql.uri) 
        .option("driver", "com.mysql.cj.jdbc.Driver").option("query",query) 
        .option("user", env.mysql.user_name).option("password", env.mysql.password).load())
        if update_column_attr and df.count()>0:
            update_columns_as_attr(df)

        return df
    except Exception as e:
        raise e


    
