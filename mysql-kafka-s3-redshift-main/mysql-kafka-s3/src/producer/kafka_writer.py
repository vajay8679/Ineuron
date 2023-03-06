from src import utils as U
from src.entity import ExportManagementSchema,TableMetaData
from src.config.environment import EnvironmentVariable
from pyspark.sql import functions as F
from pyspark.sql import types as T
from src.config.spark_manager import spark_session
from src.logging import logging
import calendar
import os 
from pyspark.sql import DataFrame
env = EnvironmentVariable()
monthName=F.UserDefinedFunction(lambda x:calendar.month_name[x],T.StringType())

def write_df_to_kafka_topic(df:DataFrame,topic_name:str):
    logging.info("Preparing record of dimesion customer table to push to kafka topic")
    df = df.selectExpr("to_json(struct(*)) AS value")
    (df.write.format("kafka")
             .option("kafka.bootstrap.servers", env.kafka_cloud.bootstrap_server)
             .option("kafka.security.protocol", "SASL_SSL")
             .option("kafka.sasl.jaas.config",
                     "org.apache.kafka.common.security.plain.PlainLoginModule  required username='{}' password='{}';".format(
                         env.kafka_cloud.api_key, env.kafka_cloud.api_secret))
             .option("kafka.ssl.endpoint.identification.algorithm", "https")
             .option("kafka.sasl.mechanism", "PLAIN")
             .option("checkpointLocation", os.path.join("kafka_checkpoint"))
             .option("topic", topic_name).save())

    logging.info(f"df has been pushed to kafka topic {topic_name}")

def produce_data_to_kafka_topics():
    try:
        logging.info(f"Starting function produce data to kafka topic")
        #Fetch all customer detail
        logging.info(f"Creating environment variable object")
        
        last_sent_customer_id=  U.get_last_sent_id(topic_name=env.kafka_topic.dim_customers)
        logging.info(f"Last customer id already sent: {last_sent_customer_id}")
        if last_sent_customer_id is None:
            last_sent_customer_id=0
        else:
            last_sent_customer_id=int(last_sent_customer_id)
        query = f"select * from customers"
        print(query)
        logging.info(f"Fetch customer record from mysql using query: \n[{query}]")
        df_cust = U.get_mysql_record_as_dataframe(query=query,update_column_attr=True)
        logging.info(f"Number of customer record found: [{df_cust.count()}]")

        #Fetch all employee
        last_sent_emp_id=  U.get_last_sent_id(topic_name=env.kafka_topic.dim_employees)
        logging.info(f"Last employee id already sent: {last_sent_emp_id}")
        if last_sent_emp_id is None:
            last_sent_emp_id=0
        else:
            last_sent_emp_id = int(last_sent_emp_id)
        query = f'select * from employees'
        logging.info(f"Fetch employee record from mysql using query: \n[{query}]")
        df_emp= U.get_mysql_record_as_dataframe(query=query,update_column_attr=True)
        logging.info(f"Number of employee record found: [{df_emp.count()}]")

        #Fetch only new order details
        last_sent_order_id=  U.get_last_sent_id(topic_name=env.kafka_topic.fact_sales)
        logging.info(f"Last order id already sent: {last_sent_emp_id}")
        if last_sent_order_id is None:
            last_sent_order_id=0
        else:
            last_sent_order_id=int(last_sent_order_id)
        query = f'select * from orders  where orderNumber>{last_sent_order_id}'
        logging.info(f"Fetch order record from mysql using query: \n[{query}]")
        df_order = U.get_mysql_record_as_dataframe(query=query,update_column_attr=True)
        query = f'select * from orderdetails  where orderNumber>{last_sent_order_id}'
        logging.info(f"Fetch order detail record from mysql using query: \n[{query}]")
        df_order_detail = U.get_mysql_record_as_dataframe(query=query,update_column_attr=True)

        logging.info(f"Number of order record found: [{df_order.count()}]")
        logging.info(f"Number of order details record found: [{df_order_detail.count()}]")
        #fetch all product
        latest_sent_created_product=  U.get_last_sent_id(topic_name=env.kafka_topic.dim_products)
        logging.info(f"Last created product already sent: {latest_sent_created_product}")
        if latest_sent_created_product is None:
            latest_sent_created_product='1900-01-01'
        query = f"select * from products"
        print(query)
        logging.info(f"Fetch product record from mysql using query: \n[{query}]")
        df_product = U.get_mysql_record_as_dataframe(query=query,update_column_attr=True)
        logging.info(f"Number of product record found: [{df_product.count()}]")


        query = f"select * from productlines"
        print(query)
        logging.info(f"Fetch productlines record from mysql using query: \n[{query}]")
        df_productlines = U.get_mysql_record_as_dataframe(query=query,update_column_attr=True)
        logging.info(f"Number of productlines record found: [{df_productlines.count()}]")


        if df_order.count()==0:
            logging.info(f"As 0 new order details found hence nothing will be sent on kafka topic")
            return None

        

        logging.info("Preparing dimension employee record to sent on kafka.")
        dim_employee = df_emp.select(F.col(df_emp.employeeNumber).alias("salesRepEmployeeId"),
                            F.col(df_emp.firstName),
                            F.col(df_emp.lastName),
                            F.col(df_emp.extension),
                            F.col(df_emp.email),
                            F.col(df_emp.officeCode),
                            F.col(df_emp.jobTitle),
                            F.col(df_emp.reportsTo)
                            )
        logging.info(f"Total number of employee record: [{dim_employee.count()}]")
        dim_employee.filter(F.col("salesRepEmployeeId")>last_sent_emp_id)
        logging.info(f"Number of employee record will be sent to kafka: [{dim_employee.count()}]")
        dim_employee.show()



        logging.info("Preparing dimension location record to be sent on kafka.")
        dim_location = df_cust.select(
                        F.col(df_cust.city),
                        F.col(df_cust.state),
                        F.col(df_cust.postalCode),
                        F.col(df_cust.country)
                    )
                    #remove duplicate id
        dim_location = dim_location.dropDuplicates()
        logging.info("Number dimension location record to be sent on kafka.")
        dim_location = dim_location.select(dim_location.columns).withColumn("locationId",F.monotonically_increasing_id())
        dim_location.show()

        logging.info("Preparing dimension product record to be sent on kafka.")
        columns = ['productCode',
                'productName',
                'productScale',
                'productVendor',
                'productDescription',
                'quantityInStock',
                'buyPrice',
                'MSRP',
                'productCreatedTimestamp'
                ]

        logging.info(f"Total number of total product: {df_product.count()}")
        dim_product = df_product.filter(F.col('productCreatedTimestamp')>latest_sent_created_product)
        logging.info(f"Number of product record to be sent on kafka: [{dim_product.count()}]")
        dim_product.show()


        logging.info("Preparing dimension date record to be sent on kafka.")
        dim_date = (df_order.select(
            F.col(df_order.orderDate).alias('date'),
            F.dayofweek(df_order.orderDate).alias('dayOfWeek'),
            F.dayofmonth(df_order.orderDate).alias('dayOfMonth'), 
            F.weekofyear(df_order.orderDate).alias('weekNumber'), 
            F.month(df_order.orderDate).alias('monthNumber'), 
            monthName(F.month(df_order.orderDate)).alias('monthName'),
            F.year(df_order.orderDate).alias('year'),
        ).orderBy(F.col('date')))

        dim_date.printSchema()
        logging.info(f"Number of record we have in dimension date table: [{dim_date.count()}]")
        dim_date = dim_date.dropDuplicates()
        logging.info(f"Number of record we have after removing duplicates from dimension date table: [{dim_date.count()}]")



        logging.info("Preparing fact sales record to be sent on kafka.")

        logging.info("Creating list of all dataframe along with their table name")
        all_df = [df_cust,df_emp,df_order_detail,df_order,df_productlines,df_product,dim_location,dim_date]
        table_names=["customers","employees","orderDetails","orders","productLines","products",'location','date']
        table_df_dict=dict(zip(table_names,all_df))
        

        table = TableMetaData(table_df_dict)
        logging.info(f"Table metadata info has been created [{table}]")
        df_product.createOrReplaceTempView("products")
        df_order_detail.createOrReplaceTempView("orderDetails")
        df_order.createOrReplaceTempView("orders")
        df_cust.createOrReplaceTempView("customers")
        df_emp.createOrReplaceTempView("employees")
        df_productlines.createOrReplaceTempView("productLines")
        logging.info(f"Create temp table using Pyspark dataframes.")

        sql = spark_session.sql
        query = f"""
                        select
                        prod.{table.products.productCode} as productId,
                        cust.{table.customers.customerNumber} as customerId,
                        cust.{table.customers.salesRepEmployeeNumber} as salesRepEmployeeNumber,
                        loc.{table.location.locationId} as locationId,
                        ord.{table.orders.orderNumber} as orderId,
                        ord.{table.orders.orderDate} as orderDate,
                        {table.orders.status},
                        {table.orderDetails.quantityOrdered} quantity,
                        {table.orderDetails.priceEach } unitPrice
                        from {table.name.orders} as ord
                        inner join {table.name.orderDetails} as ordDetails
                        on ord.{table.orders.orderNumber}=ordDetails.{table.orderDetails.orderNumber}
                        inner join {table.name.products} as prod
                        on prod.{table.products.productCode}=ordDetails.{table.orderDetails.productCode}
                        inner join {table.name.customers} as cust
                        on cust.{table.customers.customerNumber}=ord.{table.orders.customerNumber}
                        inner join {table.name.location} as loc 
                        on loc.{table.location.postalCode}=cust.{table.customers.postalCode}
                        inner join {table.name.date} as orderdate
                        on orderdate.{table.date.date}=ord.{table.orders.orderDate}
                        """
        logging.info(f"Fact sales query is prepared.\n {query}")
        fact_sales= sql(query)
        logging.info(f"Number of record found in fact sales table: [{fact_sales}]")

        logging.info("Preparing dimension customers record to be sent on kafka.")

        customer_column = ['customerNumber',
                'customerName',
                'contactFirstName',
                'contactLastName',
                'phone',
                'creditLimit',
                'addressLine1',
                'addressLine2',
                ]
        logging.info(f"Total customer in database [{df_cust.count()}]")
        dim_customer = df_cust.select(customer_column).filter(F.col("customerNumber")>last_sent_customer_id)
        print(f"Number of  customerrecord to be sent on kafka: [{df_cust.count()}]")
        dim_customer.show()
        
        last_orderNumber = fact_sales.agg({"orderId":"max"}).take(1)[0][0]
       
        if last_orderNumber is not None:
            write_df_to_kafka_topic(df=fact_sales,topic_name=env.kafka_topic.fact_sales)
            U.update_last_sent_id(topic_name=env.kafka_topic.fact_sales,last_sent_id=last_orderNumber)
            logging.info(f"Update last order id {last_orderNumber} in export management table.")
            


        # U.update_last_sent_id(topic_name="fact_sales",last_sent_id=)
        last_customerNumber = dim_customer.agg({"customerNumber":"max"}).take(1)[0][0]
        if last_customerNumber is not None:
            write_df_to_kafka_topic(df=dim_customer,topic_name=env.kafka_topic.dim_customers)
            U.update_last_sent_id(topic_name=env.kafka_topic.dim_customers,last_sent_id=last_customerNumber)
            logging.info(f"Update last customer Number id {last_orderNumber} in export management table.")
            

        last_productCreatedTimestamp = dim_product.agg({"productCreatedTimestamp":"max"}).take(1)[0][0]
        if last_productCreatedTimestamp is not None:
            logging.info("Preparing record of dimension product table to push to kafka topic")
            last_productCreatedTimestamp = last_productCreatedTimestamp.strftime("%Y-%m-%d %H:%M:%S")
            write_df_to_kafka_topic(df=dim_product,topic_name=env.kafka_topic.dim_products)
            U.update_last_sent_id(topic_name=env.kafka_topic.dim_products,last_sent_id=last_productCreatedTimestamp)
            logging.info(f"Update last product created timestamp {last_productCreatedTimestamp} in export management table.")

        last_employeeNumber = dim_employee.agg({"salesRepEmployeeId":"max"}).take(1)[0][0]
        if last_employeeNumber is not None:
            logging.info("Preparing record of dimension employee table to push to kafka topic")
            write_df_to_kafka_topic(df=dim_employee,topic_name=env.kafka_topic.dim_employees)
            U.update_last_sent_id(topic_name=env.kafka_topic.dim_employees,last_sent_id=last_employeeNumber)
            logging.info(f"Update last employee number {last_employeeNumber} in export management table.")

        if dim_location.count()>0:
            logging.info("Preparing record of dimension location table to push to kafka topic")
            write_df_to_kafka_topic(df=dim_location,topic_name=env.kafka_topic.dim_locations)
            logging.info("Dimension location record is pushed to kafka topic")

        if dim_date.count()>0:
            logging.info("Preparing record of dimension location table to push to kafka topic")
            write_df_to_kafka_topic(df=dim_date,topic_name=env.kafka_topic.dim_dates)
            logging.info("Dimension date record is pushed to kafka topic")


       
       
        



    except Exception as e:
        raise e


if __name__=="__main__":
    produce_data_to_kafka_topics()
