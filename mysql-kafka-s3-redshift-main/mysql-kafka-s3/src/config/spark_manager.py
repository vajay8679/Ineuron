from pyspark.sql import SparkSession
from .environment import EnvironmentVariable
env = EnvironmentVariable()
spark_session =(SparkSession.builder.master('local[*]').appName('bigdata') 
.config("spark.executor.instances", "1") 
.config("spark.executor.memory", "6g") 
.config("spark.driver.memory", "6g") 
.config("spark.executor.memoryOverhead", "8g")
.config('spark.jars.packages',"org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,mysql:mysql-connector-java:8.0.11,com.amazonaws:aws-java-sdk:1.12.346,org.apache.hadoop:hadoop-aws:3.2.2,com.google.guava:guava:31.1-jre,org.apache.httpcomponents:httpcore:4.4.15")
.getOrCreate())
spark_session.sparkContext.setSystemProperty('com.amazonaws.services.s3.enableV4', 'true')
##backup of previous running jar
##.config('spark.jars.packages',"org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,mysql:mysql-connector-java:8.0.11")\
accessKeyId=env.aws.access_key_id
secretAccessKey=env.aws.secret_access_key
spark_session._jsc.hadoopConfiguration().set("fs.s3a.access.key", env.aws.access_key_id)
spark_session._jsc.hadoopConfiguration().set("fs.s3a.secret.key", env.aws.secret_access_key)
spark_session._jsc.hadoopConfiguration().set('fs.s3a.endpoint', 's3-ap-south-1.amazonaws.com')
spark_session._jsc.hadoopConfiguration().set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
spark_session._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "com.amazonaws.auth.EnvironmentVariableCredentialsProvider")
# spark_session._jsc.hadoopConfiguration().set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")

# # spark_session._jsc.hadoopConfiguration().set("fs.s3a.impl","org.apache.hadoop.fs.s3native.NativeS3FileSystem")
# # spark_session._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
# # spark_session._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")
# # spark_session._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider","com.amazonaws.auth.EnvironmentVariableCredentialsProvider")
# spark_session._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "ap-south-1.amazonaws.com")
# # spark_session._jsc.hadoopConfiguration().set("fs.s3.buffer.dir","tmp")


# .config("spark.executor.instances", "1") 
#     .config("spark.executor.memory", "6g") 
#     .config("spark.driver.memory", "6g") 
#     .config("spark.executor.memoryOverhead", "8g")
#     .config("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem") 
#     .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
#     # .config('spark.jars.packages',"com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.3")

# import pyspark
# from pyspark.sql import SparkSession
# from pyspark import SparkContext, SparkConf
# from .environment import EnvironmentVariable
# env = EnvironmentVariable()
# conf = SparkConf()\
# .set('spark.executor.extraJavaOptions','com.amazonaws.services.s3.enableV4=true')\
#  .set('spark.driver.extraJavaOptions','com.amazonaws.services.s3.enableV4=true')\
#  .set("spark.executor.memoryOverhead", "8g")\
#  .setAppName('pyspark_aws').setMaster('local[*]')
# sc=SparkContext(conf=conf)
# sc.setSystemProperty('com.amazonaws.services.s3.enableV4', 'true')
# print('modules imported')

# accessKeyId=env.aws.access_key_id
# secretAccessKey=env.aws.secret_access_key
# hadoopConf = sc._jsc.hadoopConfiguration()
# hadoopConf.set('fs.s3a.access.key', accessKeyId)
# hadoopConf.set('fs.s3a.secret.key', secretAccessKey)
# hadoopConf.set('fs.s3a.endpoint', 's3-ap-south-1.amazonaws.com')
# hadoopConf.set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
# hadoopConf.set("fs.s3a.aws.credentials.provider", "com.amazonaws.auth.EnvironmentVariableCredentialsProvider")
# spark_session=SparkSession(sc)

# spark-submit --packages com.amazonaws:aws-java-sdk:1.12.346,org.apache.hadoop:hadoop-aws:3.2.2,com.google.guava:guava:31.1-jre,org.apache.httpcomponents:httpcore:4.4.15 demo.py