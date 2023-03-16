on terminal run below command
1. export AWS_ACCESS_KEY_ID=AKIA2GM5ZBDDQJSDB6XP
2. export AWS_SECRET_ACCESS_KEY=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

#run below docker command 
3. docker compose -f docker-compose.yaml up -d


#i have changed port from 3306 t0 3307 as 3306 was already exist then open adminer

http://localhost:8085/?server=db 
username - root
password - example


#run below command on terminal for dump database
4. docker exec -i mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < "./database-dump/mysqlsampledatabase.sql"

#on pellet type 
dev containers:running

#select updated one for mysql-kafka-s3
pyspark 3.2.1

create account
https://confluent.cloud/signup

create cluster - KAFKA_DEMO_CLUSTER
create topic - dim_customers,dim_dates,dim_employees,dim_locations,dim_products,fact_sales
generate API Key - 
=== Confluent Cloud API key: lkc-3rknjo ===

API key:
TEP7OMK473LNSKPL

API secret:
l2o2+rv9x2TcDxKVQCJedvNO5MdkSb4Duzx8R4JkWsMoRAyc/xCJZ/uK0QRMuhip

Bootstrap server:
pkc-lzvrd.us-west4.gcp.confluent.cloud:9092



inside remote container server open terminal
1. ls /
2. cd /project
3. ls /


create 'requirements.txt'
-e.
python-dotenv

after it run below command
pip install -r requirements.txt


create file '.env'
KAFKA_TOPIC_FACT_SALE="fact_sales"
KAFKA_TOPIC_DIM_EMP="dim_employees"
KAFKA_TOPIC_DIM_CUST="dim_customers"
KAFKA_TOPIC_DIM_PROD="dim_products"
KAFKA_TOPIC_DIM_DATE="dim_dates"
KAFKA_TOPIC_DIM_LOC="dim_locations"
KAFKA_BOOTSTRAP_SERVER="pkc-lzvrd.us-west4.gcp.confluent.cloud:9092"
KAFKA_CLOUD_API_KEY="TEP7OMK473LNSKPL"
KAFKA_CLOUD_API_SECRET="l2o2+rv9x2TcDxKVQCJedvNO5MdkSb4Duzx8R4JkWsMoRAyc/xCJZ/uK0QRMuhip"
MYSQL_URI="jdbc:mysql://mysql:3307/classicmodels?useSSL=false"
MYSQL_USER_NAME="root"
MYSQL_PASSWORD="example"
BUCKET_NAME="retail-data-analysis-b1"


#remove  below lines from -> /project/src/config/spark_manager.py
.config("spark.executor.memory", "6g") 
.config("spark.driver.memory", "6g") 
.config("spark.executor.memoryOverhead", "8g")

then run command on terminal
1. python3 producer.py


bucket name='retail-data-analysis-b2'

for kafka-redship 
we will use old version of pyspark
pyspark-2.4.8