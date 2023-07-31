#1. Create EC2 Instance - 'new_datapipeline'

instance type -  t2.large
key-value pair  - datapipeline_ec2.pem
Configure storage - 1 volume(s) - 96 GiB  

#then go to security section inside that instance  - 
https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#InstanceDetails:instanceId=i-02dcee604d37fea3a


sg-06401ebc74fc11ac0  
https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#SecurityGroup:securityGroupId=sg-06401ebc74fc11ac0



#Edit inbound rules inside security groups

Type - custom TCP
Port range - 0-10000
Source - anywhere - 0.0.0.0/0



#in EC2 - connect copy below 1,2 and paste in CMD

1. chmod 400 datapipeline_ec2.pem
2. ssh -i "datapipeline_ec2.pem" ec2-user@ec2-13-235-243-70.ap-south-1.compute.amazonaws.com

dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/5 Days Placement Crash Course/Data_Pipeline_Using_Pyspark_Airflow$ chmod 400 datapipeline_ec2.pem
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/5 Days Placement Crash Course/Data_Pipeline_Using_Pyspark_Airflow$ ssh -i "datapipeline_ec2.pem" ec2-user@ec2-13-235-243-70.ap-south-1.compute.amazonaws.com

[ec2-user@ip-172-31-37-180 ~]$ ls
[ec2-user@ip-172-31-37-180 ~]$ whoami
ec2-user
[ec2-user@ip-172-31-37-180 ~]$ 


#Install and setup Docker and Docker-compose
#install on ec2 environment
[ec2-user@ip-172-31-37-180 ~]$ sudo yum update -y

[ec2-user@ip-172-31-37-180 ~]$ sudo yum install docker

[ec2-user@ip-172-31-37-180 ~]$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

[ec2-user@ip-172-31-37-180 ~]$ sudo chmod +x /usr/local/bin/docker-compose

[ec2-user@ip-172-31-37-180 ~]$ sudo gpasswd -a $USER docker

[ec2-user@ip-172-31-37-180 ~]$ newgrp docker


Start/Stop Docker inside EC2 
[ec2-user@ip-172-31-37-180 ~]$ sudo systemctl start docker
[ec2-user@ip-172-31-37-180 ~]$ sudo systemctl stop docker


To Start Docker - sudo systemctl start docker
To Stop Docker - sudo systemctl stop docker



#in another cmd where pem file run 1st command 
1. scp -r -i "datapipeline_ec2.pem" docker_exp ec2-user@ec2-3-111-188-230.ap-south-1.compute.amazonaws.com:/home/ec2-user/docker_exp

dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/5 Days Placement Crash Course/Data_Pipeline_Using_Pyspark_Airflow$ scp -r -i "datapipeline_ec2.pem" docker_exp ec2-user@ec2-15-206-170-62.ap-south-1.compute.amazonaws.com:/home/ec2-user/docker_exp



#inside EC2 environment give permission to docker_exp folder by running  2nd command
2. sudo chmod -R 755 docker_exp

[ec2-user@ip-172-31-37-180 ~]$ sudo chmod -R 755 docker_exp

#then
cd docker_exp


#List files with permissions
ls -l


#if getting this below error run while running -> './airflow_init.sh' then run - sudo dnf install libxcrypt-compat

[ec2-user@ip-172-31-42-89 docker_exp]$ sudo pacman -S libxcrypt-compat

#error
[ec2-user@ip-172-31-42-89 docker_exp]$ ./airflow_init.sh [27142] Error loading Python lib '/tmp/_MEIRVF32Y/libpython3.7m.so.1.0': dlopen: libcrypt.so.1: cannot open shared object file: No such file or directory




#then run below command
./airflow_init.sh 


#move files in dag folder
mv -t dags hive_script.py hive_connection.py

[ec2-user@ip-172-31-42-89 docker_exp]$ mv -t dags hive_script.py hive_connection.py


#run 

[ec2-user@ip-172-31-42-89 docker_exp]$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                        PORTS                                       NAMES
3757691b4762   postgres:13    "docker-entrypoint.s…"   13 hours ago   Up About a minute (healthy)   5432/tcp                                    docker_exp_postgres_1
4a73f9a0cd4f   redis:latest   "docker-entrypoint.s…"   13 hours ago   Up About a minute (healthy)   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   docker_exp_redis_1


#run below command inside docker_exp folder
docker-compose up
[ec2-user@ip-172-31-42-89 docker_exp]$ docker-compose up
###############################################################
Start/Stop docker containers
o	cd docker_exp (run if not in the right directory)
o	docker-compose up
o	docker-compose stop
o	docker-compose down (stop and remove containers)
###############################################################

#Port Forwarding to access services locally in root directory in terminal on local

ssh -i "datapipeline_ec2.pem" ec2-user@ec2-65-2-190-221.ap-south-1.compute.amazonaws.com -o "ServerAliveInterval 30" -L 2081:localhost:2041 -L 4888:localhost:4888 -L 4889:localhost:4889 -L 2080:localhost:2080 -L 8050:localhost:8050 -L 8051:localhost:8051 -L 4141:localhost:4141 -L 4090:localhost:4090 -L 3180:localhost:3180 -L 50075:localhost:50075 -L 50070:localhost:50070 -L 50010:localhost:50010 -L 3077:localhost:3077 -L 4080:localhost:4080 -L 9870:localhost:9870 -L 8188:localhost:8188 -L 9864:localhost:9864 -L 8042:localhost:8042 -L 8088:localhost:8088 -L 8080:localhost:8080 -L 8081:localhost:8081 -L 10000:localhost:10000 -L 6080:localhost:6080 -L 8998:localhost:8998


dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/5 Days Placement Crash Course/Data_Pipeline_Using_Pyspark_Airflow$ ssh -i "datapipeline_ec2.pem" ec2-user@ec2-13-235-243-70.ap-south-1.compute.amazonaws.com -o "ServerAliveInterval 30" -L 2081:localhost:2041 -L 4888:localhost:4888 -L 4889:localhost:4889 -L 2080:localhost:2080 -L 8050:localhost:8050 -L 8051:localhost:8051 -L 4141:localhost:4141 -L 4090:localhost:4090 -L 3180:localhost:3180 -L 50075:localhost:50075 -L 50070:localhost:50070 -L 50010:localhost:50010 -L 3077:localhost:3077 -L 4080:localhost:4080 -L 9870:localhost:9870 -L 8188:localhost:8188 -L 9864:localhost:9864 -L 8042:localhost:8042 -L 8088:localhost:8088 -L 8080:localhost:8080 -L 8081:localhost:8081 -L 10000:localhost:10000 -L 6080:localhost:6080 -L 8998:localhost:8998
   ,     #_
   ~\_  ####_        Amazon Linux 2023
  ~~  \_#####\
  ~~     \###|
  ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
   ~~       V~' '->
    ~~~         /
      ~~._.   _/
         _/ _/
       _/m/'
Last login: Fri Jul 28 16:04:53 2023 from 27.7.241.132
[ec2-user@ip-172-31-42-89 ~]$ docker ps
CONTAINER ID   IMAGE                                                    COMMAND                  CREATED        STATUS                   PORTS                                                                                                                                                                        NAMES
fe80a116676b   bde2020/spark-worker:3.0.0-hadoop3.2                     "/bin/bash /worker.sh"   9 hours ago    Up 9 hours               0.0.0.0:8081->8081/tcp, :::8081->8081/tcp                                                                                                                                    hdp_spark-worker-1
07de77be4b69   bde2020/hive:2.3.2-postgresql-metastore                  "entrypoint.sh /bin/…"   9 hours ago    Up 9 hours               0.0.0.0:10000->10000/tcp, :::10000->10000/tcp, 10002/tcp                                                                                                                     hdp_hive-server


[ec2-user@ip-172-31-42-89 ~]$ docker exec -i -t hdp_namenode bash
root@2ca254492452:/# exit
[ec2-user@ip-172-31-42-89 ~]$ docker exec -i -t hdp_spark-master bash
bash-5.0# pyspark
[ec2-user@ip-172-31-42-89 ~]$ docker exec -i -t hdp_hive-server bash
root@hiveserver:/opt# hive 


#after running above command locallay check on ec2 environment all docker container
docker ps 


######################################################################
#to go inside a particular container inside ec2

#hadoop
docker exec -i -t hdp_namenode bash

#spark
1. docker exec -i -t hdp_spark-master bash
2. pyspark

#hive
1. docker exec -i -t hdp_hive-server bash
2. hive
3. show databases;
######################################################################


#for exit from docker root -> 'ctrl + D'

######################################
to check all environment on local

Nifi - http://localhost:2080/nifi/

Airflow - http://localhost:6080/    

username - airflow
password - airflow

Spark - http://localhost:8080/

Jupyter lab - http://localhost:4888/lab?
########################################


#inside ec2 inside docker_exp folder we can see-> NifiCovidTemplate.xml


#upload Nifitemplate from docker_exp folder in local Nifi - http://localhost:2080/nifi/

Nifi - http://localhost:2080/nifi/

#right click on mouse and then upload and then go to template section on header then click on add then template will be loaded


#checking Nifi view and data flow in Nifi (Data Encryption parshing)

#right click then configure then check attributes
start - refresh - stop

#in encryption template- double click and set pasword in encryption


#for sending data in hdfs first run from nifi - PutHDFS

open ec2 machine on cmd so we can see data

1. docker exec -i -t hdp_namenode bash

2. hadoop fs -ls /dezyre_data/corona-table





#for sending data in kafka first run from nifi - Publish Kafka

open ec2 machine on cmd so we can see data

1. docker exec -i -t hdp_kafka bash

2. ls

3. cd /opt/kafka_2.12-2.5.0

4. ls

5. bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic dezyre_data_csv

#till now we are in public kafka then we will do preprocessing with test.py file and then again send to consume kafka then hadoop and then airflow,hive then visualization

#data architechture

#pyspark streaming inside ec2 machine - to run spark-submit job to publish data to other kafka topic and it will be consumed by consume kafka

1. docker cp /home/ec2-user/docker_exp/test.py hdp_spark-master:/test.py

2. docker exec -i -t hdp_spark-master bash

3. chmod 755 test.py

4. ./spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0 --master local[2] test.py


remove this from test.py 
#sc = SparkContext(appName='dezyre_test')
#sc.setLogLevel('WARN')
#spark = SparkSession(sc)

#after running 4th command open new ec2 machine go to kafka container and checkout dezyre_output

1. docker exec -i -t hdp_kafka bash

2. cd /opt/kafka_2.12-2.5.0

3. bin /kafka-console-consumer.sh --bootstrap-server localhost:9092 --from-beginning --topic dezyre_output


#then refresh consume kafka in nifi and then start then evaluate json path and then rest of the pipeline as well

#to see output data in hdfs open ec2 machine on cmd and go inside hdfs container

1. docker exec -i -t hdp_namenode bash

2. hadoop fs -ls /dezyre_data/dezyre_kafka_out



#move data from hdfs location to hive open ec2 machine on cmd and go inside hive container

1. docker exec -i -t hdp_hive-server bash

2. hive

3. show tables;

#from ->corana_data.hql

4. CREATE EXTERNAL TABLE IF NOT EXISTS corona_table(
    'Global_new_confirmed' int,
    'Global_new_deaths' int,
    'Global_new_recovered' int,
    'Global_total_confirmed' int,
    'Global_total_deaths' int,
    'Global_total_recovered' int,
    'Country_code' string,
    'Country_name' string,
    'Country_new_deaths' int,
    'Country_new_recovered' int,
    'Country_new_confirmed' int,
    'Country_total_deaths' int,
    'Country_total_confirmed' int,
    'Country_total_recovered' int,
    'Country_slug' string,
    'Extracted_timestamp' timestamp,
    'country_code_hash' string,
    'Country_code_final' string
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    location '/dezyre_data/corona-table';

5. show tables;

6. select * from corona_table limit 10;

#from ->process_data.hql

7. CREATE EXTERNAL TABLE IF NOT EXISTS country_table_dezyre(
    'country_code' string,
    'country_name' string,
    'country_total_deaths' int,
    'extracted_timestamp' string )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    location '/dezyre_data/dezyre_kafka_out';

8. show tables;

9. select * from country_table_dezyre limit 10;



#data flow with Airflow -> how to connect with hive and scheduling some job
we have hive_script. and hive_connection.py

Go to Airflow and go to admin-> connection and then add
connId - hive_local
conntype - Hive client wrapper
logi -hive
password - hive
port -10000

save



and then
in airflow enable hive_script then go inside hive_script then run Dag trigger

hive_script -> Dag trigger -> Graph View -> logs on square


in ec2 machine inside hive 

1. docker exec -i -t hdp_hive-server bash
2. hive
3. show databases;
4. use db;
4. show tables

we can see by running 2nd command 
'airflow_hive' table also

1. select * from airflow_hive;


#we can connect hive with tablue and perform all operation