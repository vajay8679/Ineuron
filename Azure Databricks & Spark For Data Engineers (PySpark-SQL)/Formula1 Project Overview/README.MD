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

analysis/4.viz_dominant_teams

create or replace temp view v_dominant_teams
as
select team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points,
       rank() over(order by avg(calculated_points) desc) as team_rank
from f1_presentation.calculated_race_results
group by team_name
having count(1) > 100
order by avg_points desc;

select * from v_dominant_teams;

select race_year,
       team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where team_name in (select team_name from v_dominant_teams where team_rank <= 5 )
group by race_year, team_name
order by race_year, avg_points desc;

select race_year,
       team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where team_name in (select team_name from v_dominant_teams where team_rank <= 5 )
group by race_year, team_name
order by race_year, avg_points desc;

select race_year,
       team_name,
       count(1) as total_race,
       sum(calculated_points) as total_points,
       avg(calculated_points) as avg_points
from f1_presentation.calculated_race_results
where team_name in (select team_name from v_dominant_teams where team_rank <= 5 )
group by race_year, team_name
order by race_year, avg_points desc;


121. Create dashboards - Drivers

analysis/3.viz_dominant_drivers

%python
html = """<h1 style="color:Black;text-align:center;font-family:Ariel">Report on Dominant Formula 1 drivers</h1>"""
displayHTML(html)

display in dashboard

https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#notebook/684797452523711/dashboard/3973152690777811/present

122. Create dashboards - Teams

analysis/4.viz_dominant_teams

%python
html = """<h1 style="color:Black;text-align:center;font-family:Ariel">Report on Dominant Formula 1 Teams</h1>"""
displayHTML(html)

https://adb-2860423160921495.15.azuredatabricks.net/?o=2860423160921495#notebook/3973152690777799/dashboard/3973152690777813/present



########################################

Section - 21 - Incremental Load

123. Section Overview



124. Data Loading Design Patterns


day 1- no difference in full load and incremental load

day1(race1) -> Ingestion -> Datalake(race1) -> Transformation -> Data Lake (Race1)
(full data)

for day2,day3 -> data will append in the data of day1



125. Formula1 Project Scenario

Scenario1 -.use full data in day1 and then incremental data from day two thatis not good

scenario2 -> use incremental data from day one that will ne better

we can replace this 4 files every week in our datalake because of less data -> circuits,races,constrcutors,drivers (full files) (data from all races)

Results, PitStops, LapTimes, Qualifying - we will receive and process the incremental data only from the weekend from this files (data only from the race)


current scenario - overwrite data from (raw,processed,presentation folder)

current scenario - create subfolders for races data in  (raw,processed,presentation folder) and then apply


126. Formula1 Project Data Set-up

download - incremental_load_data folder


we will do incremental load data so delete all folders from containers raw,processed, presentation folder

utils/1.prepare_for_incremental_load - file


drop database if exists f1_processed cascade;

create database if not exists f1_processed 
Location '/mnt/formula1dlajay/processed';

drop database if exists f1_presentation cascade;

create database if not exists f1_presentation 
Location '/mnt/formula1dlajay/presentation';


upload folders from 'incremental_load_data' in containers 'raw' folder



127. Full Refresh Implementation

#full load scenario

ingestion_with_includes/1.ingest_circuits_file - file name
ingestion_with_includes/1.ingest_races_file - file name
ingestion_with_includes/1.ingest_constructors_file - file name
ingestion_with_includes/1.ingest_drivers_file - file name


changes in above files - circuits,races,constructors,drivers  (full load scenario)

dbutils.widgets.text("p_file_date","2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")

v_file_date

circuits_df = spark.read.option("header",True).schema(circuits_schema).csv(f'{raw_folder_path}/{v_file_date}/circuits.csv')

circuits_renamed_df =  circuits_selected_df.withColumnRenamed("circuitId","circuit_id") \
                       .withColumnRenamed("circuitRef","circuit_ref") \
                       .withColumnRenamed("lat","latitude") \
                       .withColumnRenamed("lng","longitude") \
                       .withColumnRenamed("alt","altitude") \
                       .withColumn("data_source",lit(v_data_source)) \
                       .withColumn("file_date",lit(v_file_date))

%sql
select * from f1_processed.circuits;


128. Incremental Load - Method 1

files - Results,PitStops,LapTimes,Qualifying

ingestion_with_includes/5.ingest_results_file

spark.read.json("/mnt/formula1dlajay/raw/2021-03-21/results.json").createOrReplaceTempView("results_cutover")

%sql
select raceId, count(1) from results_cutover group by raceId order by raceId desc;

spark.read.json("/mnt/formula1dlajay/raw/2021-03-28/results.json").createOrReplaceTempView("results_w1")

%sql
select raceId, count(1) from results_w1 group by raceId order by raceId desc;

spark.read.json("/mnt/formula1dlajay/raw/2021-04-18/results.json").createOrReplaceTempView("results_w2")

%sql
select raceId, count(1) from results_w2 group by raceId order by raceId desc;


dbutils.widgets.text("p_file_date","2021-03-28")
v_file_date = dbutils.widgets.get("p_file_date")

results_df = spark.read \
.schema(results_schema) \
.json(f"{raw_folder_path}/{v_file_date}/results.json")

results_with_columns_df = results_df.withColumnRenamed("resultId", "result_id") \
                                    .withColumnRenamed("raceId", "race_id") \
                                    .withColumnRenamed("driverId", "driver_id") \
                                    .withColumnRenamed("constructorId", "constructor_id") \
                                    .withColumnRenamed("positionText", "position_text") \
                                    .withColumnRenamed("positionOrder", "position_order") \
                                    .withColumnRenamed("fastestLap", "fastest_lap") \
                                    .withColumnRenamed("fastestLapTime", "fastest_lap_time") \
                                    .withColumnRenamed("fastestLapSpeed", "fastest_lap_speed") \
                                    .withColumn("data_source", lit(v_data_source)) \
                                    .withColumn("file_date",lit(v_file_date))

results_final_df.write.mode("append").partitionBy('race_id').format("parquet").saveAsTable("f1_processed.results")


change date and we will get data but it will append duplicate data from previous run as well


https://spark.apache.org/docs/latest/sql-ref-syntax.html#dml-statements


drop partitions - https://spark.apache.org/docs/latest/sql-ref-syntax-ddl-alter-table.html

#method1

for race_id_list in results_final_df.select("race_id").distinct().collect(): #use for small data because collect() will store in driver node
    if (spark._jsparkSession.catalog().tableExists("f1_processed.results")):
      spark.sql(f"alter table f1_processed.results drop if exists partition (race_id = {race_id_list.race_id})")


129. Incremental Load - Method 2

ingestion_with_includes/5.ingest_results_file
#method2

spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")

results_final_df = results_final_df.select("result_id","driver_id","constructor_id","number","grid","position","position_text","position_order","points","laps","time","milliseconds","fastest_lap","rank","fastest_lap_time","fastest_lap_speed","data_source","file_date","ingestion_date","race_id")

if (spark._jsparkSession.catalog().tableExists("f1_processed.results")):
    results_final_df.write.mode("overwrite").insertInto("f1_processed.results")
else:
    results_final_df.write.mode("overwrite").partitionBy("race_id").format("parquet").saveAsTable("f1_processed.results")


%sql

select race_id, count(1) from f1_processed.results group by race_id order by race_id desc;


130. Incremental Load Improvements - Assignment

results_final_df.schema.names


131. Incremental Load Improvements - Solution

ingestion_with_includes/5.ingest_results_file


common_functions - file 
add below two functions  in above file

def re_arrange_columns(input_df,partition_column): #used from common functions files
    column_list = []
    for column_name in input_df.schema.names:
        if column_name != partition_column:
            column_list.append(column_name)
        column_list.append(partition_column)
    output_df = input_df.select(column_list)
    return output_df

def overwrite_partition(input_df, db_name, table_name, partition_column): #used from common functions files
  output_df = re_arrange_columns(input_df, partition_column)
  spark.conf.set("spark.sql.sources.partitionOverwriteMode","dynamic")
  if (spark._jsparkSession.catalog().tableExists(f"{db_name}.{table_name}")):
    output_df.write.mode("overwrite").insertInto(f"{db_name}.{table_name}")
  else:
    output_df.write.mode("overwrite").partitionBy(partition_column).format("parquet").saveAsTable(f"{db_name}.{table_name}")


and call above function inside file

ingestion_with_includes/5.ingest_results_file

overwrite_function(results_final_df, 'f1_processed', 'results', 'race_id')


132. Incremental Load - Notebook Workflows


ingestion_with_includes/0.ingest_all_files -file - file

and changes for 'p_file_date' in 6,7,8 files

dbutils.widgets.text("p_file_date", "2021-03-28")
v_file_date = dbutils.widgets.get("p_file_date")

for all date and all files

v_result = dbutils.notebook.run('8.ingest_qualifying_file',0,{"p_data_source":"Ergast API","p_file_date":"2021-03-21"})



133. Incremental Load - Race Results


trans/1.race_results -file

dbutils.widgets.text("p_file_date", "2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")  


%run "../includes/common_functions"

results_df = spark.read.parquet(f"{processed_folder_path}/results") \
        .filter(f"file_date = '{v_filer_date}'") \
        .withColumnRenamed("time", "race_time") \
        .withColumnRenamed("race_id","result_race_id") \
        .withColumnRenamed("file_date","result_file_date")

race_result_df = results_df.join(circuits_races_df, circuits_races_df.race_id == results_df.result_race_id) \
    .join(constructors_df, constructors_df.constructor_id == results_df.constructor_id) \
    .join(drivers_df, drivers_df.driver_id == results_df.driver_id)

final_df = race_result_df.select("race_id","race_year","race_name","race_date","circuit_location","driver_name","driver_number","driver_nationality",
                                "team","grid","fastest_lap","race_time","points","position","result_file_date") \
                                .withColumn("created_date",current_timestamp()) \
                                .witColumnRenamed("result_file_date","file_date")

overwrite_function(final_df, 'f1_presentation', 'race_results', 'race_id')


%sql

select * from f1_presentation.race_results where race_year = 2021;


AnalysisException: [INSERT_COLUMN_ARITY_MISMATCH.TOO_MANY_DATA_COLUMNS] Cannot write to `hive_metastore`.`f1_presentation`.`race_results`, the reason is too many data columns: Table columns: `race_year`, `race_name`, `race_date`, `circuit_location`, `driver_name`, `driver_number`, `driver_nationality`, `team`, `grid`, `fastest_lap`, `race_time`, `points`, `position`, `created_date`. Data columns: `race_year`, `race_name`, `race_date`, `circuit_location`, `driver_name`, `driver_number`, `driver_nationality`, `team`, `grid`, `fastest_lap`, `race_time`, `points`, `position`, `created_date`, `race_id`.

#drop table for above 

%sql
drop table f1_presentation.race_results;


134. Incremental Load - Driver Standings

trans/2.driver_standings -file


dbutils.widgets.text("p_file_date", "2021-03-21")
v_filer_date = dbutils.widgets.get("p_file_date")

%run "../includes/common_functions"

#Find the Race year for which the data is reprocessed
race_result_list = spark.read.parquet(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") \
    .select("race_year") \
    .distinct() \
    .collect()   

race_result_list

race_year_list = []
for race_year in race_result_list:
    race_year_list.append(race_year.race_year)
# print(race_year_list)


from pyspark.sql.functions import col

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))

overwrite_function(final_df, 'f1_presentation', 'driver_standings', 'race_year')


%sql

select * from f1_presentation.driver_standings;


135. Incremental Load - Constructor Standings (Assignment)


added below function in common_functions

def df_column_to_list(input_df, column_name):
    df_row_list = input_df.select(column_name) \
                        .distinct() \
                        .collect()
    column_value_list = [row[column_name] for row in df_row_list]
    return column_value_list

trans/2.driver_standings -file

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") 
  
race_year_list = df_column_to_list(race_result_df,"race_year")


from pyspark.sql.functions import col

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))


trans/3.constructor_standings

dbutils.widgets.text("p_file_date", "2021-03-21")
v_filer_date = dbutils.widgets.get("p_file_date")

%run "../includes/common_functions"

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") 

race_year_list = df_column_to_list(race_result_df,"race_year")

from pyspark.sql.functions import col

race_result_df = spark.read.parquet(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))


overwrite_function(final_df, 'f1_presentation', 'constructor_standings', 'race_year')


##########################################

Section - 22 - Delta Lake

136. Section Overview


137. Pitfalls of Data Lakes


pitfalls means drabacks of data lake- acid transactions, versioning, time travel, BI workloads,streaming and batch workloads


138. Data Lakehouse Architecture

lakehouse architecutre



139. Read & Write to Delta Lake

Delta_Lake/set-up/mount_adls_storage - file

#mount demo folder to adls first

# Databricks notebook source
storage_account_name = "formula1dlajay"
client_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-id")
tenant_id = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-tenant-id") 
client_secret = dbutils.secrets.get(scope = "formula1-scope" , key = "formula1-account-client-secret")

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{client_secret}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

def mount_adls(container_name):
  dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/{container_name}",
    extra_configs = configs)

mount_adls("demo")

dbutils.fs.ls("/mnt/formula1dlajay/demo")

# dbutils.fs.unmount("/mnt/formula1dlajay/demo")


Delta_Lake/set-up/10.delta_lake_demo

Write data to delta lake (managed table)
Write data to delta lake (external table)
Read data from delta lake (Table)
Read data from delta lake (File)


https://docs.delta.io/latest/index.html

https://docs.databricks.com/en/index.html

https://learn.microsoft.com/en-us/azure/databricks/delta/

#write to a table
https://docs.delta.io/latest/delta-batch.html#write-to-a-table

%sql

create database if not exists f1_demo
location '/mnt/formula1dlajay/demo'


result_df = spark.read.option('inferSchema',True).json('/mnt/formula1dlajay/raw/2021-03-28/results.json')

#Write data to delta lake (managed table)
result_df.write.format("delta").mode("overwrite").saveAsTable("f1_demo.results_managed")

%sql
select * from f1_demo.results_managed;

#Write data to delta lake (external table)
result_df.write.format("delta").mode("overwrite").save("/mnt/formula1dlajay/demo/results_external")

%sql
create table f1_demo.results_external
USING DELTA
location '/mnt/formula1dlajay/demo/results_external'


%sql
--Read data from delta lake (Table)
select * from f1_demo.results_external

#Read data from delta lake (File)
results_external_df = spark.read.format("delta").load('/mnt/formula1dlajay/demo/results_external')

display(results_external_df)

#partitioned by
result_df.write.format("delta").mode("overwrite").partitionBy("constructorId").saveAsTable("f1_demo.results_partitoned")


%sql
show partitions f1_demo.results_partitoned;


140. Updates and Deletes on Delta Lake

https://docs.delta.io/latest/delta-update.html#update-a-table

Update Delta Table
Delete From Delta Table

%sql
select * from f1_demo.results_managed;

%sql
--update using sql
update f1_demo.results_managed
  set points = 11 - position
where position <= 10

%sql
select * from f1_demo.results_managed;


#update using pythonic way

from delta.tables import DeltaTable
deltaTable = DeltaTable.forPath(spark, '/mnt/formula1dlajay/demo/results_managed')
# Declare the predicate by using a SQL-formatted string.
# deltaTable.update(condition = "position <= 10", set = { "points": "21 - position" })
deltaTable.update("position <= 10",{ "points": "21 - position" })

%sql
select * from f1_demo.results_managed;

%sql
delete from f1_demo.results_managed
where position > 10;

%sql
select * from f1_demo.results_managed;

#delete using pythonic way
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, '/mnt/formula1dlajay/demo/results_managed')
deltaTable.delete("points = 0");

%sql
select * from f1_demo.results_managed;



141. Merge/ Upsert to Delta Lake

Upsert using merge

drivers_day1_df = spark.read.option("inferSchema",True) \
    .json('/mnt/formula1dlajay/raw/2021-03-28/drivers.json') \
    .filter("driverId <= 10") \
    .select("driverId","dob","name.forename","name.surname")

drivers_day1_df.createOrReplaceTempView("drivers_day1") 

display(drivers_day1_df)


from pyspark.sql.functions import upper

drivers_day2_df = spark.read.option("inferSchema",True) \
    .json("/mnt/formula1dlajay/raw/2021-03-28/drivers.json") \
    .filter("driverId BETWEEN 6 and 15") \
    .select("driverId","dob",upper("name.forename").alias("forename"),upper("name.surname").alias("surname"))

drivers_day2_df.createOrReplaceTempView("drivers_day2")

display(drivers_day2_df)

from pyspark.sql.functions import upper

drivers_day3_df = spark.read.option("inferSchema",True) \
    .json("/mnt/formula1dlajay/raw/2021-03-28/drivers.json") \
    .filter("driverId BETWEEN 1 and 5 or driverId BETWEEN 16 and 20") \
    .select("driverId","dob",upper("name.forename").alias("forename"),upper("name.surname").alias("surname"))

%sql

create table if not exists f1_demo.drivers_merge (
  driverId INT,
  dob Date,
  forename string,
  surname string,
  createdDate date,
  updatedDate date
)
using delta


%sql

MERGE INTO f1_demo.drivers_merge tgt
USING drivers_day1 upd
ON tgt.driverId = upd.driverId
WHEN MATCHED THEN
  UPDATE SET
    tgt.dob = upd.dob,
    tgt.forename = upd.forename,
    tgt.surname = upd.surname,
    tgt.updatedDate = current_timestamp
WHEN NOT MATCHED
  THEN INSERT (
    driverId,
    dob,
    forename,
    surname,
    createdDate
  )
  VALUES (
    driverId,
    dob,
    forename,
    surname,
    current_timestamp
  )

%sql
select * from f1_demo.drivers_merge;

%sql

MERGE INTO f1_demo.drivers_merge tgt
USING drivers_day2 upd
ON tgt.driverId = upd.driverId
WHEN MATCHED THEN
  UPDATE SET
    tgt.dob = upd.dob,
    tgt.forename = upd.forename,
    tgt.surname = upd.surname,
    tgt.updatedDate = current_timestamp
WHEN NOT MATCHED
  THEN INSERT (
    driverId,
    dob,
    forename,
    surname,
    createdDate
  )
  VALUES (
    driverId,
    dob,
    forename,
    surname,
    current_timestamp
  )

%sql
select * from f1_demo.drivers_merge;


from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable

deltaTable = DeltaTable.forPath(spark, '/mnt/formula1dlajay/demo/drivers_merge')

deltaTable.alias('tgt') \
  .merge(
    drivers_day3_df.alias('upd'),
    'tgt.driverId = upd.driverId'
  ) \
  .whenMatchedUpdate(set =
    {
      "dob": "upd.dob",
      "forename": "upd.forename",
      "surname": "upd.surname",
      "updatedDate": "current_timestamp()"      
    }
  ) \
  .whenNotMatchedInsert(values =
    {
      "driverId": "upd.driverId",
      "dob": "upd.dob",
      "forename": "upd.forename",
      "surname": "upd.surname",
      "createdDate": "current_timestamp()"      
    }
  ) \
  .execute()

%sql
select * from f1_demo.drivers_merge;


142. History, Time Travel, Vacuum

History & Versioning
Time Travel
Vaccum - remove data for particular user (but it removes data after 7 days)


%sql
desc history f1_demo.drivers_merge


%sql
select * from f1_demo.drivers_merge version as of 2;

%sql
select * from f1_demo.drivers_merge timestamp as of "2024-02-03T15:32:23Z";


#spark version
df = spark.read.format("delta").option("timestampAsOf","2024-02-03T15:32:23Z").load("/mnt/formula1dlajay/demo/drivers_merge")

display(df)

df = spark.read.format("delta").option("versionAsOf","2").load("/mnt/formula1dlajay/demo/drivers_merge")
display(df)


#Vaccum - remove data for particular user (but it removes data after 7 days)

%sql
vacuum f1_demo.drivers_merge;

#you will see data in below query
%sql
select * from f1_demo.drivers_merge timestamp as of "2024-02-03T15:32:23Z"; -- still show data because it delete after 7 days



#to delete immediately we have to use retain 0 hours

%sql
SET spark.databricks.delta.retentionDurationCheck.enabled = false;
VACUUM f1_demo.drivers_merge RETAIN 0 HOURS

%sql
-- you wont see data in below query - you will get error
select * from f1_demo.drivers_merge timestamp as of "2024-02-03T15:32:23Z";


%sql
-- you can see latest data in below query but you can not see the history data
select * from f1_demo.drivers_merge



%sql
desc history f1_demo.drivers_merge

%sql
--delete from the records and restore with the help of history
delete from f1_demo.drivers_merge where driverId = 1;

%sql
-- you will see 19 records
select * from f1_demo.drivers_merge;

%sql
-- you will see 20 records in last version
select * from f1_demo.drivers_merge version as of 3;

# we will use merge command to restore the deleted data 

%sql
--merge command use to restore deleted record
merge into f1_demo.drivers_merge tgt
using f1_demo.drivers_merge version as of 3 src
on (tgt.driverId = src.driverId)
when not matched then 
insert *


# we will see merge operation after delete
%sql desc history f1_demo.drivers_merge

# you will see restored data and 20 data in below command
%sql 
select * from  f1_demo.drivers_merge


143. Delta Lake Transaction Log

meta store only keeps info of table and attributes
Transaction Logs are not kept in th hive meta store because it is really inefficient to go and read hive meta store and and get all information for everything

delta lake did some clever thing for that (inside delta lake or data lake it creates log folder(_delta_log) and inside that folder .json and crc file where it keeps timestamps userid username,operation,azure account etc )


%sql

create table if not exists f1_demo.drivers_txn (
  driverId INT,
  dob Date,
  forename string,
  surname string,
  createdDate date,
  updatedDate date
)
using delta


%sql desc history f1_demo.drivers_txn;

# different parquet file will create and 00000000000000000001.json file for versioning and when we will read data for version then it will read parquet file of this operation

%sql
insert into f1_demo.drivers_txn
select * from f1_demo.drivers_merge
where driverId = 1;

%sql desc history f1_demo.drivers_txn;


# different parquet file will create and 00000000000000000002.json file for versioning and when we will read data for version then it will read parquet file of this operation

%sql
insert into f1_demo.drivers_txn
select * from f1_demo.drivers_merge
where driverId = 2;


%sql
delete from f1_demo.drivers_txn
where driverId = 1;


# it wil create 18 .json file and 2-3 compacted.json file will create in transaction log file


for driver_id in range(3,20):
    spark.sql(f"""insert into f1_demo.drivers_txn
              select * from f1_demo.drivers_merge
              where driverId = {driver_id}""")


# it wil create 1 .json file inside log folder and 2-3 partition file

%sql
insert into f1_demo.drivers_txn
select * from f1_demo.drivers_merge;

# transaction log stays for 30 days after that azure deletes it because it cost and slower the process



144. Convert from Parquet to Delta

# convert parquet file or table to delta table

%sql

create table if not exists f1_demo.drivers_convert_to_delta (
  driverId INT,
  dob Date,
  forename string,
  surname string,
  createdDate date,
  updatedDate date
)
using parquet

%sql
insert into f1_demo.drivers_convert_to_delta
select * from f1_demo.drivers_merge

%sql
--convert parquet table to delta table
convert to delta f1_demo.drivers_convert_to_delta


df  = spark.table("f1_demo.drivers_convert_to_delta")

# create a parquet file into delta table (it will create transaction log files .josn and .crc file after converting we can do our own operations as we want)
df.write.format("parquet").save('/mnt/formula1dlajay/demo/drivers_convert_to_delta_new')

%sql
convert to delta parquet.`/mnt/formula1dlajay/demo/drivers_convert_to_delta_new`


145. Data Ingestion - Circuits File


utils/1.prepare_for_incremental_load - file
run all command for this file because we want to delete all tables;


Delta_Lake/ingestion_with_includes/1.ingest_circuits_file 
Delta_Lake/ingestion_with_includes/2.ingest_races_file
Delta_Lake/ingestion_with_includes/3.ingest_constructors_file
Delta_Lake/ingestion_with_includes/4.ingest_drivers_file

only change we have to do

%run "../../includes/configuration"
%run "../../includes/common_functions"
circuits_final_df.write.mode("overwrite").format("delta").saveAsTable("f1_processed.circuits")


146. Data Ingestion - Results File

Delta_Lake/ingestion_with_includes/5.ingest_results_file - file

%run "../../includes/configuration"
%run "../../includes/common_functions"

#by using partition column in merge statement then query will be quiker -> tgt.race_id = src.race_id

spark.conf.set("spark.databricks.optimizer.dynamicPartitionPruning","true")
from delta.tables import DeltaTable

if (spark._jsparkSession.catalog().tableExists("f1_processed.results")):
   deltaTable = DeltaTable.forPath(spark,"/mnt/formula1dlajay/processed/results")
   deltaTable.alias('tgt').merge(
       results_final_df.alias("src"),
       "tgt.result_id = src.result_id and tgt.race_id = src.race_id") \
       .whenMatchedUpdateAll() \
       .whenNotMatchedInsertAll() \
       .execute() 
else:
      results_final_df.write.mode("overwrite").partitionBy("race_id").format("delta").saveAsTable("f1_processed.results")


147. Data Ingestion - Results File Improvements


includes/common_functions - file

# add below function

def merge_delta_data(input_df, db_name,table_name,partition_column,folder_path,merge_condition):
  
  spark.conf.set("spark.databricks.optimizer.dynamicPartitionPruning","true")
  from delta.tables import DeltaTable
  
  if (spark._jsparkSession.catalog().tableExists(f"{db_name}.{table_name}")):
    deltaTable = DeltaTable.forPath(spark,f"{folder_path}/{table_name}")
    deltaTable.alias('tgt').merge(
    input_df.alias("src"),
    merge_condition) \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute() 
  else:
      input_df.write.mode("overwrite").partitionBy(partition_column).format("delta").saveAsTable(f"{db_name}.{table_name}")


# in below file add below code and call function
Delta_Lake/ingestion_with_includes/5.ingest_results_file - file

merge_condition = "tgt.result_id = src.result_id and tgt.race_id = src.race_id"
merge_delta_data(results_final_df, "f1_processed", "results", "race_id",processed_folder_path, merge_condition)


148. Data Ingestion - All Other Files (Assignment)

# https://ergast.com/docs/f1db_user_guide.txt - only take primary id and partition column in merge condition
Delta_Lake/ingestion_with_includes/6.ingest_pit_stops_file

merge_condition = "tgt.race_id = src.race_id and tgt.driver_id = src.driver_id and tgt.stop = src.stop and tgt.race_id = src.race_id"
merge_delta_data(pit_stops_with_columns_df, "f1_processed", "pit_stops", "race_id", processed_folder_path, merge_condition)


%sql
select race_id, count(1) from f1_processed.pit_stops
group by race_id
order by race_id desc;



# https://ergast.com/docs/f1db_user_guide.txt -> only take primary id and partition column in merge condition
merge_condition = "tgt.race_id = src.race_id and tgt.driver_id = src.driver_id and tgt.lap = src.lap and tgt.race_id = src.race_id"
merge_delta_data(lap_times_with_columns_df, "f1_processed", "lap_times", "race_id", processed_folder_path, merge_condition)

%sql
select * from f1_processed.lap_times;

Delta_Lake/ingestion_with_includes/8.ingest_qualifying_file
# https://ergast.com/docs/f1db_user_guide.txt -> only take primary id and partition column in merge condition
merge_condition = "tgt.qualify_id = src.qualify_id and tgt.race_id = src.race_id"
merge_delta_data(qualifying_with_columns_df, "f1_processed", "qualifying", "race_id", processed_folder_path, merge_condition)

%sql
select * from f1_processed.qualifying;


149. Data Ingestion - Fix Duplicates in Results Data


Delta_Lake/ingestion_with_includes/5.ingest_results_file
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.dropDuplicates.html


# De-dupe the Dataframe -> remove duplicates values

results_deduped_df = results_final_df.dropDuplicates(["race_id","driver_id"])

merge_condition = "tgt.result_id = src.result_id and tgt.race_id = src.race_id"
merge_delta_data(results_deduped_df, "f1_processed", "results", "race_id",processed_folder_path, merge_condition)

%sql
-- give no result becuase we create data frame for no duplicates
select race_id,driver_id, count(1) from f1_processed.results
group by race_id,driver_id
having count(1) > 1
order by race_id, driver_id desc;

%sql
select count(1) from f1_processed.results; #give count

%sql
select * from f1_processed.results where race_id = 540 and driver_id = 229; # remove duplcate result

%sql
select count(1) from f1_processed.results;  


150. Data Transformation - All PySpark Notebooks


Delta_Lake/trnas/1.race_results

# read all the delta dataframe from above file

drivers_df = spark.read.format("delta").load(f"{processed_folder_path}/drivers") \
    .withColumnRenamed("number","driver_number") \
    .withColumnRenamed("name","driver_name") \
    .withColumnRenamed("nationality", "driver_nationality")



merge_condition = "tgt.driver_name = src.driver_name and tgt.race_id = src.race_id"
merge_delta_data(final_df, "f1_presentation", "race_results", "race_id",presentation_folder_path, merge_condition)


%sql
select * from f1_presentation.race_results ;


%sql
select race_id, count(1) from f1_presentation.race_results
group by race_id
order by race_id desc;


Delta_Lake/trnas/2.driver_standings 

race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") 

race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))

merge_condition = "tgt.driver_name = src.driver_name and tgt.race_year = src.race_year"
merge_delta_data(final_df, "f1_presentation", "driver_standings", "race_year",presentation_folder_path, merge_condition)


%sql
select * from f1_presentation.driver_standings where race_year = 2021;


%sql
select race_year,count(1) from f1_presentation.driver_standings
group by race_year
order by race_year desc;



Delta_Lake/trnas/3.constructor_standings


race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(f"file_date = '{v_filer_date}'") 


race_result_df = spark.read.format("delta").load(f"{presentation_folder_path}/race_results") \
    .filter(col("race_year").isin(race_year_list))

merge_condition = "tgt.team = src.team and tgt.race_year = src.race_year"
merge_delta_data(final_df, "f1_presentation", "constructor_standings", "race_year",presentation_folder_path, merge_condition)

%sql
select * from f1_presentation.constructor_standings where race_year = 2021;

%sql
select race_year,count(1) from f1_presentation.driver_standings
group by race_year
order by race_year desc;

151. Data Transformation - SQL Notebook

Delta_Lake/trnas/4.calculated_race_result

dbutils.widgets.text("p_file_date","2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")


spark.sql(f"""
          create table if not exists f1_presentation.calculated_race_results(
          race_year int,
          team_name string,
          driver_id int,
          driver_name string,
          race_id int,
          position int,
          points int,
          calculated_points int,
          created_date TIMESTAMP,
          updated_date TIMESTAMP
          )
          using delta
    """)

spark.sql(f"""
                create or replace temp view race_result_updated
                as
                select races.race_year,
                constructors.name as team_name,
                drivers.driver_id,
                drivers.name as driver_name,
                races.race_id,
                results.position,
                results.points,
                11 - results.position as calculated_points
                from f1_processed.results
                join f1_processed.drivers on (drivers.driver_id = results.driver_id)
                join f1_processed.constructors on (constructors.constructor_id = results.constructor_id)
                join f1_processed.races on (races.race_id = results.race_id)
                where results.position <= 10 and results.file_date = '{v_file_date}'                 
          
    """)

# %sql select * from race_result_updated where race_year = 2021;


#by running below command we will get incremental data in table - f1_presentation.calculated_race_results

spark.sql(f"""
        MERGE INTO f1_presentation.calculated_race_results tgt
        USING race_result_updated upd
        ON (tgt.driver_id = upd.driver_id and tgt.race_id = upd.race_id)
        WHEN MATCHED THEN
        UPDATE SET
            tgt.position = upd.position,
            tgt.points = upd.points,
            tgt.calculated_points = upd.calculated_points,
            tgt.updated_date = current_timestamp
        WHEN NOT MATCHED
        THEN INSERT (
            race_year,
            team_name,
            driver_id,
            driver_name,
            race_id,
            position,
            points,
            calculated_points,
            created_date
        )
        VALUES (
            race_year,
            team_name,
            driver_id,
            driver_name,
            race_id,
            position,
            points,
            calculated_points,
            current_timestamp
        )
   """)

%sql select count(1) from race_result_updated;

%sql select count(1) from f1_presentation.calculated_race_results;


Section - 23 - Azure Data Factory

152. Section Overview

it use to schedule and execute databricks notebook



153. Azure Data Factory Overview

a fully managed, serverless data integration solution for ingesting, preparing and transforming all your data at scale.

data coming from clouds(AWS,azure,GCP)  ,saas, on prime applications in different data formats

Azure Datafactory Provides end to end dat ingestion , transformation and orchestration

What Datafactory is 
1. Fully Managed service
2. serverless
3. Data Integration service
4. Data transformation service
5. Data orchestration service

What Datafactory is not
1. Data migration tool
2. Data Streaming service
3. Suitable for Complex Data transformation
4. Data Storage service


154. Create Azure Data Factory Service

https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.DataFactory%2FdataFactories

resource group - databrickscourse-rg
name - databricks-course-adf-ajay
region - central india


Resource group : databrickscourse-rg

# Go to launch studio

Location:Central India
Subscription:Azure subscription 1
Subscription ID:49a84c57-21dd-4dde-a744-8c4a8075b500
Type:Data factory (V2)

data factory interface


155. Azure Data Factory Components

Components - storage(adls,sql database) -> linked Service -> datasets -> Activity -> Pipeline -> trigger
Components - compute(azure databricks,azure hdinsights) -> linked Service  -> Activity -> Pipeline -> trigger

156. Create Pipeline - Circuits File

go inside data factory -> author -> pipeline -> new pipeline

pipeline name - pl_ingest_formula1_data

drag jupyter notebook
 name  - 

# linked service
 subscription name -Azure subscription 1 (49a84c57-21dd-4dde-a744-8c4a8075b500)
 name - ls_databrickscourse_ws
 Account selection method* - From Azure subscription
 Select cluster - Existing interactive cluster
 Authentication type - managed service type 

and copy Managed identity name
Managed identity name: databricks-course-adf-ajay

Managed identity name:databricks-course-adf-ajay
Managed identity object ID:540ae937-0dbe-4002-82a2-85ecf1f4edbc
Grant Data Factory service managed identity access to your Resources.

Choose from existing clusters - Databricks-course-cluster


# job cluster  - destory automatically after job is finished

https://portal.azure.com/#view/Microsoft_Azure_AD/AddRoleAssignmentsLandingBlade/scope/%2Fsubscriptions%2F49a84c57-21dd-4dde-a744-8c4a8075b500%2FresourceGroups%2Fdatabrickscourse-rg%2Fproviders%2FMicrosoft.Databricks%2Fworkspaces%2Fdatabrickscourse-ws/abacSettings~/%7B%7D/priorityRoles~/%5B%5D

Go inside -> databrickscourse-ws | Access control (IAM) -> Privileged administrator roles -> Contributor -> then select -> databricks-course-adf-ajay 

and then create so databricks will be connected to datafactory

in setting select notebook 'Delta_lake/ingestion_with_includes/1.ingest_circuits_file' -> notebook

go to setting of pipeline after clicking outside of notebook 
got to -> variable - v_data_source - Ergapt
got to -> parameter - p_window_end_date


inside parameter of setting of pipeline -> p_window_end_date - 
go to settin of notebook -> base parameter ->   p_data_source - @variables('v_data_source') (selected dynamically)
go to settin of notebook -> base parameter ->   p_file_date - @formatDateTime(pipeline().parameters.p_window_end_date,'yyyy-MM-dd') (selected formatdate function and then select parameter -> p_window_end_date and then format datasets)


157. Debugging a Pipeline

go to debug option on top and then it will ask for date 'p_window_end_date' -> 2021-04-18




158. Update Pipeline - Ingest All Other Files

duplicate all other files from folder -Delta_lake/ingestion_with_includes



159. Improve Pipeline - Handle Missing Files