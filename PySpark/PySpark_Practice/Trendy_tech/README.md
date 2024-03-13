# 1. what is meant by Data Modeling?

A way to structure your data so that it fits your needs in the best possible way.

Needs can be different based on what system are we Modeling & who is the end user?

model the table in a way that reduces the storage space,
modeling it in a way that queries run faster,
modeling in a way that user can easily query
etc..

In a transactional system (OLTP) we generally use Normalization -
It's a technique to divide one big table into multiple smaller tables with an intent to reduce the redundancy.

However, OLTP systems are not meant to do reporting?
our reporting work can overload the OLTP systems

Datawarehouse (DWH) is best fit for reporting purpose (OLAP)

What is DWH - it's like a Database but the objective is to make your analytical queries faster.

Dimensional Modeling is one of the well know techniques for modeling a DWH.

here are 2 definitions that you should know -

- "Dimensional Modeling is a design technique for Databases intended to support end user queries in a DWH"
Ralph Kimball

- the process of modeling a business process into a series of facts and dimension tables designed for analysis.

Key highlights of a Transactional DB design
- designed towards fast maintenance of data
- inserting and updating is quick
- very small sets of data is retrieved in a query
- Data consistency is critical
- Focus is on customers who are entering the data

Reporting DB design
- copy of transactional data (not exactly the same way)
- the resulting model reflects the kind of questions business wants to ask rather than the functions of underlying operational system.
- Descriptive data like customer name, customer address is separated from the quantity data such as order quantity, order amount.
- larger datsets
- insert and update speed is not relevant
- performance focus is on retrieving the data quickly.

fun facts regarding facts & dimension tables
=> dimension tables would contain more than 90% of total columns, however data in fact table would be more as we keep getting new data.
=> in fact table the foreign keys might take more space then the actual fact information .

When storage was costly, Dimension modeling ruled and it's even ruling today.

Now a days OBT (one big table) is also becoming popular, because storage space is not a big concern. We can pay little extra for storage if that helps us to build faster queries, and it's easy for end users to query it.

will OBT take a lead over Dimensional modeling in the future?


# 2. Data Engineering - 10 Managerial round Interview Questions

1. what is the size of your cluster  - 16 Node - 64GB - 4core

2. How much data you deal with on a daily basis

3. what is your role in your big data project

4. Are you using onpremise setup(locally) or you are working on cloud - cloud

5. which big data distribution are you using -  Apache Hadoop, Apache Spark, MongoDB, Cassandra, and Hive.

6. whats the most challenging thing that you faced in your project & how you overcome that.

7. what is the configuration of each node in the cluster - single node -14gb - 4 cpu -core

8. Did you face any performance challenge & how did you optimize - auto scaling - worker node from 2-8

9. day to day work that you do

10. How do you estimate amount of resources for your job.

Do mention, how would you answer these in the comments section.

what other Interview questions you have faced in the managerial round?


# 3. 20 Recently asked Pyspark Interview questions

1. Difference between client and cluster mode

In cluster mode, the driver runs on a cluster, while in client mode, the driver runs on the local machine. We also discussed the advantages and disadvantages of each mode. Cluster mode is a good choice for production workloads that require high availability, scalability, and security.


2. what is partition skew, reasons for it. How to solve partition skew issues?


Ideally, the data in the partitions should be uniformly distributed. Data skew is when one or some partitions have significantly more data compared to other partitions. Data-skew is usually the result of operations that require re-partitioning the data, mostly join and grouping ( GroupBy ) operations

handle skenness ->

Solution 1: Improve table partitioning
Option 1: Filter the skewed key value in advance
Option 2: Pick a different partition or distribution key
Option 3: Add more partition or distribution keys
Option 4: Use round-robin distribution

Solution 2: Improve the query plan
Option 1: Use the CREATE STATISTICS statement
Option 2: Use SKEWFACTOR


Custom Partitioning: Instead of relying on Spark’s default partitioning strategy, implementing a custom partitioning strategy can help distribute data more evenly across partitions. For example, range partitioning can be more effective when dealing with numeric keys.
Salting: Salting is a technique where a random value (salt) is appended to the key, which helps distribute the data more evenly across partitions. This can be particularly useful when dealing with hot keys.
Dynamic Partition Pruning: Dynamic partition pruning is a technique used in Spark to optimize join operations by skipping the scanning of irrelevant partitions in both datasets. This can help improve performance in the case of data skewness caused by join operations.
Splitting Skewed Data: Another strategy is to split the skewed data across multiple partitions. This involves identifying the skewed keys and redistributing the data associated with these keys.
Avoid GroupBy for Large Datasets: When possible, avoid using GroupBy operations on large datasets with non-unique keys. Alternatives such as reduceByKey, which performs a combine operation locally on each partition before performing the grouping operation, can be more efficient.

3. what is a broadcast join in apache spark

Broadcast join is an optimization technique used in the Spark SQL engine. It is utilized when one of the DataFrames is small enough to be stored in the memory of all executor nodes. This technique greatly improves the performance of join operations by minimizing data shuffling across the network.

from pyspark.sql.functions import broadcast
df_large.join(broadcast(df_small), join_condition)

This helps in improving query performance by avoiding redundant data transfers and reducing network overhead

4. what is the difference between partition and bucketing

Partitioning and bucketing are both techniques for organizing data. Partitioning is best for low cardinality columns, while bucketing is best for high cardinality columns. 

Partitioning
Groups similar types of data based on a specific column. Partitioning splits data into separate folders on disk based on one or multiple columns. Partitioning is useful when the column has low cardinality and a high search query. For example, creating a partition by country name.

Bucketing
Combines data within a partition into a number of equal groups, or files. Bucketing uses a hash function on one or more columns to assign data to buckets. Bucketing is effective for low volume data for a given partition. 

Partitioning and bucketing can also help improve query performance. Partitioning reduces the query latency by scanning only relevant partitioned data instead of the whole data set. Bucketing improves query performance by grouping similar data together and reducing the number of files to scan during processing. 


Before going into Bucketing, we need to understand what Partitioning is. Let us take the below table as an example. Note that I have given only 12 records in the below example for beginner level understanding. In real-time scenarios you might have millions of records.

enter image description here

saleid productid transdate   amount
1         P1     20-01-2023  2000
2         P1     21-01-2023  2500
3         P1     21-01-2023  3000
4         P1     22-01-2023  3500
5         P2     23-01-2023  4000
6         P2     24-01-2023  5000
7         P2     25-01-2023  6000
8         P2     26-01-2023  7000


PARTITIONING
---------------------
Partitioning is used to obtain performance while querying the data. For example, in the above table, if we write the below sql, it need to scan all the records in the table which reduces the performance and increases the overhead.

select * from sales_table where product_id='P1'

To avoid full table scan and to read only the records related to product_id='P1' we can partition (split hive table's files) into multiple files based on the product_id column. By this the hive table's file will be split into two files one with product_id='P1' and other with product_id='P2'. Now when we execute the above query, it will scan only the product_id='P1' file.

../hive/warehouse/sales_table/product_id=P1
../hive/warehouse/sales_table/product_id=P2

The syntax for creating the partition is given below. Note that we should not use the product_id column definition along with the non-partitioned columns in the below syntax. This should be only in the partitioned by clause.

create table sales_table(sales_id int,trans_date date, amount int) 
partitioned by (product_id varchar(10))

Cons : We should be very careful while partitioning. That is, it should not be used for the columns where number of repeating values are very less (especially primary key columns) as it increases the number of partitioned files and increases the overhead for the Name node.



BUCKETING
------------------
Bucketing is used to overcome the cons that I mentioned in the partitioning section. This should be used when there are very few repeating values in a column (example - primary key column). This is similar to the concept of index on primary key column in the RDBMS. In our table, we can take Sales_Id column for bucketing. It will be useful when we need to query the sales_id column.

Below is the syntax for bucketing.

create table sales_table(sales_id int,trans_date date, amount int) 
partitioned by (product_id varchar(10)) Clustered by(Sales_Id) into 3 buckets

Here we will further split the data into few more files on top of partitions.

enter image description here

../hive/warehouse/sales_table/product_id=P1/000000_0 ---bucket 0
../hive/warehouse/sales_table/product_id=P1/000001_0 ---bucket 1
../hive/warehouse/sales_table/product_id=P1/000002_0 ---bucket 2
../hive/warehouse/sales_table/product_id=P2/000000_0 ---bucket 0
../hive/warehouse/sales_table/product_id=P2/000001_0 ---bucket 1
../hive/warehouse/sales_table/product_id=P2/000002_0 ---bucket 2


Since we have specified 3 buckets, it is split into 3 files each for each product_id. It internally uses modulo operator to determine in which bucket each sales_id should be stored. For example, for the product_id='P1', the sales_id=1 will be stored in 000001_0 file (ie, 1%3=1), sales_id=2 will be stored in 000002_0 file (ie, 2%3=2),sales_id=3 will be stored in 000000_0 file (ie, 3%3=0) etc.


5. What are different types of joins in Spark

you can expect to encounter five primary types of joins:
Broadcast Hash Join.
Shuffle Hash Join.
Sort Merge Join.
Cartesian Join.
Broadcast Nested Loop Join.


Comprehensive Guide to PySpark Sql Joins
inner and cross joins.
outer joins (left, right, full)
left semi and, left anti join.

SQL Join Clause	                       PySpark Join Type	                           Description
INNER JOIN	                           inner	                          Returns all rows when there is at least one match in BOTH tables
CROSS JOIN	                           cross	                          Returns all rows from the left table multiplied by all rows from the right table (Cartesian product)
LEFT OUTER JOIN (a.k.a LEFT JOIN)      left, leftouter, left_outer        Returns all rows from the left table, and the matched rows from the right table
RIGHT OUTER JOIN (a.k.a RIGHT JOIN)    right, rightouter, right_outer	  Returns all rows from the right table, and the matched rows from the left table
FULL OUTER JOIN		                   outher, full, fullouther, full_outher  Returns all rows when there is a match in ONE of the tables
LEFT SEMI JOIN	                       semi, leftsemi, left_semi	       Returns all rows from the left table for which there is at least one match in the right table
LEFT ANTI JOIN	                       anti, leftanti, left_anti	       Returns all rows from the left table for which there is no match in the right table



https://iomete.com/resources/reference/pyspark/pyspark-join

Glossary for PySpark Joins
DataFrame
DataFrame: A distributed collection of data organized into named columns, conceptually equivalent to a table in a relational database. DataFrames can be manipulated using both SQL and standard Python-like operations.

Join
Join: An operation in relational databases and PySpark that combines rows from two or more DataFrames based on a related column between them.


Inner Join
Inner Join: A type of join that returns rows from both DataFrames where the join condition is true. It only returns matching rows.

df_joined = df_employees.join(df_departments, df_employees.dept_id == df_departments.dept_id)


Outer Join
Outer Join: A type of join that returns all rows from one or both DataFrames where there is a match. Depending on the type (left, right, or full), non-matching rows are filled with null values.

df1.join(df2, join_condition, "full") # "outer", "fullouter", "full_outer" can also be used



Left Outer Join
Left Outer Join: A join that returns all rows from the left DataFrame and matched rows from the right DataFrame. Non-matching rows from the right DataFrame are filled with nulls.

df1.join(df2, join_condition, "left") # "leftouter", "left_outer" can be used


Right Outer Join
Right Outer Join: A join that returns all rows from the right DataFrame and the matched rows from the left DataFrame. Non-matching rows from the left DataFrame are filled with nulls.

df1.join(df2, join_condition, "right") # "rightouter", "right_outer" can be used


Full Outer Join
Full Outer Join: A join that returns all rows from both the left and right DataFrames. Rows that do not match on either side are filled with nulls.

df1.join(df2, join_condition, "full") # "outer", "fullouter", "full_outer" can also be used


Cross Join
Cross Join: A join operation that returns the Cartesian product of the rows from the DataFrames involved. It combines each row of the first DataFrame with every row of the second DataFrame.

df1.crossJoin(df2)




Left Semi Join
Left Semi Join: A join that returns all rows from the left DataFrame that have a corresponding match in the right DataFrame. It's used for filtering rather than combining DataFrames.

df_purchasers = df_users.join(df_purchases, df_users.id == df_purchases.user_id, "left_semi")


Left Anti Join
Left Anti Join: A join that returns all rows from the left DataFrame that do not have a corresponding match in the right DataFrame. It's useful for identifying non-matching entries.

df_non_purchasers = df_users.join(df_purchases, df_users.id == df_purchases.user_id, "left_anti")


Cartesian Product
Cartesian Product: The result of a cross join, where each row from one DataFrame is combined with each row from another DataFrame, resulting in every possible combination of rows.

SparkSession
SparkSession: The entry point to programming Spark with the DataFrame and Dataset API. It's used to create DataFrames, register DataFrames as tables, and execute SQL over tables, among other functions.

Broadcast Join
Broadcast Join: A type of join in Spark where the smaller DataFrame is sent to every node containing partitions of the larger DataFrame for more efficient join operations. It's beneficial for small to medium-sized DataFrames.

Partitioning
Partitioning: The process of dividing a large DataFrame into smaller pieces (partitions) that can be processed in parallel. Effective partitioning is crucial for optimizing join operations in distributed computing.


6. why count when used with group by is a transformation else its an action.

When "count" is used with "group by," it is typically viewed as a transformation because it is applied to the data and helps to summarize it. On the other hand, when "count" is used with certain other database operations, such as "having" or "order by," it is often considered an action because it is used to filter or sort the data. Ultimately, the context in which "count" is used will determine whether it is considered a transformation or an action.

In your case you are calling groupBy on dataframe which returns RelationalGroupedDataset object, and you are calling count on grouped Dataset which returns a Dataframe , so its a transformation since it doesn't gets the data to the driver and initiates the DAG execution.

7. If your spark job is running slow how would you approach to debug it.

Spark jobs might fail due to out of memory exceptions at the driver or executor end. When troubleshooting the out of memory exceptions, you should understand how much memory and cores the application requires, and these are the essential parameters for optimizing the Spark appication.

- Check the execution plan: Use the explain() function to analyze the execution plan and identify any performance bottlenecks.
- Optimize the code: Review your code and look for areas where you can optimize it, such as avoiding unnecessary shuffles or reducing the number of partitions.
- Increase memory: Increasing the amount of memory available to Spark can help improve performance. You  can do this by adjusting the  -> spark.executor.memory and spark.driver.memory configuration properties.
- Use different storage formats: Different storage formats may

Identify the problem
    Check the Spark configuration
    Check for data skewness
    Check the execution plan
    Check for code issues
Enable debugging mode
    Set the log level to "DEBUG" in the Spark configuration
    Use thread dumps to debug a specific task
    Use breakpoints and IDE debugging tools to set breakpoints, step through code, and inspect variables
Check resources
    Check for resource contention
    Ensure that there are enough resources (CPU, memory, and cluster nodes) available for the job
    Adjust resource configurations, such as the number of executors and executor memory, if necessary


8. Difference between managed table & external table. When do you go about creating exernal tables.

A managed table is a table that is created, maintained, and optimized by your database system, while an external table is a table that is stored in a separate data source, such as a file or another database. The main difference between these two types of tables is that managed tables are optimized for performance, while external tables are not.

You might choose to use an external table if you are working with data from a third-party source or if you need to access data from a legacy system. In the case of an external table, you would typically create it using a tool like SQL Server's INSERT INTO EXTERNAL TABLE statement.

In case of managed table, schema and data is managed by Hive whereas to create external table you need to use external keyword in create table statement and you can also specify location of the dataset. In external table, Hive only manage meta data and data can be stored at any location in HDFS


9. Why we are not using mapreduce these days. what are similarities between spark and mapReduce.

MapReduce is still widely used in many industries, including finance, healthcare, and e-commerce. However, it is true that many organizations are moving towards using Apache Spark instead of MapReduce due to its similarities, flexibility, and performance improvements. Spark is a fast and general-purpose cluster computing system that can be used for a wide range of data processing tasks, including batch and real-time processing, machine learning, and graph processing. The similarities between the two systems include the distributed computing model, the use of a programming model based on functional programming.

Spark processes and retains data in memory for subsequent steps, whereas MapReduce processes data on disk. Spark is faster, utilizes RAM not tied to Hadoop's two-stage paradigm, and works well for small data sets that fit into a server's RAM. MapReduce is designed for batch processing and is not as fast as Spark. It is best suited where memory is limited and processing data size is so big that it would not fit in the available memory. 

there are some differences between the two: Processing Model: MapReduce is a batch processing model, where data is processed in batches. Spark, on the other hand, uses a more flexible processing model, allowing for real-time processing, interactive queries, and streaming data processing.

MapReduce is not ideal for real-time processing due to its limitations in terms of performance and response time. While MapReduce is efficient for processing large-scale data in batch mode, it lacks real-time performance.

10. How do you handle your pyspark code deployment, Explain about the CICD process.

There are several methods for handling PySpark code deployment, including using tools like SparkSubmit, Mesos, and Kubernetes. The Continuous Integration/Continuous Deployment (CICD) process involves integrating your code into a shared repository, building it, testing it, and automatically deploying it to production. This can be achieved using tools like Jenkins, CircleCI, Travis CI, and SparkSubmit with these tools helps to automate your code deployment process. It leads to faster deployment of code, ensures that your code is properly built and tested before deployment, and makes it easier for you to manage your deployment as your codebase grows.


Continuous Integration and Continuous Deployment ensure that changes and updates to data pipelines are automatically tested, integrated, and deployed to production, facilitating consistent and reliable data processing and delivery.

11. Have you used caching in your project, when & where do you consider using it.

Caching is a technique that stores data in a temporary storage location, or cache, so that it can be accessed more quickly. Caches are used in a variety of systems, including web applications, databases, and operating systems.

Here are some situations where you can use caching in Spark:
Reusing data: Caching can be useful when you need to perform multiple operations on the same dataset. This can be useful when:
    Reusing RDDs in iterative machine learning applications
    Reusing RDDs in standalone Spark applications
    RDD computation is expensive
    Frequent sub-set access is needed
    Using broadcast variables, especially when the same data needs to be shared efficiently across worker nodes
Repeated transformations: Caching can be beneficial when a repeated transformation takes a longer time to run. This can happen when the input is large or the logic is complicated.
Reducing recovery costs: Caching can help reduce the cost of recovery if one executor fails.


The rule of thumb for caching is to identify the Dataframe that you will be reusing in your Spark Application and cache it. Even if you don't have enough memory to cache all of your data you should go-ahead and cache it. Spark will cache whatever it can in memory and spill the rest to disk.

 Yes, caching can be used in Spark to improve performance by storing frequently accessed data in faster memory. It can be considered in project tasks that require iterative access to the same data, such as in machine learning algorithms, and processing large datasets. Caching can be set up at different levels, including within the Spark executor, method caching and in-memory caching. The right caching strategy for a Spark project depends on the specific use case and the amount of data being processed.  

12. how to estimate the amount of resources for your spark job.

Here's some information about estimating resources for a Spark job:
    Total memory
    The total memory for a Spark job is calculated as memory required by the driver plus the memory used by executors multiplied by the number of executors.

    Memory overhead
    Spark allocates a minimum of 384 MB for memory overhead in each executor, and the rest is allocated for the actual workload. The formula for calculating memory overhead is max(Executor Memory * 0.1, 384 MB).

    Heap memory
    Heap memory consists of reserved memory and Spark unified memory. Reserved memory is reserved for Spark engine-related tasks, and Spark unified memory is dedicated for storage and execution. The default values for both are 50%.

    Cores
    A core is a basic computation unit of a CPU, and a CPU may have one or more cores to perform tasks at a given time. In Spark, this controls the number of parallel tasks an executor can run.

    Executor-memory
    Executor-memory is derived as (Memory per executor - Executor memory overhead).

Reserved Memory — memory reserved for Spark engine related tasks, fixed 300 MB is reserved.
Spark Unified Memory = (Heap Memory — Reserved Memory) * 0.6. This memory is dedicated for storage and execution, default values are 50% for both.
User Memory = (Heap Memory — Reserved Memory) * 0.4 .


To estimate the amount of resources needed for a Spark job, you should consider the size and complexity of your data, the number of expected iterations, the number of partitions, and the memory requirements for each task. You can use the Spark Execution Engine to allocate resources dynamically, either by adjusting the number of executors, cores, or memory for each executor. Alternatively, you can pre-allocate resources by configuring the Spark executor to set the amount of memory, CPU core, network memory, and other parameters. Monitoring your job's performance and adjusting resources accordingly can help ensure optimal performance.

13. difference between narrow and wide transformation

Narrow transformations are operations that use each input partition to compute one output partition. Wide transformations are operations that use each input partition to compute multiple output partitions

Narrow transformations are preferred when the data can be processed within partitions without shuffling, while wide transformations are necessary for operations that involve aggregations, joins, or reshuffling of data across partitions.


narrow : map ,flatmap,filter,union,coalesce,repartition

wide :reducebykey,groupbykey,join ,

distinct,cogroup

in narrow :one to one mapping between rdd partition and file blocks

more wide transformation > more shuffling >more time and cost


Narrow Transformation: A narrow transformation is a type of transformation where each input partition contributes to only one output partition. It does not require data shuffling or movement across partitions. Narrow transformations are executed within a single stage without requiring data exchange between nodes.

Diagram:

sqlCopy codeInput RDD                    Narrow Transformation                   Output RDD
+-----------+         +------------------------>         +-----------+
| Partition |         |                           |         | Partition |
+-----------+         |                           |         +-----------+
| Partition |         |                           |         | Partition |
+-----------+         +------------------------>         +-----------+
| Partition |         |                           |         | Partition |
+-----------+         |                           |         +-----------+
Examples of Narrow Transformations:

map()
filter()
union()
coalesce()
repartition()


Wide Transformation: A wide transformation is a type of transformation where each input partition can contribute to multiple output partitions. It involves shuffling and data movement across partitions, often resulting in a stage boundary in Spark. Wide transformations require coordination and data exchange across nodes.
Diagram:

sqlCopy codeInput RDD                    Wide Transformation                   Output RDD
+-----------+         +------------------------>         +-----------+
| Partition |         |                           |         | Partition |
+-----------+         |                           |         +-----------+
| Partition |         |                           |         | Partition |
+-----------+         +------------------------>         +-----------+
| Partition |                                             | Partition |
+-----------+         +------------------------>         +-----------+
| Partition |         |                           |         | Partition |
+-----------+         |                           |         +-----------+
Examples of Wide Transformations:

groupByKey()
reduceByKey()
join()
cogroup()
distinct()
Wide transformations involve shuffling and data movement, which can impact performance. They typically introduce a stage boundary in the Spark execution plan and require network communication.

It’s important to note that transformations in Spark are lazily evaluated. They define a logical plan, and the execution happens when an action is called on the RDD. Spark optimizes the execution plan based on the transformations and the available resources.

The choice of narrow or wide transformations depends on the specific processing requirements and data characteristics. Narrow transformations are preferred when the data can be processed within partitions without shuffling, while wide transformations are necessary for operations that involve aggregations, joins, or reshuffling of data across partitions.

14. difference between dataframe and dataset

A dataset is a collection of related data items that can be stored in one or more dataframes. A dataframe is a specific type of data structure used in data analysis, which consists of rows and columns where each row represents a data point and each column represents a feature of that data point. The main difference between a dataset and a dataframe is that a dataset can include various types of data stored in different data structures, while a dataframe is more structured and specifically designed for data manipulation and analysis.


A DataFrame is a Dataset organized into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations under the hood.

Use Case: DataFrames are generally used for structured and semi-structured data, whereas Datasets are used for strongly-typed, object-oriented programming and can handle more complex data structures and operations


Dataset VS DataFrame
A Dataset and a DataFrame are both used for storing and manipulating large amounts of data in a structured way, but they have some key differences:

- Data Type: A DataFrame is a 2D size-mutable, tabular data structure with rows and columns. It can hold any data type, whereas a Dataset is a collection of strongly-typed JVM objects, and it is type-safe.
- Performance: A DataFrame is generally faster than a Dataset when it comes to performance because the latter uses the Java Virtual Machine (JVM) and the former uses code generation. DataFrames are implemented on top of RDDs (Resilient Distributed Datasets) and optimized for performance.
- API: DataFrames have a wider variety of APIs and are more flexible when it comes to data manipulation, whereas Datasets have a more limited set of APIs, but they are more concise and expressive.
- Type Safety: Datasets provide compile-time type safety, which means that if you try to store an incompatible type in a Dataset, the code will not compile. DataFrames, on the other hand, are not type-safe and may lead to runtime errors.
- Memory Management: DataFrames leverage lazy evaluation, which means that it will not perform any computation until an action is performed on the data. This allows for better memory management, whereas Datasets perform immediate evaluation and consume more memory.
- Use Case: DataFrames are generally used for structured and semi-structured data, whereas Datasets are used for strongly-typed, object-oriented programming and can handle more complex data structures and operations.

Datasets are preferred over Dataframes in Apache Spark when the data is strongly typed, i.e., when the schema is known ahead of time and the data is not necessarily homogeneous. This is because Datasets can enforce type safety, which means that type errors will be caught at compile time rather than at runtime.

15. If some job failed with out of memory error in production, what will be you approach to debug that

Here are some steps you can take to debug a job that fails with an out of memory error in production:
    1. Check the kernel message log.
    This will show you if the process was killed because it ran out of memory.
    2. Review the system performance metrics.
    This will help you determine if there were any unusual CPU, I/O, or memory utilizations in the minutes, hours, or days prior to the failure.
    3. Increase the maximum heap size.
    You can do this by adding the -Xmx flag to your JVM application startup settings and setting it to a larger value. For example, to increase the maximum heap size to 8GB, you would add the -Xmx8g parameter to your JVM application start parameters.
    4. Use a Java profiler.
    This will help you identify where memory is being allocated and how it is being used.
    5. Generate a memory dump.
    This will give you a snapshot of the heap memory at the time of the failure. You can use this to identify objects that are no longer being used but are still taking up memory.
    6. Analyze the memory dump.
    You can use a variety of tools to analyze the memory dump, such as Eclipse Memory Analyzer (MAT) or VisualVM.
    7. Fix the memory leak.
    Once you have identified the source of the memory leak, you can fix it by modifying your code.
    Here are some additional tips for debugging out of memory errors:
    Try to reproduce the error in a development environment.: This will make it easier to debug the problem.
    Use a debugger to step through your code.: This will help you identify the line of code that is causing the error.
    Use logging to track memory usage.: This will help you identify areas of your code that are using excessive amounts of memory.
    Monitor your application's memory usage in production.: This will help you identify memory leaks before they cause problems.

If a job fails with an out of memory error in production, the first step would be to identify the cause of the error by looking at the logs and error messages generated by the system. This can help to identify the resources or objects that are causing the error. The next step would be to investigate the code and configuration of the job itself, looking for potential sources of memory usage that can be optimized or modified to work more efficiently. It may also be necessary to adjust the amount of memory allocated to the job, or to consider scaling up the system resources to support the workload.

16. what is DAG & how that helps.

A DAG is a Directed Acyclic Graph, a type of graph whose nodes are directionally related to each other and don't form a directional closed loop. In the practice of analytics engineering, DAGs are often used to visually represent the relationships between your data models.

 DAGs help represent many different types of flows, including data processing flows. By thinking about large-scale processing flows in terms of DAGs, one can more clearly organize the various steps and the associated order for these jobs.

17. which version control do you use

There are many version control systems available, including Git, Team Foundation Version Control (TFVC), and Subversion (SVN). Git is a widely popular distributed version control system that enables collaboration and tracking changes across multiple branches and remote repositories. 

18. how do you test your spark code

To test your Spark code, you can use the local mode of Spark by running the code in a local Python or Scala shell. You can also use the Spark Shell in the Integrated Development Environment (IDE) or the command-line interface (CLI) to test and debug your code. Additionally, you can test your code on a small dataset or create a simulated dataset to work with for testing purposes.

Here are some ways to test Spark code:
    Unit testing
         Isolates code for testing. Unit tests are small and fast, and can cover a lot of code. However, they require a lot of assertion code.
    Integration testing
        Can cover a lot of code with a few tests. Integration tests can be split into two categories: one that involves infrastructure code, and one that doesn't.
    Using a testing framework
        Use the built-in Python unittest library or the popular Python testing frameworkpytest.
    Using FunSuite
        Write tests for your spark code using FunSuite.
    Using mockito-scala and scalatest libraries
        Write unit tests for Spark Scala code using the mockito-scala and scalatest libraries.
    Using a local SparkSession
         Cover your production Spark code with tests using a local SparkSession and creating Spark Datasets of the appropriate structure with test data.


19. what is shuffling, why we should think about minimizing it.

Shuffling is a fundamental concept in distributed data processing frameworks like Apache Spark. Shuffling is the process of redistributing or reorganizing data across the partitions of a distributed dataset.

Shuffling refers to the shuffle of data given. This operation is considered the costliest . The shuffle operation is implemented differently in Spark compared to Hadoop. On the map side, each map task in Spark writes out a shuffle file (OS disk buffer) for every reducer — which corresponds to a logical block in Spark.


Solutions to Mitigate Shuffle

Reduce Network I/O: By using fewer and larger worker nodes, you can reduce the amount of network I/O during shuffle. Larger nodes allow more data to be processed locally, minimizing the need for data transfer across the network.

20. if 199/200 partitions are getting executed but after 1 hour you are getting 
error.What things you will do?

One of the reasons for this can be skewness in data, where data is not distributed uniformly across the partitions. Task which is operating on the partition with huge amount of data will process slowly, generally such task is called as straggling task. Ultimately this may lead to the out of memmory error.

Data skewness can be taken care by generally below 3 approaches.

    1. Repartioning data by column which we know can provide the unform distribution across partitions.
    2. If we are not aware of the column which would provide uniform distribution of data across the partition then we can go ahead with salting technique but that is again pain.
    3. Starting from spark 3.0 we can enable AQE (Adaptive Query Execution) which itself sense the data skewness with the help of runtime statistics and handles the skewness by breaking the larger partitions into smaller ones and also by coalescing smaller partitions into bigger partition to ensure uniform distribution of data across the partitions.

Try answering in comments!

I am sure this will help all the Data Engineering enthusiasts.






Learn Apache Spark Step by Step (Follow the Sequence)

1. A quick introduction to the Spark API
https://lnkd.in/g8Y3tdhX

2. Overview of Spark - RDD, accumulators, broadcast variable
https://lnkd.in/g7fepuFF

3. Spark SQL, Datasets, and DataFrames:
https://lnkd.in/g3iZp7zk

4. PySpark - Processing data with Spark in Python
https://lnkd.in/gBnh6PAi

5. Processing data with SQL on the command line
https://lnkd.in/ggnxDaUu

6. Cluster Overview
https://lnkd.in/guCQnJnv

7. Packaging and deploying applications
https://lnkd.in/gUZpi2P9

8. Customize Spark via its configuration system
https://lnkd.in/gZh8Vkmv

9. Monitoring - Track the behavior of your applications
https://lnkd.in/grpGKFuP

10. Best practices to optimize performance and memory use
https://lnkd.in/gTRYBDQu

Credits - Spark Official Docs




#####################################################################################

Pyspark interview series

https://www.youtube.com/watch?v=XU0z0fFkQ7s&list=PLtgiThe4j67qEutypME2H3Ern8sjT1EA6&index=1&ab_channel=SumitMittal

number of initial partitions (128mb or lesser) - it is decided by max partition bytes and number of cpu cores based on this two number of partion decided

 if 12 cpu cores and 1.1GB Data then 12 partitions
                        if 4 cpu cores and 1.1GB Data then 9 partitions

                        spark.conf.get("spark.sql.files.maxPartitionBytes")
                        o/p - 134217728b

                        134217728 / (1024 * 1024)
                        o/p - 128.0

                        spark.sparkContext.defaultParallelism
                        o/p - 12 -  it is equal to number of cpu cores included that time - one big file split into small files

                        df.rdd.getNumPartitions()
                        o/p - 1 -  for non splitable file


                        spark.conf.get("spark.sql.files.openCostInBytes")
                        o/p- 4194304 -  let say 500 files of 2mb - 4+2 = 6x21 = 126MB Approx - 500/21 = 24 partition

                        4194304/(1024 * 1024)
                        o/p - 4.0