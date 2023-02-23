Export data from mysql-database to REDSHIFT using kafka

![Data flow diagram](./diagrams/dataflow-diagram.png)

Problem Statement:
We need to build an ETL pipeline to dump mysql data base record to redshift using kafka
![MY SQL DATABASE](./diagrams/mysql-oltp-database.png)


RedShift Dataware house
![Red Shift](./diagrams/redshift-olap-diagram.png)
Approach
1. Read data from mysql and  send to kafka topic and from kafka topic we will dump to s3 bucket
![mysql-kafka-s3](./diagrams/mysql-kafka-s3.png)

2. Read data from s3 bucket and dump in REDSHIFT
![s3-redshift](./diagrams/s3-redshift.png)

Launch entire server setup
```
docker-compose up
```

Dump data in mysql db
```
docker exec -i mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < "./database-dump/mysqlsampledatabase.sql"
```



We will design Star Schema so that we can export above attached OLTP to OLAP

1. [Redshift setup](doc/REDSHIFT.md)
2. [Kafka setup](doc/CONFLUENT_KAFKA.md)

1. [MYSQL KAFKA S3](./mysql-kafka-s3/README.md) Project Description
2. [S3 Redshift](./kafka-redshift/README.md) Project Description

