from src.pipeline.s3_to_redshift import transfer_data_from_s3_to_redshift
# from src.config.spark_manager import spark_session
# from src.entity import FactSalesSchema
if __name__=="__main__":
    transfer_data_from_s3_to_redshift()
    # df= spark_session.read.schema(FactSalesSchema).parquet("s3a://eshop-redshift/kafka-topic/fact_sales/")
    # df.printSchema()

