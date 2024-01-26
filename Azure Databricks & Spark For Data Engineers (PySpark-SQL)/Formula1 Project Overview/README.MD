#######################################
section -9  - Formula1 Project Overview


48. Formula1 Data Overview

https://ergast.com/mrd/




49. Upload Formula1 Data to Data Lake

upload from 'row' folder all 6 files and 2 folder into 'raw' container


50. Project Requirement Overview

dataingestionrequirement
transofrmdata
analysisrequiremnt
schedulingrequirement
otherrequirement


51. Solution Architecture Overview

https://learn.microsoft.com/en-gb/azure/architecture/solution-ideas/articles/azure-databricks-modern-analytics-architecture

https://www.databricks.com/solutions/data-engineering

https://learn.microsoft.com/en-us/azure/architecture/

https://www.databricks.com/blog

solutionarchitechture
Modern analytics architecture with Azure Databricks
databricksarchitecture


#######################################
section 10 - Spark Introduction


52. Spark Cluster Architecture

scaling - 
horizonal scaling - adding more worker node
vertical scaling -adding more core in the same machine 

clster has - 1driver , 1 or more worker node 
worker node has  4cpu core or more and it has slots where execution happens



53. Dataframe & Data Source API Overview

spark dataframe

data source (csv,json) -> Read (Data source API - DATA frame reader method) -> dataframe -> Trans( Dataframe API) -> Dataframe -> Write (Data source API - DATA frame writer method) -> Data sink(orc,parquet)    

################################################
Section - 11 - Data Ingestion - csv

54. Data Ingestion Overview


csv,json,xml -> read data(dataframe read api) -> transform data(Data frame api - data types, row, column, functions,window,grouping) -> write data(dataframe write api) -> parquet,avro,delta,jdbs


55. Circuits File - Requirements


csv -> read -> transform -> write -> parquet

rename columns, delete unnessary column and add required column and taking care of datatypes of columns

data ingestion circuits


56. Circuits File - Dataframe Reader

https://spark.apache.org/docs/latest/api/python/index.html

https://spark.apache.org/docs/latest/api/python/reference/index.html

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/io.html


display(dbutils.fs.mounts())

%fs
ls /mnt/formula1dlajay/raw

circuits_df = spark.read.option("header",True).csv('dbfs:/mnt/formula1dlajay/raw/circuits.csv')

circuits_df = spark.read.option("header",True).option("inferSchema",True).csv('dbfs:/mnt/formula1dlajay/raw/circuits.csv')


type(circuits_df)

circuits_df.show()

display(circuits_df)



57. Circuits File - Specify Schema


https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/data_types.html


from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

circuits_schema = StructType(fields=[StructField('circuitId',IntegerType(),False),
                                     StructField('circuitRef',StringType(),True),
                                     StructField('name',StringType(),True),
                                     StructField('location',StringType(),True),
                                     StructField('country',StringType(),True),
                                     StructField('lat',DoubleType(),True),
                                     StructField('lng',DoubleType(),True),
                                     StructField('alt',IntegerType(),True),
                                     StructField('url',StringType(),True)])

circuits_df = spark.read.option("header",True).schema(circuits_schema).csv('dbfs:/mnt/formula1dlajay/raw/circuits.csv')

display(circuits_df)


58. Circuits File - Select Columns

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.select.html



#1st way of selectiong column
circuits_selected_df = circuits_df.select("circuitId","circuitRef","name","location","country","lat","lng","alt")

#2nd way of selectiong column
circuits_selected_df = circuits_df.select(circuits_df.circuitId,circuits_df.circuitRef,circuits_df.name,circuits_df.location,circuits_df.country,circuits_df.lat,circuits_df.lng,circuits_df.alt)

#3rd way of selecting column
circuits_selected_df = circuits_df.select(circuits_df["circuitId"],circuits_df["circuitRef"],circuits_df["name"],circuits_df["location"],circuits_df["country"],circuits_df["lat"],circuits_df["lng"],circuits_df["alt"])


from pyspark.sql.functions import col

#4th way of selecting column
circuits_selected_df = circuits_df.select(col("circuitId"),col("circuitRef"),col("name"),col("location"),col("country"),col("lat"),col("lng"),col("alt"))

display(circuits_selected_df)


59. Circuits File - WithColumnRenamed

