import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1681042111162 = glueContext.create_dynamic_frame.from_options(
    format_options={},
    connection_type="s3",
    format="parquet",
    connection_options={"paths": ["s3://project-nee/raw_data/"], "recurse": True},
    transformation_ctx="AmazonS3_node1681042111162",
)

# Script generated for node Select Fields
SelectFields_node1681042172413 = SelectFields.apply(
    frame=AmazonS3_node1681042111162,
    paths=["name", "id"],
    transformation_ctx="SelectFields_node1681042172413",
)

# Cast "name" column to string
resolved_frame = SelectFields_node1681042172413.resolveChoice(specs=[('name','cast:string')])

# Cast "id" column to integer
resolved_frame = resolved_frame.withColumn("id", resolved_frame["id"].cast("int"))

# Script generated for node Amazon S3
AmazonS3_node1681042307291 = glueContext.write_dynamic_frame.from_options(
    frame=resolved_frame,
    connection_type="s3",
    format="parquet",
    connection_options={"path": "s3://project-nee/curated_data/", "partitionKeys": []},
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1681042307291",
)

job.commit()
