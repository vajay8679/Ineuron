#necessary libraries of pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

spark = SparkSession.builder.appName("demoApp").getOrCreate()

#Create list of data to prepare data frame
person_list = [("Berry","","Allen",1,"M"),
        ("Oliver","Queen","",2,"M"),
        ("Robert","","Williams",3,"M"),
        ("Tony","","Stark",4,"F"),
        ("Rajiv","Mary","Kumar",5,"F")
    ]


    #defining schema for dataset
schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", IntegerType(), True), \
    StructField("gender", StringType(), True), \

    ])

    #creating spark dataframe
df = spark.createDataFrame(data=person_list,schema=schema)

    #Printing data frame schema
df.printSchema()

    #Printing data
df.show(truncate=False)

    #Writing file in hadoop
df.write.csv("/output/record.csv")
