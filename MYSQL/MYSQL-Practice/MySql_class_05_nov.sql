create database class2_db;

use class2_db;

CREATE TABLE if NOT exists employee(  
    id int,
    name varchar(50),
    address VARCHAR(50),
    city VARCHAR(50)
);


INSERT into employee values(1,'Ajay','Indore','Lucknow');


SELECT * from employee;

--add new column named DOBs in the TABLE
alter Table employee add DOB date;

SELECT * from employee;


--modify existing column in a table or change datatype of name column or increase length of name COLUMN
alter table employee modify column name VARCHAR(100);

--delete existing column from given TABLE or remove city column from employee TABLE
alter table employee drop column city;

SELECT * from employee;


--rename the column name to full_name
alter table employee rename column name to full_name;

SELECT * from employee;


--add unique integirty constraints on id COLUMN
alter table employee add constraint id_unique UNIQUE(id);


insert into employee VALUES(1,'Ajay','ndore','2022-09-08');

--drop constraints from existing TABLE
alter table employee drop constraint id_unique;


insert into employee VALUES(1,'Ajay','Indore','2022-09-08');


SELECT * from employee;



--create table with Primary_Key
create Table persons
(
    id INT,
    name VARCHAR(50),
    age int,
   -- PRIMARY KEY (id)
   -- PRIMARY KEY (id,name)
   constraint pk PRIMARY KEY (id)
);


insert into persons VALUES(1,'ajay',27);

--try to insert duplicate value for primary key COLUMN
insert into persons VALUES(1,'Ravi',27);

--try to insert null value for PRIMARY key column
insert into persons values(null,'Rahul',25);

--for difference between primary key and Unique
alter table persons add constraint age_unq UNIQUE(age);


select * from persons;

insert into persons values(2,'Rahul',28);

insert into persons values(3,'Amit',26);

insert into persons values(4,'Amit',null);

insert into persons values(5,'deepak',null);

select * from persons;



--create table for foreign key demo
create table customer 
(
    cust_id int,
    name varchar(50),
    age int,
    constraint pk Primary Key (cust_id)
);


create table orders 
(
    order_id int,
    order_num varchar(50),
    customer_id int,
    constraint pk Primary Key (order_id),
    constraint fk FOREIGN Key (customer_id) REFERENCES customer(cust_id)

);


--Difference BETWEEN Drop & TRUNCATE Command

select * from persons;
TRUNCATE table persons;

select * from persons;

drop table persons;

select * from employee;

drop table employee;


--Operations with select Command
create table if not exists employee(
    id int,
    name varchar(50),
    age int,
    hiring_date date,
    salary int,
    city varchar(50)
);

insert into employee value(1,'Ajay',25,'2021-08-10',10000,'Lucknow');

insert into employee value(2,'Amit',25,'2021-08-10',20000,'Indore');

insert into employee value(3,'Sumit',22,'2021-08-10',11000,'Noida');

insert into employee value(4,'Raja',27,'2021-08-12',10000,'Gurgaon');

SELECT * from employee;

--how to count total records
select count(*) from employee;

--alias declaration
select count(*) as total_row_count from employee;

--display specific columns in the final result
select name,salary from employee;

--alias for multiple columns
select name as employee_name,salary as employee_salary from employee;

select * from employee;

--print unique hiring_dates from the employee table when employees joined it
select DISTINCT(hiring_date) as distinct_hiring_dates from employee;

SELECT * from employee;

--how many unique age values in the tables?
select count(distinct(age)) as total_unique_ages from employee;


--increment salary of each employee by 20% and display final result with new salary
select id,
       name,
       salary as old_salary,
       (salary+salary * 0.2) as new_salary 
from employee;

--syntax for update command 
SELECT * from employee;

--updates will be made for all rows
UPDATE employee SET age = 20;

SELECT * from employee;

--update the salary of employee after giving 20% increment
UPDATE employee SET salary = salary + salary * 0.2;

SELECT * from employee;

--how to filter data using WHERE Clauses
select * from employee where hiring_date = '2021-08-12';


--update the salary of employees who joined the company on 2021-08-10 to 80000

update employee set salary = 80000 where hiring_date = '2021-08-12';

SELECT * from employee;

--how to delete specific records from table using delete comand
--delete records of those employee who joined company on 2021-08-10

delete from employee where hiring_date = '2021-08-12';


SELECT * from employee;
