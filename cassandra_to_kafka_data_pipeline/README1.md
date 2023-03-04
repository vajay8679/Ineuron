#visual studio extension
1. python
2. dev containers
3. remote development
4. cassandra workbench


#run below command inside directory - cassandra-kafka-dev
docker compose -f docker-compose.yml up -d

#check docker container
docker ps

pwd


cltr + p

then type
>Cassandra Workbench: Generate configuration
then select


docker compose up
docker compose down

########################################################
1. CREATE KEYSPACE ineuron
	WITH REPLICATION = {
		'class': 'org.apache.cassandra.locator.SimpleStrategy',
		'replication_factor': '3'
	}
	AND DURABLE_WRITES = true;


2.  CREATE TABLE EMPLOYEE(
     EMP_ID INT,
     EMP_NAME text,
     CITY text,
     STATE text,
     primary key (EMP_ID)
 );


 3. INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES
(2,'Avnish','Bengalore','Karnataka');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (4,'Stephen','Mumbai','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (5,'Berry','Chennai','Tamilnadu');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (6,'Barton','Pune','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (7,'Natasha','Hyderabad','Andra Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (8,'Sundar','Noida','Uttar Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (9,'Shashank','Delhi','Delhi');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (10,'Sudhanshu','New Mumbai','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (11,'Krish','Nagpur','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (12,'Aman','Hyderabad','Andra Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (13,'Rahul','Noida','Uttar Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (14,'Sunny','Delhi','Delhi');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (15,'Vishal','New Mumbai','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (16,'Vikash','Nagpur','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (17,'Aravind','Chennai','Tamilnadu');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (18,'Adam','Pune','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (19,'Scarlett','Hyderabad','Andra Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (20,'Robert','Noida','Uttar Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (21,'Shivam','Delhi','Delhi');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (22,'Deepak','New Mumbai','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (23,'Amit','Nagpur','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (24,'Susmita','Hyderabad','Andra Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (25,'Iris','Mumbai','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (26,'Pia','Chennai','Tamilnadu');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (27,'Ankit','Pune','Maharashtra');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (28,'Akash','Hyderabad','Andra Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (29,'Harry','Noida','Uttar Pradesh');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (30,'Emma','Delhi','Delhi');
INSERT INTO ineuron.EMPLOYEE (EMP_ID,EMP_NAME,CITY,STATE) VALUES (31,'Abhishek','New Mumbai','Maharashtra');


4. select * from ineuron.EMPLOYEE;




After running above query in CQL

in pallet  
dev containers:Attached to running containers

then 

select 
pyspark-1

in terminal in new vs code after selecting pyspark-1

ls /
cd /prject
ls /

after running above command you are in project directory then run below command for producer.py 
1. spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0  producer.py 


after running 'cd /prject' command on new terminal you are in project directory then run below command for  consumer.py
2. spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 consumer.py 


CDC - change data capture