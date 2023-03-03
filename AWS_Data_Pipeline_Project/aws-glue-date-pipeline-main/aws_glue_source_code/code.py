
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as func
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import LongType
from awsglue.job import Job
import os 
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#declaring constant variables
BUCKET_NAME="data327030"
DYNAMODB_TABLE_NAME="fc_data"
INPUT_FILE_PATH=f"s3://{BUCKET_NAME}/inbox/*json"

#getting logger object to log the progress
logger  = glueContext.get_logger()
logger.info(f"Started reading json file from {INPUT_FILE_PATH}")
df_sparkdf=spark.read.json(INPUT_FILE_PATH)
logger.info(f"Type casting columns of spark dataframe to Long type")
df_sparkdf = df_sparkdf.withColumn("complaint_id",func.col("complaint_id").cast(LongType()))

logger.info(f"Columns in dataframe : {len(df_sparkdf.columns)}--> {df_sparkdf.columns}")
logger.info(f"Number of rows found in file: {df_sparkdf.count()} ")

dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="dynamodb",
    connection_options={"dynamodb.input.tableName": DYNAMODB_TABLE_NAME,
        "dynamodb.throughput.read.percent": "1.0",
        "dynamodb.splits": "100"
    }
)
dyf_sparkdf=dyf.toDF()
new_sparkdf=None
if dyf_sparkdf.count()!=0:
    logger.info(f"Columns in dynamodb dataframe : {len(dyf_sparkdf.columns)}--> {dyf_sparkdf.columns}")
    logger.info(f"Number of rows found in file: {dyf_sparkdf.count()} ")
    logger.info(f"Renaming exiting complaint id column of dynamodb ")
    existing_complaint_spark_df = dyf_sparkdf.select("complaint_id").withColumnRenamed("complaint_id","existing_complaint_id")
    logger.info(f"Applying left join on new dataframe from s3 and dynamo db ")
    joined_sparkdf = df_sparkdf.join(existing_complaint_spark_df,df_sparkdf.complaint_id==existing_complaint_spark_df.existing_complaint_id,"left")
    logger.info(f"Number of row after left join : {joined_sparkdf.count()}")
    new_sparkdf = joined_sparkdf.filter("existing_complaint_id is null")
    new_sparkdf.drop("existing_complaint_id")
    new_sparkdf=new_sparkdf.coalesce(10)
else:
    new_sparkdf=df_sparkdf.coalesce(10)

logger.info(f"Converting spark dataframe to DynamicFrame")
newDynamicFrame= DynamicFrame.fromDF(new_sparkdf, glueContext, "new_sparkdf")
logger.info(f"Started writing new records into dynamo db dataframe.")
logger.info(f"Number of records will be written to dynamodb: {new_sparkdf.count()}")
glueContext.write_dynamic_frame_from_options(
    frame=newDynamicFrame,
    connection_type="dynamodb",
    connection_options={"dynamodb.output.tableName": DYNAMODB_TABLE_NAME,
        "dynamodb.throughput.write.percent": "1.0"
    }
)

logger.info(f"Data has been dumped into dynamodb ")
logger.info(f"Archiving file from inbox source: s3://{BUCKET_NAME}/inbox  to archive: s3://{BUCKET_NAME}/archive ")
os.system(f"aws s3 sync s3://{BUCKET_NAME}/inbox s3://{BUCKET_NAME}/archive")

logger.info(f"File is successfully archived.")
os.system(f"aws s3 rm s3://{BUCKET_NAME}/inbox/ --recursive")
    
job.commit()