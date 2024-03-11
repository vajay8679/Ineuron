1. SQL Fundamentals, CRUD Operations
Create
Adds new data entries or objects to a data storage system, such as a database or API.
Read
Retrieves data from a database. This can involve querying the database to fetch existing records or documents that match certain criteria.
Update
Allows a user to update existing data in a database. This is typically performed through a form, where the user enters the new values for the existing data and then clicks the submit button.
Delete
Used to delete or remove existing data from a database or other data storage system. 


2. Primary Key vs Unique Key, Auto Increment Values -

a primary key is a key that uniquely identifies each record in a table but cannot store NULL values. In contrast, a unique key prevents duplicate values in a column and can store NULL values

A primary key and unique key are both important database constraints, but serve different purposes. A primary key is a column or group of columns that uniquely identifies each row in a table. It must be unique and cannot be null. A unique key, on the other hand, is a column or group of columns that must be unique, but can have null values.

In terms of auto-increment values, this is a feature that automatically increases a value in a column each time a new row is inserted into the table. This is commonly used for columns that represent an auto-incrementing ID or timestamp, such as an order number or a timestamp for when a record was created.


3. DDL vs DML, Truncate vs Delete

DDL (Data Definition Language) and DML (Data Manipulation Language) are categories of SQL statements used to define data in a database and manipulate it, respectively. Truncate and Delete are two types of DML statements used to remove data from a table. The main difference between the two statements is the way they handle data. Truncate removes all the data in a table, including primary key and foreign key constraints, while Delete removes data from a table but preserves the data integrity.

Truncate is useful when you want to remove all the data in a table to start fresh and reload it from a source. While Delete is useful when you want to remove specific rows from a table based

DROP and TRUNCATE are DDL command while DELETE is a DML command. DELETE remove the specific row based on the given condition, TRUNCATE removes all the record from the table at once, whereas the DROP command removes the table or databases and as well as the structure.



4. Foreign Key Constraint

The FOREIGN KEY constraint is used to prevent actions that would destroy links between tables. A FOREIGN KEY is a field (or collection of fields) in one table,


A foreign key is a column (or combination of columns) in a table whose values must match values of a column in some other table. FOREIGN KEY constraints enforce referential integrity, which essentially says that if column value A refers to column value B, then column value B must exist.

5. Distinct, Order By, Limit, Like Keyword

In the context of SQL databases, 'Distinct' is a keyword used to return unique values for a specific column. 'Order By' is used to organize the result set based on the value or expression specified. 'Limit' is used to restrict the number of rows returned in the result set. 'Like' keyword is used to perform pattern matching with a percentage sign (%) wildcard, allowing for partial matches. These keywords are often used together in SQL statements to retrieve specific and organized data from a database.


6. Order of execution in SQL

The correct order of execution in SQL is FROM, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY and LIMIT. 

7. Aggregate Functions

SQL Aggregate Functions: Explore 5 Types of Functions
An aggregate function in SQL performs a calculation on multiple values and returns a single value. SQL provides many aggregate functions that include avg, count, sum, min, max, etc

Aggregate functions are mathematical operations used in database management to summarize and simplify the data within a set of rows, based on specific combinations of values within the rows. Some of the common aggregate functions include SUM, COUNT, AVG, MAX, and MIN. These functions can be used in SELECT statements to return a single value representing a summary or summary of several values from one or more tables. They are extremely useful for analyzing and reporting data effectively.


8. Datatypes in SQL

data types are primarily classified into three categories.

Numeric Datatypes - BigInt , Int, smallint, tinyint , numeric , Float
Date and Time Database - DATE, DATETIME, TIMESTAMP, YEAR
String Database - char, varchar, text


9. Logical Operators in SQL

Types of Logical Operators in SQL
Given below is the list of logical operators available in SQL.

Operator 	        Meaning
AND	       TRUE if both Boolean expressions are TRUE. - SELECT * FROM employee WHERE emp_city = 'Allahabad' AND emp_country = 'India';

IN	       TRUE if the operand is equal to one of a list of expressions. - SELECT * FROM employee WHERE emp_city IN ('Allahabad', 'Patna');

NOT	       Reverses the value of any other Boolean operator. - SELECT * FROM employee WHERE emp_city NOT LIKE 'A%';

OR	       TRUE if either Boolean expression is TRUE. - SELECT * FROM employee WHERE emp_city = 'Varanasi' OR emp_country = 'India';

LIKE	   TRUE if the operand matches a pattern. - SELECT * FROM employee WHERE emp_city LIKE 'P%';

BETWEEN	   TRUE if the operand is within a range. - SELECT * FROM employee WHERE emp_id BETWEEN 101 AND 104;

ALL	       TRUE if all of a set of comparisons are TRUE. - SELECT * FROM employee WHERE emp_id = ALL 
                (SELECT emp_id FROM employee WHERE emp_city = 'Varanasi');

ANY	       TRUE if any one of a set of comparisons is TRUE. - SELECT * FROM employee WHERE emp_id = ANY
                (SELECT emp_id FROM employee WHERE emp_city = 'Varanasi');

EXISTS     TRUE if a subquery contains any rows. - SELECT emp_name FROM employee WHERE EXISTS
                (SELECT emp_id FROM employee WHERE emp_city = 'Patna');

SOME	   TRUE if some of a set of comparisons are TRUE. - SELECT * FROM employee WHERE emp_id < SOME 
                (SELECT emp_id FROM employee WHERE emp_city = 'Patna');
                
https://www.geeksforgeeks.org/sql-logical-operators/


10. Joins in SQL

CROSS JOINS in SQL
    SELECT column-name(s)
    FROM table1 CROSS JOIN table2;

SELECT is used to specify all columns we need to display in the resulting table. FROM specifies the tables where we need to look for these columns. The type of join, i.e., CROSS JOIN, in this case, is placed between the two tables we wish to join.

SELF JOIN in SQL
    SELECT a.column1 , b.column2
    FROM table_name a, table_name b
    WHERE some_condition;

In SQL Self Join, a table is joined to itself. This means each row of the table is joined with itself and all other rows concerning stated conditions if any. In other words, we can say that it is a merge between two copies of the same table. This is extremely helpful when the foreign key references the primary key of the same table.

INNER JOIN in SQL
    SELECT column-name 
    FROM table-1 INNER JOIN table-2 
    WHERE table-1.column-name = table-2.column-name;

(INNER) JOIN: Returns records that have matching values in both tables

SELECT *
FROM Customers NATURAL JOIN Shopping_Details;

SQL Natural Join is a type of Inner join based on the condition that columns having the same name and datatype are present in both the tables to be joined.

LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
    SELECT column-name(s)
    FROM table1 LEFT OUTER JOIN table2
    ON table1.column-name = table2.column-name;

RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
    SELECT column-name(s)
    FROM table1 RIGHT OUTER JOIN table2
    ON table1.column-name = table2.column-name;

FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
    SELECT column-name(s)
    FROM table1 FULL OUTER JOIN table2
    ON table1.column-name = table2.column-name;


11. Difference between where and having

If “Where” clause is used to filter the records from a table that is based on a specified condition, then the “Having” clause is used to filter the record from the groups based on the specified condition.

In SQL, the WHERE and HAVING clauses are both used to filter data. The main difference between the two is that the WHERE clause applies to individual rows, while the HAVING clause applies to groups as a whole.


Difference Between WHERE and HAVING Clause - Shiksha ...
The main difference between WHERE and HAVING clause is that the WHERE clause allows you to filter data from specific rows (individual rows) from a table based on certain conditions. In contrast, the HAVING clause allows you to filter data from a group of rows in a query based on conditions involving aggregate values.

12. Over Clause & Partition By Clause

In SQL, the PARTITION BY clause is a subclause of the OVER clause. The OVER clause defines how windows of records are built, while the PARTITION BY clause defines which records to include in each window. 

The 'PARTITION BY' clause in SQL is a subclause of the 'OVER' clause. It's used to split a large table into smaller, more manageable partitions. Each partition is then processed for the function present in the 'OVER()' clause

An Over Clause - in SQL, refers to the part of a query where you bring back additional rows of data on top of the rows that were matched for the main query. On the other hand, Partition By Clause is used to specify how the dataset should be partitioned, by which column or columns. In combination with the Over Clause, it allows you to perform aggregation across the different partitions of your data. This can be useful for tasks such as performing calculations across different groups or time periods. However, it is important to note that the use of Over Clause and Partition By Clause together can impact performance, so it should be used judiciously.


PARTITION BY does not affect the number of rows returned, but it changes how a window function's result is calculated. The OVER clause defines a window or user-specified set of rows within a query result set. A window function then computes a value for each row in the window.

13. Row Number Function in MySQL

The ROW_NUMBER() function in MySQL is used to returns the sequential number for each row within its partition. It is a kind of window function. The row number starts from 1 to the number of rows present in the partition.

    ROW_NUMBER() OVER (<partition_definition> <order_definition>)  

The ROW_NUMBER() function in MySQL is used to returns the sequential number for each row within its partition. It is a kind of window function.

The row number function in MySQL is used to assign a unique row number to each record within a result set, based on a specified order. It can be used in SELECT, INSERT, UPDATE, and DELETE statements. The function syntax is
text

ROW_NUMBER() OVER (ORDER BY column1 ASC [, column2 ASC ...])
, where column1, column2, etc. are the columns to be used for ordering, and ASC indicates ascending order. The ROW_NUMBER() function assigns a value of 1 to the first record in the result set, and incremental values to subsequent records, based on the specified order.

14. Rank & Dense Rank

RANK() assigns the same rank to rows with equal values, leaving gaps. DENSE_RANK() assigns the same rank to equal values without gaps, resulting in consecutive ranks

he RANK function does not return consecutive values in the case of having multiple occurrences of the same value. The DENSE_RANK function always returns consecutive values.

15. CTE in SQL

A Common Table Expression (CTE) is a named result set in a SQL query. CTEs help keep your code organized, and allow you to perform multi-level aggregations on your data, like finding the average of a set of counts.

A Common Table Expression (CTE) is a temporary result set in a SQL query. CTEs are temporary because they are not stored in the database and are lost once a query is executed. CTEs can be used in a variety of statements, including SELECT, INSERT, UPDATE, DELETE, and MERGE

CTE, or Common Table Expression, is a temporary result set that is defined within a single statement or a set of statements in SQL. It allows you to refer to the result set by a name, making your code easier to read and maintain. CTEs can be used with SELECT, INSERT, UPDATE, and DELETE statements, and they are created at the time the statement is executed. Once the statement is complete, the CTE is no longer available.

WITH cte_name(column1, column2, etc.) AS (SELECT ...)


https://www.metabase.com/learn/sql-questions/sql-cte#:~:text=A%20Common%20Table%20Expression%20(CTE,of%20a%20set%20of%20counts.

-- define CTE:
WITH Cost_by_Month AS
(SELECT campaign_id AS campaign,
       TO_CHAR(created_date, 'YYYY-MM') AS month,
       SUM(cost) AS monthly_cost
FROM marketing
WHERE created_date BETWEEN NOW() - INTERVAL '3 MONTH' AND NOW()
GROUP BY 1, 2
ORDER BY 1, 2)

-- use CTE in subsequent query:
SELECT campaign, avg(monthly_cost) as "Avg Monthly Cost"
FROM Cost_by_Month
GROUP BY campaign
ORDER BY campaign



-- CTE to calculate average order total
-- with the name for the CTE (avg_order) and column (total)
WITH avg_order(total) AS (

-- CTE query
  SELECT
    AVG(total)
  FROM
    orders
  WHERE
    -- exclude test orders
    product_id > 10
    AND -- exclude orders before launch
    created_at > '2016-04-21'
    AND -- exclude test accounts
    user_id > 10
)

-- our main query:
-- orders with above-average totals
SELECT
  o.id,
  o.total
FROM
  orders AS o
  -- join the CTE: avg_order
  LEFT JOIN avg_order AS a
WHERE
  -- total is above average
  o.total > a.total
ORDER BY
  o.total DESC



16. SQL internals

In SQL, internal is a term used to provide details about the sql server instance or database engine. It is related to server settings, parameters, and functionality that are not typically relevant to end users of the database. These settings include things like memory allocation, query optimizer settings, and various performance-tuning parameters. Understanding these internal details can be helpful for system administrators and database managers to optimize performance and ensure that the database is configured correctly.

--one of the query format
--select top 3 city from students order by salary desc;
select top 2 oorder_emp_id,count(*) as total_customer from orders group by oorder_emp_id order by total_customer desc;

https://www.youtube.com/watch?v=gZu2ZldwrK4&list=PLtgiThe4j67osrX6iUEpo7J4Gkh_G25Y_&index=2&t=34s&ab_channel=SumitMittal


I have created a SQL video where all of these topics are covered.
here is the link - https://lnkd.in/gXTvqk3i

Also the complete notes for this are present over the github -
https://lnkd.in/gzbziNWj