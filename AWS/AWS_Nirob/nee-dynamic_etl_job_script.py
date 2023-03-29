import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from awsglue.dynamicframe import DynamicFrame



args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# read data from s3 >> nee-s3/input-nee-data/

dynamic_frame = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={"paths": ["s3://nee-s3/input-nee-data/"], "recurse": True},
    transformation_ctx="S3bucket_node1",
)

# Convert the Glue DynamicFrame to a Spark DataFrame
spark_df = dynamic_frame.toDF()


# Perform transformation on spark dataframe
spark_df = spark_df.withColumnRenamed("id", "candidate_ID").withColumnRenamed("rollno", "roll_no")
spark_df = spark_df.withColumn("score",  lit(100))
spark_df = spark_df.withColumn("company_name", lit('GrowthPaay'))


# Write the transformed data back to S3 using glueContext.write_dynamic_frame.from_options
glueContext.write_dynamic_frame.from_options(
    frame = DynamicFrame.fromDF(spark_df, glueContext, "spark_df"),
    connection_type = "s3",
    connection_options = {"path": "s3://nee-s3/nee-glue-etl-output-bucket/"},
    format = "parquet",
    transformation_ctx = "write_dynamic_frame"
)


job.commit()
