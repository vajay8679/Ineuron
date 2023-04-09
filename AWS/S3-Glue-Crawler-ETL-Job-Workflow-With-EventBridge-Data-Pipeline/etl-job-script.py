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
job.init(args['JOB_NAME'],args)
empDf = glueContext.create_dynamic_frame.from_catalog(
       database = "ajay1-test",
       table_name = "ajay1ajay_input_athena",
       transformation_ctx = 's3_input_0'
    )
    
empDf.printSchema()
sparkEmpDf = empDf.toDF()
sparkEmpDf.show()
print(sparkEmpDf.count())

# df2 = sparkEmpDf.select("employee_id")
# df2.show()

job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()