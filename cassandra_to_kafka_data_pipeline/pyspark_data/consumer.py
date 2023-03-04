from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os
from pyspark.sql import DataFrame
import time
import logging
from datetime import datetime


#Variable declaration

#cassandra database detail
KEYSPACE = "ineuron"
TABLE="employee"

#kafka server detail
KAFKA_BOOTSTRAP_SERVER="kafka:9092"
KAFKA_TOPIC = "employee"

#Cassandra database connectivity credentails
CASSANDRA_HOST="cassandra"
CASSANDRA_USER="cassandra"
CASSANDRA_PASSWORD="cassandra"

PROCESSING_INTERVAL = f"5 seconds"

#Maining log 
#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
#log directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")
#create folder if not available
os.makedirs(LOG_FILE_DIR,exist_ok=True)


logging.basicConfig(
    filename=os.path.join(LOG_FILE_DIR,LOG_FILE_NAME),
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


#create spark session with cassandar configuration
sparkSesison = (SparkSession.builder
                 .config("spark.cassandra.connection.host","cassandra")
                 .config("spark.cassandra.auth.username","cassandra")
                 .config("spark.cassandra.auth.password","cassandra")
                 .appName("demo").getOrCreate()
                 )


schema = StructType(fields=[

StructField(name="emp_id",dataType=IntegerType()),
StructField(name="emp_name",dataType=StringType()),
StructField(name="city",dataType=StringType()),
StructField(name="state",dataType=StringType()),
])

dataSink = os.path.join("employee_data")

def processEachInterval(df:DataFrame,epoch_id):
    # print(epoch_id)
    # df.show(truncate=False)
    df = (df.withColumn("value",
        from_json(decode("value",charset="UTF-8"),schema=schema)
        .alias("value"))
        .select("value.*")
    )
    if df.count()>0:
        df.show(truncate=False)
        df.write.mode("append").parquet(dataSink)

if __name__=="__main__":
    df = (sparkSesison
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers",KAFKA_BOOTSTRAP_SERVER)
    .option("subscribe",KAFKA_TOPIC)
    .option("startingOffsets","earliest")
    .load()
    )

    df.printSchema()
    query = (df.writeStream
             .trigger(processingTime=PROCESSING_INTERVAL)
             .foreachBatch(processEachInterval)
             .start()
            )
    query.awaitTermination()