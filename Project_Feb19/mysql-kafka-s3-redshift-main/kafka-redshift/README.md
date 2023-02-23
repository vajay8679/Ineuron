File is dumped in s3 bucket from Kafka

How to export data from s3 to Redshift?

We have done the implementation of exporting data from s3 to Redshift
Steps:
1. Reading data from s3 using Pyspark
2. Do required transformation on dataset
3. Dump data to Redshift using pyspark

Dump s3 file to Redshift

![S3 Redshift](../diagrams/s3-redshift.png)


Create .env file and set required environment variables
```
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
REDSHIFT_USER_NAME=""
REDSHIFT_PASSWORD=""
TEMP_BUCKET_NAME=""
REDSHIFT_JDBC_URL="jdbc:redshift://<hostname>:5439/<database>?user=<user_name>&password=<password>&ssl=true&sslfactory=com.amazon.redshift.ssl.NonValidatingFactory"
```

Python and PySpark environment used this source code tested
```
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
2022-11-23 12:02:21,727 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.8
      /_/

Using Python version 3.5.3 (default, Sep 27 2018 17:25:39)
SparkSession available as 'spark'.
```

Install requirements.txt
```
pip install -r requirements.txt
```

To run your script run start.sh file
```
sh start.sh
```