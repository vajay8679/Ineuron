from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import datetime
import time
from pyspark.sql.functions import split
from pyspark.sql.functions import *
#sc = SparkContext(appName='dezyre_test')
#sc.setLogLevel('WARN')
#spark = SparkSession(sc)
spark = SparkSession.builder.appName("pyspark-notebook").\
config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0").\
getOrCreate()
 
#Read streaming data from Kafka into Pyspark dataframe
dfCSV=spark.readStream.format('kafka').option('kafka.bootstrap.servers','kafka:9092').option('subscribe', 'dezyre_data_csv').option("failOnDataLoss","false").option('startingOffsets', 'earliest').load().selectExpr("CAST(value AS STRING)")
dfCSV.printSchema()

#Define schema for the data
userSchema =StructType([
StructField('Global_new_confirmed',StringType()),
StructField('Global_new_deaths',StringType()),
StructField('Global_new_recovered',StringType()),
StructField('Global_total_confirmed',StringType()),
StructField('Global_total_deaths',StringType()),
StructField('Global_total_recovered',StringType()),
StructField('Country_code',StringType()),
StructField('Country_name',StringType()),
StructField('Country_new_deaths',StringType()),
StructField('Country_new_recovered',StringType()),
StructField('Country_new_confirmed',StringType()),
StructField('Country_total_deaths',StringType()),
StructField('Country_total_confirmed',StringType()),
StructField('Country_total_recovered',StringType()),
StructField('Country_slug',StringType()),
StructField('Extracted_timestamp',TimestampType()),
StructField('country_code_hash',StringType()),
StructField('Country_code_final',StringType())

])


print("coming1-->")

#Parse the data 
def parse_data_from_kafka_message(sdf, schema):
  from pyspark.sql.functions import split
  assert sdf.isStreaming == True, "DataFrame doesn't receive streaming data"
  col = split(sdf['value'], ',') #split attributes to nested array in one Column
  #now expand col to multiple top-level columns
  for idx, field in enumerate(schema): 
      sdf  = sdf.withColumn(field.name, col.getItem(idx).cast(field.dataType))
  return sdf.select([field.name for field in schema])
dfCSV = parse_data_from_kafka_message(dfCSV, userSchema)

print("coming2-->")
#Process the data 
q=dfCSV.groupBy("Country_code_final","Country_name","Country_total_deaths","Extracted_timestamp").count()

print("coming3-->")
#Write streaming data to output Kafka topic which can be consumed by destination services like #HDFS, Nifi, etc.
q2=q.select(to_json(struct(
'Country_code_final',
'Country_name',
'Country_total_deaths','Extracted_timestamp')).alias('value')).writeStream.format("kafka").outputMode("complete").option("failOnDataLoss","false").option('checkpointLocation','/checkpoint/').option("kafka.bootstrap.servers","kafka:9092").option("topic", "dezyre_out").start().awaitTermination()
