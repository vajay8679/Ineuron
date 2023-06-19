#necessary libraries of pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from os.path import abspath
import logging
from pyspark.sql.functions import *

logging.basicConfig(level=logging.INFO)
warehouse_location = abspath('spark-warehouse')

spark = SparkSession.builder.master("spark://localhost:7077").appName("demo").config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport().getOrCreate()


def ratings_connect():
     schema=StructType([StructField('userid',StringType(), True),StructField('movieid1',StringType(), True),StructField('rating',StringType(), True),StructField('timestamp',StringType(), True)])
     logging.info("Reading data from ratings and programatically specified the schema")
     ratings=spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .option("sep","::").load("/ratings.csv")
     ratings.show(10,True)
     ratings.createOrReplaceTempView('ratings')
     logging.info("Saving Tables without defining DDL")
     ratings.write.mode('overwrite').saveAsTable("ratings")
     return ratings

def movies_connect():
     df=spark.read.options(delimiter='::').csv("/movies.csv")
     logging.info("Read data from csv and renamed the headers according to the requirement")
     movies=df.withColumnRenamed('_c0','movieid').withColumnRenamed('_c1','title').withColumnRenamed('_c2','genre')
     movies.show(10,True)
     movies.createOrReplaceTempView('movies')
     logging.info("Saving Tables without defining DDL")
     movies.write.mode('overwrite').saveAsTable("movies")
     return movies


def users_connect():
     df=spark.read.options(delimiter='::').csv("/users.csv")
     logging.info("Read data from csv and renamed the headers according to the requirement")
     users=df.withColumnRenamed('_c0','userid').withColumnRenamed('_c1','gender').withColumnRenamed('_c2','age').withColumnRenamed('_c3','occupation').withColumnRenamed('_c2','zip-code')
     users.show(10,True)
     users.createOrReplaceTempView('users')
     logging.info("Saving Tables without defining DDL")
     users.write.mode('overwrite').saveAsTable("users")
     return users
     



   
    
