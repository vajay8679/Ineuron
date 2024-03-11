from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("cross_join_example").getOrCreate()

# Create DataFrames for Employees and Departments
data_employees = [(1, "John"), (2, "Emma"), (3, "Raj")]
data_departments = [("A", "HR"), ("B", "Tech")]

columns_employees = ["emp_id", "emp_name"]
columns_departments = ["dept_id", "dept_name"]

df_employees = spark.createDataFrame(data_employees, columns_employees)
df_departments = spark.createDataFrame(data_departments, columns_departments)

# Perform Cross Join
df_cross_joined = df_employees.crossJoin(df_departments)

# Show the result
df_cross_joined.show()




# SELECT
#     *
# FROM
#     employees e
# CROSS JOIN
#     departments d;


Table A (Employees):

emp_id	emp_name
1	John
2	Emma
3	Raj
Table B (Departments):

dept_id	dept_name
A	HR
B	Tech


+------+--------+-------+---------+
|emp_id|emp_name|dept_id|dept_name|
+------+--------+-------+---------+
|     1|    John|      A|       HR|
|     1|    John|      B|     Tech|
|     2|    Emma|      A|       HR|
|     2|    Emma|      B|     Tech|
|     3|     Raj|      A|       HR|
|     3|     Raj|      B|     Tech|
+------+--------+-------+---------+