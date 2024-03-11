from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("right_outer_join_example").getOrCreate()

# Create DataFrames for Employees and Departments
data_employees = [(1, "John", 1), (2, "Emma", 2), (3, "Raj", None), (4, "Nina", 4)]
data_departments = [(1, "HR"), (2, "Tech"), (3, "Marketing"), (None, "Temp")]

columns_employees = ["emp_id", "emp_name", "dept_id"]
columns_departments = ["dept_id", "dept_name"]

df_employees = spark.createDataFrame(data_employees, columns_employees)
df_departments = spark.createDataFrame(data_departments, columns_departments)

# Perform Right Outer Join
df_joined = df_employees.join(df_departments, df_employees.dept_id == df_departments.dept_id, "right")

# Show the result
df_joined.show()




# SELECT
#     *
# FROM
#     employees e
# RIGHT JOIN
#     departments d ON e.dept_id = d.dept_id;


Table A (Employees):

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


Expected output:

emp_id	emp_name	dept_id	dept_id	dept_name
1	John	1	1	HR
2	Emma	2	2	Tech
null	null	null	3	Marketing
null	null	null	null	Temp


+------+--------+-------+-------+---------+
|emp_id|emp_name|dept_id|dept_id|dept_name|
+------+--------+-------+-------+---------+
|     1|    John|      1|      1|       HR|
|     2|    Emma|      2|      2|     Tech|
|  null|    null|   null|      3|Marketing|  -> no employees in Marketing department
|  null|    null|   null|   null|     Temp|  -> null values do not match with other null values, therefore no matching rows
+------+--------+-------+-------+---------+

Handling Null Values In Right Outer Join
As you've seen in the example, null dept_id doesn't match null in the left DataFrame (df_employees). Therefore, those rows are not matched and null values are used to fill in the columns from the left DataFrame.