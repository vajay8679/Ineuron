--create database command

create DATABASE BigDataBootCamp;

create DATABASE test;

--get list of existing DATABASE
show DATABASES;

--dropping DATABASE
drop DATABASE test;

--go inside DATABASE
use BigDataBootCamp;

--command to create TABLE
create table if not exists employee
(
    id int,
    name VARCHAR(50)
);


--Command to list down all the TABLES
show tables;

--Command to list down all the TABLES
show create table employee;

--command to DELETE TABLE
drop table employee;

--commoand to create table
create table if not exists employee
(
    id int,
    name VARCHAR(50),
    salary DOUBLE, 
    hiring_data DATE
);

--insert data into table
insert into employee values(1,'AJAY',10000,'2021-09-15');

--This statement will fail
insert into employee values(1,'AJAY','2021-09-15');

--syntax 2 to insert data into a table
insert into employee(salary,name,id) values(10000,'Rahul',2);

--insert multiple rows using single insert statement
insert into employee values(3,'Amit',25000,'2021-09-15'),(4,'Sumit',45600,'2023-09-25'),(5,'Ravi',4000,'2021-09-10');


--use select command to query the data
SELECT * from employee;

--Example for integrity constraints
create table if not exists employee_with_constraints
(
    id int NOT NULL,
    name VARCHAR(50) NOT NULL,
    salary DOUBLE, 
    hiring_data DATE DEFAULT '2021-01-01',
    UNIQUE (id),
    CHECK (salary > 1000)
);

--Example 1 for Integrity Constraints failure
-- exception will be thrown -> Column 'id' cannot be null
insert into employee_with_constraints values(null,'Amit',3000,'2021-02-03');

--Example 2 for Integrity Constraints failure
-- exception will be thrown -> Column 'name' cannot be null
insert into employee_with_constraints values(3,null,3000,'2021-02-03');

--Example 3 for Integrity Constraints failure
-- exception will be thrown -> Check constraint 'employee_with_constraints_chk_1' is violated.
insert into employee_with_constraints values(1,'Amit',500,'2021-02-03');

--insert correct data
insert into employee_with_constraints values(1,'Amit',5000,'2021-02-03');


--Example 4 for Integrity Constraints failure
-- exception will be thrown -> Duplicate entry '1' for key 'employee_with_constraints.id'
insert into employee_with_constraints values(1,'Amit',1300,'2022-02-03');


--Example 5 for Integrity Constraints failure
insert into employee_with_constraints values(2,'Amit',1300,null);


insert into employee_with_constraints(id,name,salary) values(3,'Sumit',1300);

select * FROM employee_with_constraints;


--Add alias name for constraints
create table if not exists employee_with_constraints_tmp
(
    id int NOT NULL,
    name VARCHAR(50) NOT NULL,
    salary DOUBLE, 
    hiring_data DATE DEFAULT '2021-01-01',
   CONSTRAINT  unique_id UNIQUE (id),
   CONSTRAINT salary_check CHECK (salary > 1000)
);



--Example 3 for Integrity Constraints failure
-- exception will be thrown -> Check constraint 'salary_check' is violated.
insert into employee_with_constraints_tmp values(1,'Amit',500,'2021-02-03');