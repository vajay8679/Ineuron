## PySpark Apache Kafka and  Cassandra DB 



This project demonstrate how to setup developmen enviornment locally
This is a repo help you to understand and launch Kafka cluster 


### Project Architecture:
![untitled (1)](https://user-images.githubusercontent.com/115451707/219657272-0b190c35-b148-43d3-a30f-7611705f3a6f.png)


## Steps to setup projects

To start the setup
```
docker-compose up -d
```

To stop the setup
```
docker-compose down
```

Install few extension in vscode to work with cassandra db
1. Cassandra Workbench

Create a keysapce with name "ineuron"
```
CREATE KEYSPACE ineuron
	WITH REPLICATION = {
		'class': 'org.apache.cassandra.locator.SimpleStrategy',
		'replication_factor': '3'
	}
	AND DURABLE_WRITES = true;
```

Create a table Employee
```
 CREATE TABLE EMPLOYEE(
     EMP_ID INT,
     EMP_NAME text,
     CITY text,
     STATE text,
     primary key (EMP_ID)
 );
```

> To insert records into Employee table refer CQL_SCRIPT.cql

Once above steps is completed execute below command

To launch producer script
```
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0  producer.py 
```

To launch consumer script
```
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 consumer.py 
```