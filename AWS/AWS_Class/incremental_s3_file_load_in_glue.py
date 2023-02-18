import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
empDf = glueContext.create_dynamic_frame.from_catalog(
        database="b1-glue-catalog-db",
        table_name="s3new_b1_athena_input_data",
        transformation_ctx = "s3_input_new"
        )
        
empDf.printSchema()
sparkEmpDf = empDf.toDF()
sparkEmpDf.show()
print(sparkEmpDf.count())

job.commit()
