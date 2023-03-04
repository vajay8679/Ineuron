from src.config.environment import EnvironmentVariable
from src.config.spark_manager import spark_session
from pyspark.sql import DataFrame
from pyspark.sql import types as T
from pyspark.sql import functions as F
from src import entity as E
env = EnvironmentVariable()
from src.logging import logging


def read_data_of_kafka_topic(topic_name,schema:T.StructType)->DataFrame:
    """
    topic_name: Kafka topic name
    schema: Schema of your dataset
    """
    try:
        logging.info(f"Reading data from kafka topic {topic_name}")
        df = (spark_session
          .read
          .format("kafka")
          .option("kafka.bootstrap.servers", env.kafka_cloud.bootstrap_server)
          .option("kafka.security.protocol", "SASL_SSL")
          .option("kafka.sasl.jaas.config",
                  "org.apache.kafka.common.security.plain.PlainLoginModule  required username='{}' password='{}';".format(env.kafka_cloud.api_key, env.kafka_cloud.api_secret))
          .option("kafka.ssl.endpoint.identification.algorithm", "https")
          .option("kafka.sasl.mechanism", "PLAIN")
          .option("kafka.group.id", "eshop")
          .option("subscribe", topic_name)
          .option("startingOffsets", "earliest")
          .option("failOnDataLoss", "false")
          .load()
          )
        logging.info(f"Extracting data from received dataframe from kafka topic using schema {schema}")
        df = df.select(F.decode(F.col("value"),charset="utf-8").alias("value"))
        df = df.select(F.from_json(F.col("value"),schema=schema).alias("table")).select("table.*")
        return df
    except Exception as e:
        raise e



def write_kafka_to_s3():
    """
    This function real all data from kafka topic and dump these records to s3 bucket
    """
    logging.info("Started reading data from kafka topic")
    fact_sale = read_data_of_kafka_topic(topic_name=env.kafka_topic.fact_sales,schema=E.FactSalesSchema)
    dim_employee = read_data_of_kafka_topic(topic_name=env.kafka_topic.dim_employees,schema = E.DimEmployeeSchema)
    dim_customer = read_data_of_kafka_topic(topic_name=env.kafka_topic.dim_customers,schema=E.DimCustomerSchema)
    dim_product = read_data_of_kafka_topic(topic_name=env.kafka_topic.dim_products,schema=E.DimProductSchema)
    dim_date = read_data_of_kafka_topic(topic_name=env.kafka_topic.dim_dates,schema=E.DimDateSchema)
    dim_location = read_data_of_kafka_topic(topic_name=env.kafka_topic.dim_locations,schema =E.DimLocationSchema)
    logging.info("All topic data has been read.")
    fact_sale.show()
    dim_employee.show()
    dim_customer.show()
    dim_product.show()
    dim_date.show()
    dim_location.show()

    logging.info("Preparing s3 bukcet url to dump data from kafka topic")
    #lets prepare s3 bukcet file path
    #s3a://bucket_name/kafka-topic/topic_name
    s3_uri = "s3a://{bukcet_name}/kafka-topic/{topic_name}"
    fact_sales_s3_uri = s3_uri.format(bukcet_name=env.aws.bucket_name,topic_name=env.kafka_topic.fact_sales)
    dim_employees_s3_uri = s3_uri.format(bukcet_name=env.aws.bucket_name,topic_name=env.kafka_topic.dim_employees)
    dim_customers_s3_uri = s3_uri.format(bukcet_name=env.aws.bucket_name,topic_name=env.kafka_topic.dim_customers)
    dim_products_s3_uri = s3_uri.format(bukcet_name=env.aws.bucket_name,topic_name=env.kafka_topic.dim_products)
    dim_dates_s3_uri = s3_uri.format(bukcet_name=env.aws.bucket_name,topic_name=env.kafka_topic.dim_dates)
    dim_locations_s3_uri = s3_uri.format(bukcet_name=env.aws.bucket_name,topic_name=env.kafka_topic.dim_locations)
    s3_bucket_root_url = f"s3a://{env.aws.bucket_name}"
    logging.info(f"All info will be written in bucket: {s3_bucket_root_url}")
    # print(fact_sales_s3_uri)
    logging.info(f"Fact sales has {fact_sale.count()} row.")
    fact_sale.write.parquet(fact_sales_s3_uri,mode="overwrite")

    logging.info(f"Dimension employee has {dim_employee.count()} row.")
    dim_employee.write.parquet(dim_employees_s3_uri,mode="overwrite")

    logging.info(f"Dimension customer has {dim_customer.count()} row.")
    dim_customer.write.parquet(dim_customers_s3_uri,mode="overwrite")

    logging.info(f"Dimension product has {dim_product.count()} row.")
    dim_product.write.parquet(dim_products_s3_uri,mode="overwrite")

    logging.info(f"Dimension date has {dim_date.count()} row.")
    dim_date.write.parquet(dim_dates_s3_uri,mode="overwrite")

    logging.info(f"Dimension location has {dim_location.count()} row.")
    dim_location.write.parquet(dim_locations_s3_uri,mode="overwrite")

    






