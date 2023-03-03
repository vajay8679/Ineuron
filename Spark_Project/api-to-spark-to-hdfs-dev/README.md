inside spark_project directory

1. PROJECT_DIR=$(pwd)
2. docker pull avnish327030/spark-hadoop-airflow
3. docker image tag  avnish327030/spark-hadoop-airflow spark-hadoop-airflow
4. docker run -it -p 9870:9870 -p 8088:8088 -p 8080:8080 -p 18080:18080 -p 9000:9000 -p 8888:8888 -p 9864:9864 -p 8085:8085 -p 8793:8793 -p 8081:8081 -v $PROJECT_DIR/project/notebook:/root/ipynb -v $PROJECT_DIR/project/airflow:/home/airflow -v $PROJECT_DIR/data:/data avnish327030/spark-hadoop-airflow

Name Node  - http://localhost:9870/
Hadoop Cluster - http://localhost:8088/
Spark Master - http://localhost:8080/
History Server - http://localhost:18080/
Jupyter Lab - http://localhost:8888/
Hadoop Data Node - http://localhost:9864/
Airflow UI - http://localhost:8085/  -> username: admin, password: airflow
Spark Worker Node - http://localhost:8081/

Both are same
http://localhost:8081/ - http://0.0.0.0:8081/




inside spark_project directory 
1. docker ps
#use below command to go inside hadoop
2. docker exec -it <container_name> sh
   docker exec -it intelligent_kilby sh

check hadoop file
hadoop fs -ls /


#after running command -> df.write.saveAsTable(table_name)
cd /root
ls
hadoop fs -mkdir /financd_data
hadoop fs -put /root/spark-warehouse/finance_complaint/* /finance_data
hadoop fs -ls /finance_data


#How to delete directory from hadoop
hadoop fs -rmr /financd_data
cd spark-warehouse
ls
rm -r financd_data
ls



######################################################################################
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/Spark_Project$ PROJECT_DIR=$(pwd)
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/Spark_Project$ docker pull avnish327030/spark-hadoop-airflow
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/Spark_Project$ docker image tag  avnish327030/spark-hadoop-airflow spark-hadoop-airflow
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/Spark_Project$ docker run -it -p 9870:9870 -p 8088:8088 -p 8080:8080 -p 18080:18080 -p 9000:9000 -p 8888:8888 -p 9864:9864 -p 8085:8085 -p 8793:8793 -p 8081:8081 -v $PROJECT_DIR/project/notebook:/root/ipynb -v $PROJECT_DIR/project/airflow:/home/airflow -v $PROJECT_DIR/data:/data avnish327030/spark-hadoop-airflow
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/Spark_Project$ docker ps
CONTAINER ID   IMAGE                               COMMAND                CREATED         STATUS         PORTS                                                                                                                                                                                                                                NAMES
3c1a472320e7   avnish327030/spark-hadoop-airflow   "./airflow-start.sh"   2 minutes ago   Up 2 minutes   0.0.0.0:8080-8081->8080-8081/tcp, 0.0.0.0:8085->8085/tcp, 0.0.0.0:8088->8088/tcp, 0.0.0.0:8793->8793/tcp, 0.0.0.0:8888->8888/tcp, 0.0.0.0:9000->9000/tcp, 0.0.0.0:9864->9864/tcp, 0.0.0.0:9870->9870/tcp, 0.0.0.0:18080->18080/tcp   intelligent_kilby
dell@dell-Latitude-3410:~/Desktop/Ajay/Ineuron/Spark_Project$ docker exec -it intelligent_kilby sh
# hadoop fs -ls /
# hadoop fs -ls /     
# cd /root
# ls
Untitled.ipynb	derby.log  ipynb  metastore_db	spark-warehouse
# cd ipynb
# ls
# cd ..
# ls
Untitled.ipynb	derby.log  ipynb  metastore_db	spark-warehouse
# hadoop fs -mkdir /finance_data
# hadoop fs -put /root/spark-warehouse/finance_complaint/* /financd_data
2023-03-03 15:32:10,674 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
2023-03-03 15:32:13,777 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
2023-03-03 15:32:13,910 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
2023-03-03 15:32:13,987 INFO sasl.SaslDataTransferClient: SASL encryption trust check: localHostTrusted = false, remoteHostTrusted = false
# hadoop fs -ls /financd_data
Found 5 items
-rw-r--r--   1 root supergroup          0 2023-03-03 15:32 /financd_data/_SUCCESS
-rw-r--r--   1 root supergroup     328867 2023-03-03 15:32 /financd_data/part-00000-4e8f8264-69a7-4e76-bb74-36896b3b4a32-c000.snappy.parquet
-rw-r--r--   1 root supergroup     359324 2023-03-03 15:32 /financd_data/part-00001-4e8f8264-69a7-4e76-bb74-36896b3b4a32-c000.snappy.parquet
-rw-r--r--   1 root supergroup     389803 2023-03-03 15:32 /financd_data/part-00002-4e8f8264-69a7-4e76-bb74-36896b3b4a32-c000.snappy.parquet
-rw-r--r--   1 root supergroup     310221 2023-03-03 15:32 /financd_data/part-00003-4e8f8264-69a7-4e76-bb74-36896b3b4a32-c000.snappy.parquet
#


############################################################################################


#example_for_ec2_tunnel.txt
# Open new terminal
ssh -i "bigdatahiveProject.pem" ec2-user@ec2-43-205-239-231.ap-south-1.compute.amazonaws.com -o "ServerAliveInterval 30" -L 2081:localhost:2041 -L 4888:localhost:4888 -L 4889:localhost:4889 -L 2080:localhost:2080 -L 8050:localhost:8050 -L 8051:localhost:8051 -L 4141:localhost:4141 -L 4090:localhost:4090 -L 3180:localhost:3180 -L 50075:localhost:50075 -L 50070:localhost:50070 -L 50010:localhost:50010 -L 3077:localhost:3077 -L 4080:localhost:4080 -L 9870:localhost:9870 -L 8188:localhost:8188 -L 9864:localhost:9864 -L 8042:localhost:8042 -L 8088:localhost:8088 -L 8080:localhost:8080 -L 8081:localhost:8081 -L 10000:localhost:10000 -L 6080:localhost:6080 -L 8998:localhost:8998 -L 3306:localhost:3306
