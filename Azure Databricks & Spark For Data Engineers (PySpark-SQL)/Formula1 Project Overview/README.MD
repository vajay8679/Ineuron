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



############################################
section -15 Filters and Join Transformations


83. Section Overview



84. Filter Transformation

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.filter.html#pyspark.sql.DataFrame.filter




85. Join Transformation - Inner Join

%run "../includes/configuration"

demo_df = spark.read.parquet(f"{processed_folder_path}/races")

demo_filter_df = demo_df.filter("race_year = 2019 and round <= 5")

demo_filter_df = demo_df.filter((demo_df["race_year"] == 2019) & (demo_df["round"] <= 5))

demo_filter_df = demo_df.where((demo_df["race_year"] == 2019) & (demo_df["round"] <= 5))

display(demo_filter_df)


85. Join Transformation - Inner Join

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.join.html#pyspark.sql.DataFrame.join

%run "../includes/configuration"

races_df = spark.read.parquet(f"{processed_folder_path}/races").filter("race_year = 2019").withColumnRenamed("name","race_name")

circuits_df = spark.read.parquet(f"{processed_folder_path}/circuits").withColumnRenamed("name","circuit_name")

races_circuits_df = circuits_df.join(races_df, circuits_df.circuit_id == races_df.circuit_id,"inner") \
    .select(circuits_df.circuit_name,circuits_df.location,circuits_df.country,races_df.race_name,races_df.round)

display(races_circuits_df)


races_circuits_df.select("circuit_name").show()


86. Join Transformation - Outer Join

#left outer join
races_circuits_df = circuits_df.join(races_df, circuits_df.circuit_id == races_df.circuit_id,"left") \
    .select(circuits_df.circuit_name,circuits_df.location,circuits_df.country,races_df.race_name,races_df.round)

#right outer join
races_circuits_df = circuits_df.join(races_df, circuits_df.circuit_id == races_df.circuit_id,"right") \
    .select(circuits_df.circuit_name,circuits_df.location,circuits_df.country,races_df.race_name,races_df.round)

#full outer join
races_circuits_df = circuits_df.join(races_df, circuits_df.circuit_id == races_df.circuit_id,"full") \
    .select(circuits_df.circuit_name,circuits_df.location,circuits_df.country,races_df.race_name,races_df.round)



87. Join Transformation - Semi, Anti & Cross Joins

#semi - similar to inner join but only takes column from left left table
races_circuits_df = circuits_df.join(races_df, circuits_df.circuit_id == races_df.circuit_id,"semi") \
    .select(circuits_df.circuit_name,circuits_df.location,circuits_df.country)


#Anti Join - it is opposite of semi join - it will give data from opposite dataframe
races_circuits_df = races_df.join(circuits_df, circuits_df.circuit_id == races_df.circuit_id,"anti") 

#cross join - each record from left table join with every record from right tale
races_circuits_df = races_df.crossJoin(circuits_df)


88. Join Race Results - Requirement

joins four tables columns data


89. Set-up Presentation Layer (Assignment)

check this -> 8.mount_adls_container_for_project


90. Join Race Results - Solution (Assignment)

join_race_result image

joints_tables images

we have connected five table here

https://www.bbc.com/sport/formula1/2020/results

file - race_results

%run "../includes/configuration"

drivers_df = spark.read.parquet(f"{processed_folder_path}/drivers") \
    .withColumnRenamed("number","driver_number") \
    .withColumnRenamed("name","driver_name") \
    .withColumnRenamed("nationality", "driver_nationality")

constructors_df = spark.read.parquet(f"{processed_folder_path}/constructors") \
        .withColumnRenamed("name", "team")

circuits_df = spark.read.parquet(f"{processed_folder_path}/circuits") \
        .withColumnRenamed("location", "circuit_location")

races_df = spark.read.parquet(f"{processed_folder_path}/races") \
        .withColumnRenamed("name", "race_name") \
        .withColumnRenamed("race_timestamp", "race_date")

results_df = spark.read.parquet(f"{processed_folder_path}/results") \
        .withColumnRenamed("time", "race_time")

circuits_races_df = races_df.join(circuits_df, circuits_df.circuit_id == races_df.circuit_id,"inner") \
    .select(races_df.race_id, races_df.race_year, races_df.race_name, races_df.race_date, circuits_df.circuit_location)

race_result_df = results_df.join(circuits_races_df, circuits_races_df.race_id == results_df.race_id) \
    .join(constructors_df, constructors_df.constructor_id == results_df.constructor_id) \
    .join(drivers_df, drivers_df.driver_id == results_df.driver_id)

from pyspark.sql.functions import current_timestamp

final_df = race_result_df.select("race_year","race_name","race_date","circuit_location","driver_name","driver_number","driver_nationality",
                                "team","grid","fastest_lap","race_time","points") \
                                .withColumn("created_date",current_timestamp())

display(final_df.filter("race_year == 2020 and race_name == 'Abu Dhabi Grand Prix'").orderBy(final_df.points.desc()))


final_df.write.mode("overwrite").parquet(f"{presentation_folder_path}/race_result")




########################################################

section - 16 Aggregations


91. Section Overview



92. Simple Aggregate functions

aggregation_demo file


%run "../includes/configuration"

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_result")

demo_df = race_result_df.filter("race_year == 2020")

from pyspark.sql.functions import count, countDistinct, sum

demo_df.select(count("*")).show()

demo_df.select(count("race_name")).show()

demo_df.select(countDistinct("race_name")).show()

demo_df.select(sum("points")).show()

demo_df.filter("driver_name = 'Lewis Hamilton'").select(sum("points")).show()

demo_df.filter("driver_name = 'Lewis Hamilton'").select(sum("points"),countDistinct("race_name")).show()

demo_df.filter("driver_name = 'Lewis Hamilton'").select(sum("points"),countDistinct("race_name")).withColumnRenamed("sum(points)","sum_points") \
    .withColumnRenamed("count(DISTINCT race_name)","distinct_race_name").show()


93. Group By

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/grouping.html

#group by -> multiple column in groupby using agg()

demo_df \
    .groupBy("driver_name") \
    .agg(sum("points").alias("total_point"),countDistinct("race_name").alias("number_of_races")) \
    .show()


94. Window Functions

https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/window.html


demo_grouped_df = demo_df \
    .groupBy("race_year","driver_name") \
    .agg(sum("points").alias("total_point"),countDistinct("race_name").alias("number_of_races"))


from pyspark.sql.window import Window
from pyspark.sql.functions import desc, rank

driverRankSpec = Window.partitionBy("race_year").orderBy(desc("total_point"))

demo_grouped_df.withColumn("rank",rank().over(driverRankSpec)).show(100)


95. Driver Standings

https://www.bbc.com/sport/formula1/drivers-world-championship/standings

results table

2.driver_standings - file


%run "../includes/configuration"

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_result")

display(race_result_df)

from pyspark.sql.functions import sum, count, when, col

driver_standings_df = race_result_df \
    .groupBy("race_year","driver_name","driver_nationality","team") \
    .agg(sum("points").alias("total_points"),count(when(col("position") == 1, True)).alias("wins"))

display(driver_standings_df.filter("race_year == 2020"))


from pyspark.sql.window import Window
from pyspark.sql.functions import desc, rank, asc
driver_rank_spec = Window.partitionBy("race_year").orderBy(desc("total_points"),desc("wins"))
final_df = driver_standings_df.withColumn("rank",rank().over(driver_rank_spec))

display(final_df.filter("race_year == 2020"))

final_df.write.mode("overwrite").parquet(f"{presentation_folder_path}/driver_standings")



96. Constructor Standings (Assignment)


https://www.bbc.com/sport/formula1/constructors-world-championship/standings

3.constructor_standings - file

%run "../includes/configuration"

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_result")

from pyspark.sql.functions import sum, count, when, col

constructor_standings_df = race_result_df \
    .groupBy("race_year","team") \
    .agg(sum("points").alias("total_points"),count(when(col("position") == 1, True)).alias("wins"))

display(constructor_standings_df.filter("race_year == 2020"))

from pyspark.sql.window import Window
from pyspark.sql.functions import desc, rank, asc
constructor_rank_spec = Window.partitionBy("race_year").orderBy(desc("total_points"),desc("wins"))
final_df = constructor_standings_df.withColumn("rank",rank().over(constructor_rank_spec))

display(final_df.filter("race_year == 2020"))

final_df.write.mode("overwrite").parquet(f"{presentation_folder_path}/constructor_standings")



####################################################

section - 17 - Using SQL in Spark Application


97. Local Temp View

Access dataframes using SQL

%run "../includes/configuration"

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_result")

race_result_df.createTempView("v_race_result") #it is temporary table we ca not use in other notebook or if we detech and attach cluster again then below query wont run

race_result_df.createOrReplaceTempView("v_race_result") #use this in place of createTempView because if table exists then it will replace or either create


%sql
select * from v_race_result where race_year = 2020;

%sql
select count(1) from v_race_result where race_year = 2020;

p_race_year = 2020

#we can pass variable in this kind of query and we can use dataframe for further use but we can not do this in above query
race_result_2019_df = spark.sql(f"select * from v_race_result where race_year = {p_race_year}")


display(race_result_2019_df)




98. Global Temp View

Global Temporary Views

Create global temporary views on dataframes
Access the view from SQL cell
Access the view from Python cell
Acesss the view from another notebook


race_result_df.createOrReplaceGlobalTempView("gv_race_result") # we can use this table from other notebook and even after attached and detech cluster and still it will work from other notebook

%sql
SHOW TABLES in global_temp;

%sql
select * from global_temp.gv_race_result;

spark.sql("select * from global_temp.gv_race_result").show()


we can not run from other notebook 

%sql
select * from v_race_result;


we can run from other notebook 

%sql
select * from global_temp.gv_race_result;



#######################################################

Section - 18 - Spark SQL - Databases/Tables/Views



99. Spark SQL - Introduction


hive_meta_store image


spark_table_view image



100. Databases

https://spark.apache.org/docs/latest/api/python/reference/index.html


https://spark.apache.org/docs/latest/sql-ref-syntax.html


create database if not exists demo;
show databases;
describe database demo;
describe database extended demo;
select current_database();
show tables in demo;
show tables;




101. Managed Tables


Managed Tables
Type MANAGED
Location dbfs:/user/hive/warehouse/demo.db/race_result_sql

Create managed table using Python

%run "../includes/configuration"

%python
race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_result")


%python
race_result_df.write.format("parquet").saveAsTable("demo.race_result_python")


use demo;
show tables;

desc extended race_result_python;

select * from demo.race_result_python where race_year = 2020;


Create managed table using SQL

create table demo.race_result_sql
as
select * from demo.race_result_python where race_year = 2020;

desc extended race_result_sql --this table is 'managed' table and location - dbfs:/user/hive/warehouse/demo.db/race_result_sql

drop table demo.race_result_sql; -- if we drop this table then it will delete table with metadata and all data as well

show tables in demo;


102. External Tables

External Tables
1. Create external table using Python


%python
race_result_df.write.format("parquet").option("path",f"{presentation_folder_path}/race_result_ext_py").saveAsTable("demo.race_result_ext_py")


desc extended demo.race_result_ext_py;

Type EXTERNAL
Provider parquet
Location dbfs:/mnt/formula1dlajay/presentation/race_result_ext_py


https://spark.apache.org/docs/latest/sql-ref-syntax-dml-insert-table.html


2.Create external table using SQL

CREATE TABLE demo.race_results_ext_sql
(race_year INT,
race_name STRING,
race_date TIMESTAMP,
circuit_location STRING,
driver_name STRING,
driver_number INT,
driver_nationality STRING,
team STRING,
grid INT,
fastest_lap INT,
race_time STRING,
points FLOAT,
position INT,
created_date TIMESTAMP
)
USING PARQUET
LOCATION '/mnt/formula1dlajay/presentation/race_results_ext_sql'


show tables in demo;

-- we have to insert data into external table then we will get data
insert into demo.race_results_ext_sql
select * from demo.race_result_ext_py where race_year = 2020;

select count(1) from demo.race_results_ext_sql;

show tables in demo;

drop table demo.race_results_ext_sql;

show tables in demo;


manage table - spark manage meta data as well as data
external table - spark manage only metadata and we manage data



103. Views

Views on tables

1. Create Temp View (temporary table)

create or replace temp view v_race_results
as
select * from demo.race_result_python
where race_year = 2018;

select * from v_race_results;



2. Create Global Temp View

create or replace global temp view gv_race_results
as 
select * from demo.race_result_python
where race_year = 2012;

select * from global_temp.gv_race_results; -- we can run this notebook from other notebook and detech and attach and read data from this table

show tables in global_temp;



3. Create Permanent View

create or replace view demo.pv_race_results
as 
select * from demo.race_result_python
where race_year = 2000;

show tables in demo;

select * from demo.pv_race_results;


temp view - we can use in current notebook in spark session only

global view - we can use it from other notebook and and attach and detech and work in same application and after that batch process or job if you dont need then use global view

permanent view - we can use it from other notebook and and attach and detech and work in application and it will stay even after application has been closed and we need to comeback and use it then we we have to create permanent view


104. Formula1 Project SQL Requirement

manage external table




105. Create Table - CSV Source


file name - 1.create_raw_tables

create database if not exists f1_raw;

1. Create circuit table

DROP table if exists f1_raw.circuits;
create table if not exists f1_raw.circuits(circuitId INT,
circuitRef STRING,
name STRING,
location STRING,
country STRING,
lat DOUBLE,
lng DOUBLE,
alt INT,
url STRING
)
USING csv
OPTIONS (path "/mnt/formula1dlajay/raw/circuits.csv", header true)

select * from f1_raw.circuits;


similar for races table




106. Create Table - JSON Source

Create constructors table
Single Line JSON
Simple structure

1.create_raw_tables -file


drop table if exists f1_raw.constructors;
create table if not exists f1_raw.constructors(
  constructorId INT, 
  constructorRef STRING, 
  name STRING, 
  nationality STRING, 
  url STRING
)
using json
options (path "/mnt/formula1dlajay/raw/constructors.json")


select * from f1_raw.constructors;


1.create_raw_tables -file

Create drivers table
Single Line JSON
Complex structure


drop table if exists f1_raw.drivers;
create table if not exists f1_raw.drivers(
  driverId INT, 
  driverRef STRING, 
  number INT, 
  code STRING, 
  name STRUCT<forename:STRING, surname:STRING>,
  dob DATE,
  nationality STRING,
  url STRING
)
using json
options (path "/mnt/formula1dlajay/raw/drivers.json")

select * from f1_raw.drivers;


1.create_raw_tables -file

Create results table
Single Line JSON
Simple structure

drop table if exists f1_raw.results;
create table if not exists f1_raw.results(
resultId INT,
raceId INT,
driverId INT,
constructorId INT,
number INT,grid INT,
position INT,
positionText STRING,
positionOrder INT,
points INT,
laps INT,
time STRING,
milliseconds INT,
fastestLap INT,
rank INT,
fastestLapTime STRING,
fastestLapSpeed FLOAT,
statusId STRING
)
using json
options (path "/mnt/formula1dl/raw/results.json")

select * from f1_raw.results;


Create pit stops table
Multi Line JSON
Simple structure


drop table if exists f1_raw.pit_stops;
create table if not exists f1_raw.pit_stops(
driverId INT,
duration STRING,
lap INT,
milliseconds INT,
raceId INT,
stop INT,
time STRING
)
using json
options (path "/mnt/formula1dl/raw/pit_stops.json", multiLine true) -- remember it is multiline


select * from f1_raw.pit_stops;



107. Create Table - Multi Files Source

1.create_raw_tables - file

Create tables for list of files

Create Lap Times Table
CSV file
Multiple files

drop table if exists f1_raw.lap_times;
create table if not exists f1_raw.lap_times(
raceId INT,
driverId INT,
lap INT,
position INT,
time STRING,
milliseconds INT
)
using csv
options (path "/mnt/formula1dlajay/raw/lap_times")

select count(1) from f1_raw.lap_times;

select * from f1_raw.lap_times;


Create Qualifying Table
JSON file
MultiLine JSON
Multiple files


drop table if exists f1_raw.qualifying;
create table if not exists f1_raw.qualifying(
constructorId INT,
driverId INT,
number INT,
position INT,
q1 STRING,
q2 STRING,
q3 STRING,
qualifyId INT,
raceId INT
)
using json
options (path "/mnt/formula1dlajay/raw/qualifying", multiLine true)

select count(1) from f1_raw.qualifying;

select * from f1_raw.qualifying;



108. Create Table - Parquet Source (Processed Data)

inside 

ingestion_with_includes/9.create_processed_database

create database if not exists f1_processed
location "/mnt/formula1dlajay/processed" -- we choose external path of database

desc database f1_processed;


ingestion_with_includes/1.ingest_circuits_file

step 5

circuits_final_df.write.mode("overwrite").format("parquet").saveAsTable("f1_processed.circuits")

%sql
select * from f1_processed.circuits;


do similar with all other files and folder as well to write data into processed_folder inside container


109. Create Table - Parquet Source (Presentation Data) - Assignment


trans/0.create_presentation_database

create database if not exists f1_presentation
location '/mnt/formula1dlajay/presentation' -- we choose external path of database

desc database f1_presentation


we write table for all 3 for presentation_folder for all3 folder database  'f1_presentation' -> 1.race_results & 2.driver_standings & 3.constructor_standings

final_df.write.mode("overwrite").format("parquet").saveAsTable("f1_presentation.race_results")

select * from f1_presentation.race_results;




#######################################################

section - 19 - Spark Sql - Filters/ Joins/ Aggregations

110. Section Overview


111. SQL DML Basics


demo/7.sql_basic_demo


show databases;
use f1_processed;
select * from f1_processed.drivers limit 10;
select * from f1_processed.drivers where nationality = "British" and dob >= "1990-01-01";
select name,dob as date_of_birth from f1_processed.drivers where nationality = "British" and dob >= "1990-01-01";
select name,dob from f1_processed.drivers where nationality = "British" and dob >= "1990-01-01" order by dob desc;
select * from f1_processed.drivers order by nationality asc, dob desc; 
select name, nationality, dob from f1_processed.drivers where (nationality = "British" and dob >= "1990-01-01") or nationality = 'Indian' order by dob desc;


112. SQL Simple Functions

demo/8.sql_functions_demo

https://spark.apache.org/docs/latest/api/sql/index.html

https://spark.apache.org/docs/latest/api/sql/index.html#max


use f1_processed;
select * from drivers;
select *, concat(driver_ref,'-',code)  as new_driver_ref from drivers;
select *, split(name, ' ') from drivers;
select *, split(name, ' ') [0] forename,split(name, ' ') [1] surname from drivers;
select *, current_timestamp() from drivers;
select *, date_format(dob, 'dd-MM-yyyy') from drivers;
select *, date_add(dob, 1) from drivers;





113. SQL Aggregates/ Window functions

demo/8.sql_functions_demo

use f1_processed;
select count(*) from drivers;
select max(dob) from drivers;
select * from drivers where dob ='2000-05-11';
select count(*) from drivers where nationality ="British";
select nationality, count(*) from drivers group by nationality order by nationality desc;
select nationality, count(*) from drivers group by nationality having count(*) >100 order by nationality desc;
select nationality, name, dob, rank() over (partition by nationality order by dob desc) as age_rank from drivers order by nationality, age_rank;


114. SQL Joins

demo/9.sql_joins_demo


inner join

select * from v_driver_standings_2018 d_2018 
  join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

left join

select * from v_driver_standings_2018 d_2018 
  left join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

right join

select * from v_driver_standings_2018 d_2018 
  right join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

full join

select * from v_driver_standings_2018 d_2018 
  full join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);


Semi Join
it is a inner join but it will give records from left table from the join only

select * from v_driver_standings_2018 d_2018 
  semi join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

Anti Join
we will get the data that didnot participate in 2020 from participant of 2018 race

select * from v_driver_standings_2018 d_2018 
  Anti join v_driver_standings_2020 d_2020 
    on (d_2018.driver_name = d_2020.driver_name);

Cross Join
each record from left table will join with each record from right table - n X m

select * from v_driver_standings_2018 d_2018 
  cross join v_driver_standings_2020 d_2020;



##################################################

section - 20 - Spark SQL - Analysis

115. Introduction


116. Create Race Results table

trans/4.calculated_race_result

use f1_processed;

select races.race_year,
       constructors.name as team_name,
       drivers.name as driver_name,
       results.position,
       results.points,
       11 - results.position as calculated_points
  from results
  join drivers on (drivers.driver_id = results.driver_id)
  join constructors on (constructors.constructor_id = results.constructor_id)
  join races on (races.race_id = results.race_id)
  where results.position <= 10;

#put above query in a table inside table in f1_presentation database

create table f1_presentation.calculated_race_results
using parquet
as
select races.race_year,
       constructors.name as team_name,
       drivers.name as driver_name,
       results.position,
       results.points,
       11 - results.position as calculated_points
  from f1_processed.results
  join f1_processed.drivers on (drivers.driver_id = results.driver_id)
  join f1_processed.constructors on (constructors.constructor_id = results.constructor_id)
  join f1_processed.races on (races.race_id = results.race_id)
  where results.position <= 10;

select * from f1_presentation.calculated_race_results;

117. Dominant Drivers - Analysis

analysis/1.find_dominant_drivers - file

select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
group by driver_name
having count(1) > 50
order by avg_points desc;


select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2011 and 2020
group by driver_name
having count(1) > 50
order by avg_points desc;

select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2001 and 2010
group by driver_name
having count(1) > 50
order by avg_points desc;




118. Dominant Teams - Analysis

analysis/2.find_dominant_teams

select team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
group by team_name
having count(1) > 100
order by avg_points desc;


select team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2011 and 2020
group by team_name
having count(1) > 100
order by avg_points desc;

select team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2001 and 2010
group by team_name
having count(1) > 100
order by avg_points desc;


119. Dominant Drivers - Visualisation

analysis/3.viz_dominant_drivers


create or replace temp view v_dominant_drivers
as
select driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points,
       rank() over(order by avg(calculated_points) desc) as driver_rank
from f1_presentation.calculated_race_results
group by driver_name
having count(1) > 50
order by avg_points desc;

#line graph
select race_year,
       driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where driver_name in (select driver_name from v_dominant_drivers where driver_rank <= 10 )
group by race_year, driver_name
order by race_year, avg_points desc;

#bar graph
select race_year,
       driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where driver_name in (select driver_name from v_dominant_drivers where driver_rank <= 10 )
group by race_year, driver_name
order by race_year, avg_points desc;


#areal graph
select race_year,
       driver_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where driver_name in (select driver_name from v_dominant_drivers where driver_rank <= 10 )
group by race_year, driver_name
order by race_year, avg_points desc;






120. Dominant Teams - Visualisation
