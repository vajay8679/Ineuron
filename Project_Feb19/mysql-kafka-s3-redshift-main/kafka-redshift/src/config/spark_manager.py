from pyspark.sql import SparkSession
import os
from src.config.environment import EnvironmentVariable
env = EnvironmentVariable()
spark_session =( SparkSession.builder.master('local[*]').appName('bigdata') 
     .config("spark.executor.instances", "1") 
    .config("spark.executor.memory", "6g") 
    .config("spark.driver.memory", "6g") 
    .config("spark.executor.memoryOverhead", "8g") 
    .config('spark.jars.packages',"org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.1")
    .getOrCreate())
   
spark_session._jsc.hadoopConfiguration().set("fs.s3.awsAccessKeyId",env.aws.access_key_id)
spark_session._jsc.hadoopConfiguration().set("fs.s3.awsSecretAccessKey",env.aws.secret_access_key)


    