create DATABASE Relations;

use Relations;
drop table city;


create table country(
    country_id int PRIMARY KEY,
    country_name varchar(255)
);

create table city(
    city_id int,
    city_name varchar(255),
    country_id int,
    constraint fk_foreign_key FOREIGN KEY (country_id) REFERENCES country(country_id)
);


insert into country values (1,"India"),(2,"Pakistan"),(3,"Shrilanka"),(4,"Bangladesh");

insert into city values (1,"Delhi",1),(2,"Kolkata",1),(3,"Indore",1),(4,"Islamabad",2),(5,"Karachi",2),(6,"Columbo",3),(7,"Galle",3),(8,"Dhaka",4);


select * from country;
select * from city;


#One-to-many relationship
-- A one-to-many relationship occurs when one record in table 1 is related to one or more records in table 2. However, one record in 
--table 2 cannot be related to more than one record in table 1

select * from country inner join city on city.country_id = country.country_id;


#One-to-one relationship
--A one-to-one relationship in a database occurs when each row in table 1 has only one related row in table 2. 
--For example, a department may have only one head manager, a husband — only one wife, an employee — one company car, etc.

CREATE TABLE Employee (
  ID int PRIMARY KEY,
  Name VARCHAR(50)
);

CREATE TABLE Salary (
  EmployeeID int UNIQUE NOT NULL,
  SalaryAmount int,
  CONSTRAINT FK_Salary_Employee FOREIGN KEY (EmployeeID) REFERENCES Employee (ID)
);

insert into Employee values (1,"Ajay"),(2,"Amit"),(3,"Sumit"),(4,"Raja");
insert into Salary values (1,1000),(2,2000),(3,3000),(4,5000);

select * from Employee;
select * from Salary;

select * from Employee inner join Salary on Salary.EmployeeID = Employee.ID;


#Many-to-many relationship
--A many-to-many relationship occurs when multiple records in one table are related to multiple records in another table.
--For example, products and suppliers: one supplier may deliver one or many products and at the same time, the company
-- may order one product from one or many suppliers.
--The relationship between the Product entity and Order entity is many-to-many, as one product may be in many orders 
--and many orders may contain the same product.


--Example of creating many-to-many relation in SQL
--Relational databases don’t support direct many-to-many relationships between two tables. Then, how to implement
-- many-to-many relationships in SQL? To create a many-to-many relationship in a database, you’ll need to create a
-- third table to connect the other two. This new table (also known as a linking, joining, bridging, or junction 
--table) will contain the primary key columns of the two tables you want to relate and will serve as an intermediate 
--table between them.

--Let’s consider the following example of how to create many-to-many relationship in SQL. Suppose, we want to 
--establish a many-to-many relationship between two tables: films and category. First, we create the two tables.

CREATE TABLE films (
  film_id INT PRIMARY KEY,
  title VARCHAR(50),
  director VARCHAR(50),
  year_released DATETIME
);


CREATE TABLE category (
  category_id INT PRIMARY KEY,
  name VARCHAR(50)
);

--Next, we create a junction table film_category that will map these two tables together by referencing the
-- primary keys of both tables.

CREATE TABLE film_category (
  film_id INT
 ,category_id INT
 ,CONSTRAINT film_cat_pk PRIMARY KEY (film_id, category_id)
 ,CONSTRAINT FK_film
  FOREIGN KEY (film_id) REFERENCES films (film_id)
 ,CONSTRAINT FK_category
  FOREIGN KEY (category_id) REFERENCES category (category_id)
);


#Many-to-one relationship
--Many experts don’t separate a many-to-one relationship as a class of its own as there is not much difference 
--between one-to-many and many-to-one relationships. It’s just a matter of focus. For example, if one school class
-- can consist of several pupils then, class to pupil is a one-to-many relationship (one class consists of many pupils),
-- while pupil to class relationship is many-to-one (many pupils study in one class).
--Example of many-to-one relationship in SQL:

--table -order -> table-customer
--many order done by one customer


#Self-referencing relationships
--A self-referencing relationship (also known as a recursive relationship) in a database occurs when a column in 
--a table relates to another column in the same table. In such a relationship, only one table is involved. 
--For example, the Staff table contains information about company employees and their managers, however,
-- managers themselves belong to staff too.

--A self-referencing relationship example in SQL:

--employee table contains employee_id column and oner column is manager_id column


--Relationship	Example
--one-to-one	A User has ONE address
--one-to-many	A Book has MANY reviews
--many-to-many	A user has MANY books and a book has MANY users
