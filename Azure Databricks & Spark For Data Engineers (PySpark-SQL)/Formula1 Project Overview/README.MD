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

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumnRenamed.html#pyspark.sql.DataFrame.withColumnRenamed


circuits_renamed_df =  circuits_selected_df.withColumnRenamed("circuitId","circuit_id") \
                       .withColumnRenamed("circuitRef","circuit_ref") \
                       .withColumnRenamed("lat","latitude") \
                       .withColumnRenamed("lng","longitude") \
                       .withColumnRenamed("alt","altitude")


display(circuits_renamed_df)




60. Circuits File - WithColumn

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.withColumns.html#pyspark.sql.DataFrame.withColumns

step -4 Add ingestion data to Dataframe
from pyspark.sql.functions import current_timestamp, lit #we can use lit function as well to show default values

from pyspark.sql.functions import current_timestamp


circuits_final_df = circuits_renamed_df.withColumn('ingestion_date',current_timestamp()).withColumn('env',lit("Production"))

circuits_final_df = circuits_renamed_df.withColumn('ingestion_date',current_timestamp())

display(circuits_final_df)



61. Circuits File - Dataframe Writer

write data to datalake as parquet format

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.parquet.html#pyspark.sql.DataFrameWriter.parquet


circuits_final_df.write.mode("overwrite").parquet('/mnt/formula1dlajay/processed/circuits') #to avoide error from rerun we use mode

%fs
ls /mnt/formula1dlajay/processed/circuits


# df = spark.read.parquet('dbfs:/mnt/formula1dlajay/processed/circuits/')
# display(df)
display(spark.read.parquet('dbfs:/mnt/formula1dlajay/processed/circuits/'))

62. Races File - Requirements

https://ergast.com/docs/f1db_user_guide.txt


from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

races_schema = StructType(fields=[StructField('raceId',IntegerType(),False),
                                     StructField('year',IntegerType(),True),
                                     StructField('round',IntegerType(),True),
                                     StructField('circuitId',IntegerType(),True),
                                     StructField('name',StringType(),True),
                                     StructField('date',DateType(),True),
                                     StructField('time',StringType(),True),
                                     StructField('url',StringType(),True)])

races_df = spark.read.option("header",True).schema(races_schema).csv('dbfs:/mnt/formula1dlajay/raw/races.csv')


display(races_df)


from pyspark.sql.functions import current_timestamp, to_timestamp,  concat, col, lit

races_with_timestamp_df = races_df.withColumn('ingestion_date',current_timestamp()) \
                          .withColumn('race_timestamp',to_timestamp(concat(col("date"), lit(" "), col("time")), "yyyy-MM-dd HH:mm:ss"))

display(races_with_timestamp_df)

races_selected_df = races_with_timestamp_df.select(col("raceId").alias("race_id"), col("year").alias("race_year"), col("round"), col("circuitId").alias("circuit_id"), col("name"), col("ingestion_date"), col("race_timestamp") )

races_selected_df.write.mode("overwrite").parquet('/mnt/formula1dlajay/processed/races')



64. Races File - Partitioning

partitionBy 'race_year'

races_selected_df.write.mode("overwrite").partitionBy("race_year").parquet('/mnt/formula1dlajay/processed/races')

display(spark.read.parquet('/mnt/formula1dlajay/processed/races'))



##########################################
section -12 Data Ingestion - JSON


65. Constructors File - Requirements

json -> read -> transform -> write -> parquet

data ingestion json



66. Constructors File - Read Data

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.schema.html

constructor_schema = "constructorId INT,constructorRef string,name string, nationality string, url string"
construct_df = spark.read.schema(constructor_schema).json('/mnt/formula1dlajay/raw/constructors.json/')
construct_df.printSchema()
display(construct_df)


67. Constructors File - Transform & Write Data

from pyspark.sql.functions import col
constructor_dropped_df = construct_df.drop(col('url'))


from pyspark.sql.functions import current_timestamp

constructor_renamed_df = constructor_dropped_df.withColumnRenamed("constructorId","constructor_id") \
                                               .withColumnRenamed("constructorRef","constructor_ref") \
                                               .withColumn("ingestion_date",current_timestamp())

display(constructor_renamed_df)

constructor_renamed_df.write.mode('overwrite').parquet('/mnt/formula1dlajay/processed/constructors')




68. Drivers File - Requirements

driver.json file

concatenate firstname,lastname and ingest date and rename columns


69. Drivers File - Spark Program


from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

name_schema = StructType(fields=[StructField("forename",StringType(),True),
                                 StructField("surname",StringType(),True) 
                        ])

driver_schema = StructType(fields=[StructField("driverId",IntegerType(),False),
                                StructField("driverRef",StringType(),True),
                                StructField("number",IntegerType(),True),
                                StructField("code",StringType(),True),
                                StructField("name",name_schema) ,
                                StructField("dob",DateType(),True),
                                StructField("nationality",StringType(),True),
                                StructField("url",StringType(),True),      
                        ])

driver_df = spark.read.schema(driver_schema).json('/mnt/formula1dlajay/raw/drivers.json')

driver_rename_df = driver_df.withColumnRenamed("driverId","driver_id") \
                            .withColumnRenamed("driverRef","driver_ref") \
                            .withColumn("ingestion_date",current_timestamp()) \
                            .withColumn("name", concat(col("name.forename"),lit(" "),col("name.surname")))  

driver_final_df = driver_rename_df.drop("url")

display(spark.read.parquet('/mnt/formula1dlajay/processed/drivers'))




70. Results File - Requirements

data ingestion of results.json file - assignment

https://ergast.com/docs/f1db_user_guide.txt



71. Results File - Spark Program (Assignment)

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType

results_schema = StructType(fields=[StructField("resultId", IntegerType(), False),
                                    StructField("raceId", IntegerType(), True),
                                    StructField("driverId", IntegerType(), True),
                                    StructField("constructorId", IntegerType(), True),
                                    StructField("number", IntegerType(), True),
                                    StructField("grid", IntegerType(), True),
                                    StructField("position", IntegerType(), True),
                                    StructField("positionText", StringType(), True),
                                    StructField("positionOrder", IntegerType(), True),
                                    StructField("points", FloatType(), True),
                                    StructField("laps", IntegerType(), True),
                                    StructField("time", StringType(), True),
                                    StructField("milliseconds", IntegerType(), True),
                                    StructField("fastestLap", IntegerType(), True),
                                    StructField("rank", IntegerType(), True),
                                    StructField("fastestLapTime", StringType(), True),
                                    StructField("fastestLapSpeed", FloatType(), True),
                                    StructField("statusId", StringType(), True)])

results_df = spark.read \
.schema(results_schema) \
.json("/mnt/formula1dlajay/raw/results.json")

from pyspark.sql.functions import current_timestamp


results_with_columns_df = results_df.withColumnRenamed("resultId", "result_id") \
                                    .withColumnRenamed("raceId", "race_id") \
                                    .withColumnRenamed("driverId", "driver_id") \
                                    .withColumnRenamed("constructorId", "constructor_id") \
                                    .withColumnRenamed("positionText", "position_text") \
                                    .withColumnRenamed("positionOrder", "position_order") \
                                    .withColumnRenamed("fastestLap", "fastest_lap") \
                                    .withColumnRenamed("fastestLapTime", "fastest_lap_time") \
                                    .withColumnRenamed("fastestLapSpeed", "fastest_lap_speed") \
                                    .withColumn("ingestion_date", current_timestamp()) 

from pyspark.sql.functions import col

results_final_df = results_with_columns_df.drop(col("statusId"))

results_final_df.write.mode("overwrite").partitionBy('race_id').parquet("/mnt/formula1dl/processed/results")



72. Pitstops File - Requirements

pitstops file

73. Pitstops File - Spark Program

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType

pit_stops_schema = StructType(fields=[StructField("raceId", IntegerType(), False),
                                    StructField("driverId", IntegerType(), True),
                                    StructField("stop", StringType(), True),
                                    StructField("lap", IntegerType(), True),
                                    StructField("time", StringType(), True),                                                                      
                                    StructField("duration", StringType(), True),
                                    StructField("milliseconds", IntegerType(), True)
                                    ])

pit_stops_df = spark.read \
.schema(pit_stops_schema) \
.option("multiLine",True) \ # for multiline
.json("/mnt/formula1dlajay/raw/pit_stops.json")

display(pit_stops_df)

from pyspark.sql.functions import current_timestamp


pit_stops_with_columns_df = pit_stops_df.withColumnRenamed("raceId", "race_id") \
                                    .withColumnRenamed("driverId", "driver_id") \
                                    .withColumn("ingestion_date", current_timestamp())


display(pit_stops_with_columns_df)

pit_stops_with_columns_df.write.mode("overwrite").parquet("/mnt/formula1dlajay/processed/pit_stops")

display(spark.read.parquet('/mnt/formula1dlajay/processed/pit_stops'))


#########################################################
Section -13 -Data Ingestion - Multiple Files

74. Lap Times - Requirements


multiple files ingesion from lap_times folder

75. Lap Times - Spark Program


from pyspark.sql.types import StructType, StructField, IntegerType, StringType

lap_times_schema = StructType(fields=[StructField("raceId", IntegerType(), False),
                                    StructField("driverId", IntegerType(), True),
                                    StructField("lap", IntegerType(), True),
                                    StructField("position", IntegerType(), True),
                                    StructField("time", StringType(), True),                                                                      
                                    StructField("milliseconds", IntegerType(), True)                                    
                                    ])

lap_times_schema_df = spark.read \
.schema(lap_times_schema) \
.csv("/mnt/formula1dlajay/raw/lap_times")   #/mnt/formula1dlajay/raw/lap_times/lap_times*.csv we can use like this

lap_times_schema_df.count()


display(lap_times_schema_df)

from pyspark.sql.functions import current_timestamp

lap_times_with_columns_df = lap_times_schema_df.withColumnRenamed("raceId", "race_id") \
                                    .withColumnRenamed("driverId", "driver_id") \
                                    .withColumn("ingestion_date", current_timestamp())

lap_times_with_columns_df.write.mode("overwrite").parquet("/mnt/formula1dlajay/processed/lap_times")

display(spark.read.parquet('/mnt/formula1dlajay/processed/lap_times'))


76. Qualifying - Requirements

dataingestion_qualifying

77. Qualifying - Spark Program (Assignment)

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

qualifying_schema = StructType(fields=[StructField("qualifyId", IntegerType(), False),
                                    StructField("raceId", IntegerType(), True),
                                    StructField("driverId", IntegerType(), True),
                                    StructField("constructorId", IntegerType(), True),
                                    StructField("number", IntegerType(), True),                                                                      
                                    StructField("position", IntegerType(), True),
                                    StructField("q1", StringType(), True),
                                    StructField("q2", StringType(), True),
                                    StructField("q3", StringType(), True),
                                    ])

qualifying_df = spark.read \
.schema(qualifying_schema) \
.option("multiLine",True) \
.json("/mnt/formula1dlajay/raw/qualifying")

from pyspark.sql.functions import current_timestamp

qualifying_with_columns_df = qualifying_df.withColumnRenamed("raceId", "race_id") \
                                    .withColumnRenamed("driverId", "driver_id") \
                                    .withColumnRenamed("qualifyId", "qualify_id") \
                                    .withColumnRenamed(" constructorId", "constructor_id") \
                                    .withColumn("ingestion_date", current_timestamp())


qualifying_with_columns_df.write.mode("overwrite").parquet("/mnt/formula1dlajay/processed/qualifying")



#####################################

section 14 - Databricks Workflow


78. Section Overview

overall flow

79. Including a Child Notebook

configuration:

raw_folder_path = '/mnt/formula1dlajay/raw'
processed_folder_path = '/mnt/formula1dlajay/processed'
presentation_folder_path = '/mnt/formula1dlajay/presentation'

common_functions:

from pyspark.sql.functions import current_timestamp
def add_ingestion_date(input_df):
  output_df = input_df.withColumn("ingestion_date", current_timestamp())
  return output_df


%run "../includes/configuration"

%run "../includes/common_functions"

circuits_df = spark.read.option("header",True).schema(circuits_schema).csv(f'{raw_folder_path}/circuits.csv')

circuits_final_df.write.mode("overwrite").parquet('{processed_folder_path}/circuits') #to avoide error from rerun we use mode


circuits_final_df = add_ingestion_date(circuits_renamed_df)

circuits_final_df.write.mode("overwrite").parquet(f'{processed_folder_path}/circuits') #to avoide error from rerun we use mode

display(spark.read.parquet(f'{processed_folder_path}/circuits/'))



80. Passing Parameters to Notebooks

we can pass parameters with the help of widgets in new column

dbutils.widgets.help()

dbutils.widgets.text("p_data_source","")
v_data_source = dbutils.widgets.get("p_data_source")


v_data_source


from pyspark.sql.functions import lit

circuits_renamed_df =  circuits_selected_df.withColumnRenamed("circuitId","circuit_id") \
                       .withColumnRenamed("circuitRef","circuit_ref") \
                       .withColumnRenamed("lat","latitude") \
                       .withColumnRenamed("lng","longitude") \
                       .withColumnRenamed("alt","altitude") \
                       .withColumn("data_source",lit(v_data_source))




81. Notebook Workflows

https://docs.databricks.com/en/notebooks/notebook-workflows.html
Run multiple notebooks concurrently


0.ingest_all_files

dbutils.notebook.help()

v_result = dbutils.notebook.run('1.ingest_circuits_file',0,{"p_data_source":"Ergast API"})
v_result

v_result = dbutils.notebook.run('2.ingest_race_file',0,{"p_data_source":"Ergast API"})
v_result


we did same for all 8 files


82. Databricks Jobs

https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#job/list

creating job cluster
go to job and create inside databricks

select - single user and single node
node type - standard 14gp 4cpu core

job name - 'F1 Job'
cluster name -'F1_Job_cluster'


Path - /Formula1/ingestion_with_includes/1.ingest_circuits_file
Parameters - p_data_source  - E API

databricks_job_cluster2


job-run2




job task edit and then change path and remove parameter

Path - /Formula1/ingestion_with_includes/0.ingest_all_files

Parameters -  remove paramter
