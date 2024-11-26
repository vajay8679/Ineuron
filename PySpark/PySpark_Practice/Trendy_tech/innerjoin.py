from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("inner_join_example").getOrCreate()

# Create DataFrames for Employees and Departments
data_employees = [(1, "John", 1), (2, "Emma", 2), (3, "Raj", None), (4, "Nina", 4)]
data_departments = [(1, "HR"), (2, "Tech"), (3, "Marketing"), (None, "Temp")]

columns_employees = ["emp_id", "emp_name", "dept_id"]
columns_departments = ["dept_id", "dept_name"]

df_employees = spark.createDataFrame(data_employees, columns_employees)
df_departments = spark.createDataFrame(data_departments, columns_departments)

# Perform INNER JOIN
# since `inner` is the default join type, we can omit it
df_joined = df_employees.join(df_departments, df_employees.dept_id == df_departments.dept_id)

# Show the result
df_joined.show()



# SELECT *
# FROM employees e
# INNER JOIN departments d
#     ON e.dept_id = d.dept_id;


emp_id	emp_name	dept_id
1	John	1
2	Emma	2
3	Raj	null
4	Nina	4
Table B (Departments):

dept_id	dept_name
1	HR
2	Tech
3	Marketing
null	Temp


o/p -

emp_id	emp_name	dept_id	dept_name
1	John	1	HR
2	Emma	2	Tech

+------+--------+-------+-------+---------+
|emp_id|emp_name|dept_id|dept_id|dept_name|
+------+--------+-------+-------+---------+
|     1|    John|      1|      1|       HR|
|     2|    Emma|      2|      2|     Tech|
+------+--------+-------+-------+---------+