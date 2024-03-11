from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("full_outer_join_example").getOrCreate()

# Create DataFrames for Employees and Departments
data_employees = [(1, "John", 1), (2, "Emma", 2), (3, "Raj", None), (4, "Nina", 4)]
data_departments = [(1, "HR"), (2, "Tech"), (3, "Marketing"), (None, "Temp")]

columns_employees = ["emp_id", "emp_name", "dept_id"]
columns_departments = ["dept_id", "dept_name"]

df_employees = spark.createDataFrame(data_employees, columns_employees)
df_departments = spark.createDataFrame(data_departments, columns_departments)

# Perform Full Outer Join
df_joined = df_employees.join(df_departments, df_employees.dept_id == df_departments.dept_id, "outer")

# Show the result
df_joined.show()



# SELECT
#     *
# FROM
#     employees e
# FULL OUTER JOIN
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
3	Raj	null	null	null
4	Nina	4	null	null
null	null	null	null	Temp
null	null	null	3	Marketing


+------+--------+-------+-------+---------+
|emp_id|emp_name|dept_id|dept_id|dept_name|
+------+--------+-------+-------+---------+
|     1|    John|      1|      1|       HR|   -> matched row
|     2|    Emma|      2|      2|     Tech|   -> matched row
|     3|     Raj|   null|   null|     null|   -> employees included in the result, but no matching department (null `dept_id` on employees table)
|     4|    Nina|      4|   null|     null|   -> employees included in the result, but no matching department
|  null|    null|   null|   null|     Temp|   -> departments included in the result, but no matching employee (null `dept_id` on departments table)
|  null|    null|   null|      3|Marketing|   -> departments included in the result, but no matching employee
+------+--------+-------+-------+---------+


Handling Null Values In Full Outer Join
As you see in the example above, null values do not match with other null values. Therefore, rows with null values as the join key are not matched.