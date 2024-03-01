--1st CLASS_ORIGIN
-- two types of DATABASE- relational(row & column) dtaabase and nosql(key-value,document,graph) DATABASE

--https://ide.goorm.io/my/dashboard


--mysql-ctl cli;

CREATE DATABASE trendytech;

show DATABASES;

--drop DATABASE trendytech;

use trendytech;

--to know in which database you are
select database();


CREATE Table employee(
    name VARCHAR(50),
    age INT,
    salary int
);


DESCRIBE employee;


--drop table employee;


--if wee didnt select database and we want to create table use below command - here we use trendytech db

-- CREATE Table trendytech.employee(
--     name VARCHAR(50),
--     age INT,
--     salary int
-- );



--session2

CREATE Table employee(
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    salary int,
    location VARCHAR(50)
);


desc employee;


select * from employee;


insert into employee(first_name,middle_name,last_name,age,salary,location) values("Ajay","Kumar","Verma",28,20000,"Indore"); 
insert into employee values("Sumit","Kumar","Verma",26,25000,"Bhopal"); 
insert into employee(first_name,last_name,age,location) values("Sumit","Verma",24,"Indore"); 
insert into employee(first_name,last_name,age,location) values("Sumit'h","Verma",24,"Indore"); 

insert into employee(first_name,last_name,age,location) values('Sumit\'h',"Verma",24,"Indore"); 
insert into employee(first_name,middle_name,last_name,age,salary,location) values("Ajay1","Kumar","Verma",28,20000,"Indore"),("Ajay2","Kumar","Verma",28,20000,"Indore"),("Ajay3","Kumar","Verma",28,20000,"Indore"); 

insert into employee values("SumitSumitSumitSumitSumitSumitSumitSumitSSumitSumitSumitSumitSumitSumitSumitSumitSuSumitSumitSumitSumitSumitSumitSumitSumitSuSumitSumitSumitSumitSumitSumitSumitSumitSuSumitSumitSumitSumitSumitSumitSumitSumitSuitSumitSumitSumit","Kumar","Verma",26,25000,"Bhopal"); 

select * from employee;


# constraints (NOT NULL, DEFAULT)

drop TABLE employee;
CREATE Table employee(
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50)  NOT NULL,
    age INT  NOT NULL,
    salary int,
    location VARCHAR(50)  NOT NULL DEFAULT 'Bangalore'  #combination of DEFAULT and Not NUll it means we can not use null vaue here because of not null
);

desc employee;

insert into employee(first_name,last_name,age,salary) values("Ajay","Verma",28,20000); 

SELECT * from employee;


--session3

CREATE Table employee(
    id int PRIMARY KEY,
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    salary int,
    location VARCHAR(50)
);

desc employee;

insert into employee(id,first_name,middle_name,last_name,age,salary,location) values(1,"Ajay","Kumar","Verma",28,20000,"Indore"); 

--not UNIQUE vaue
insert into employee(id,first_name,middle_name,last_name,age,salary,location) values(1,"Ajay","Kumar","Verma",28,20000,"Indore"); 

--not null vaue
insert into employee(id,first_name,middle_name,last_name,age,salary,location) values(NULL,"Ajay","Kumar","Verma",28,20000,"Indore"); 


CREATE Table employee(
    id int AUTO_INCREMENT,
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    salary int,
    location VARCHAR(50),
    PRIMARY KEY(ID)
);


insert into employee(first_name,middle_name,last_name,age,salary,location) values("Ajay","Kumar","Verma",28,20000,"Indore"); 

insert into employee(first_name,middle_name,last_name,age,salary,location) values("sumit","Kumar","Verma",28,20000,"Indore"); 

SELECT * FROM employee;


CREATE Table employee(
    id int UNIQUE KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);

insert into employee(id,first_name,last_name,age) values(1,"Ajay","Kumar",28); 
insert into employee(id,first_name,last_name,age) values(NULL,"Ajay","Kumar",28); 
insert into employee(id,first_name,last_name,age) values(NULL,"Ajay","Kumar",28); 



--session4


CREATE Table employee(
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50)  NOT NULL,
    age INT  NOT NULL,
    salary int,
    location VARCHAR(50)  NOT NULL DEFAULT 'Bangalore'  #combination of DEFAULT and Not NUll it means we can not use null vaue here because of not null
);


insert into employee(first_name,last_name,age,salary) values("sumit","Verma",28,20000); 
insert into employee(first_name,last_name,age,salary) values("Ajay","Verma1",28,20000); 
insert into employee(first_name,last_name,age,salary) values("ravi","Verma2",28,20000); 

desc employee;

select * from employee;

select * from employee where first_name = "Sumit";  #case INSENSITIVE

select * from employee binary where first_name = "Sumit";#error now it will match exact case - case SENSITIVE


select first_name as name, last_name as lname from employee;


update employee set first_name = "Rohit" where last_name ="Verma";

update employee set salary = salary+5000;


delete from employee where first_name="Sumit";


--alter is used to alter schema of the TABLE
alter table employee add column jobtitle varchar(20);
alter table employee modify jobtitle varchar(40)

alter table employee drop column jobtitle;

alter table employee add  PRIMARY key(first_name);

alter table employee drop  PRIMARY key;


desc employee;

--DDL - it change table structure or schema (Create, Alter, Drop, TRUNCATE)
--DML - deals with data directly (Insert, Update, Delete)


TRUNCATE table employee; #internally drops the table and recreate it again thats why it is DDl - remove all records from the table

delete from employee; # both turncate and delete will work but trucate is faster and efficient then delete(it takes more time).


--session5

create table students (
    student_id int AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(30),
    student_email VARCHAR(30),
    student_phone VARCHAR(15),
    student_altername_phone VARCHAR(15),
    enrollment_date TIMESTAMP NOT NULL,
    year_of_experience int NOT NULL,
    student_company VARCHAR(50),
    student_course int NOT NULL DEFAULT 1,
    batch_date VARCHAR(30) Not NULL,
    source_of_joining VARCHAR(30) Not NULL,
    location VARCHAR(30) NOT NULL,
    PRIMARY KEY (student_id),
    UNIQUE KEY(student_email),
    Foreign Key (student_course) REFERENCES course(course_id)
);

desc students;
drop table students;
insert into students(first_name,last_name,student_email,student_phone,enrollment_date,year_of_experience,student_company,student_course,batch_date,source_of_joining,location) values("Ajay","Kumar","ajay@gmail.com","7247593467","2021-11-02",12,"Walmart",2,"2021-10-03","google","Indore"),("amit","Kumar","amit@gmail.com","7247593467","2021-12-02",12,"Walmart",1,"2021-10-03","linkedin","Indore"),("ravi","verma","ravi@gmail.com","7247593467","2021-10-02",10,"Walmart",3,"2021-10-03","indeed","Indore"),("sumit","Verma","sumit@gmail.com","7247593467","2021-10-02",15,"Walmart",1,"2021-10-03","naukri","Indore"),("Niraj","Verma","niraj@gmail.com","7247593467","2021-12-02",20,"Google",2,"2021-10-03","shine","Bhopal");


--constraints error
insert into students(first_name,last_name,student_email,student_phone,enrollment_date,year_of_experience,student_company,student_course,batch_date,source_of_joining,location) VALUES ("Bumrah","Verma","bumrah@gmail.com","7247593467","2021-12-02",20,"Google",7,"2021-10-03","shine","Bhopal");
select * from students;

select student_id,first_name, student_email,enrollment_date,year_of_experience,batch_date from students;


create table course (
    course_id int NOT NULL,
    course_name VARCHAR(50) not NULL,
    course_duration int,
    course_fee VARCHAR(30) NOT NULL,
    PRIMARY KEY(course_id)
);

insert into course (course_id,course_name,course_duration,course_fee) values(1,"Big Data",6,5000),(2,"Data Science",3,2000),(3,"Data Analyst",2,7000);

select * from course;


select * from students;

--foreign key constraint fails error because we have key in studets table
delete from course where course_id = 3;



--session6

select DISTINCT location from students;

select DISTINCT student_company from students;

select student_id,first_name, student_email,enrollment_date,year_of_experience,batch_date from students order by year_of_experience;


select first_name, year_of_experience from students order by 2 desc;
select first_name, year_of_experience from students order by 1 desc;


select student_id,first_name, student_email,enrollment_date,year_of_experience,batch_date from students order by year_of_experience desc limit 3;


--this query wont work
select DISTINCT source_of_joining  from students order by enrollment_date desc limit 3;

--this will work because distinct combine both column source_of_joining,enrollment_date
select DISTINCT source_of_joining,enrollment_date  from students order by enrollment_date desc limit 3;

select student_id,first_name, student_email,enrollment_date,year_of_experience,batch_date from students order by enrollment_date desc limit 1;


select * from students order by enrollment_date desc limit 0,3;  #start from 0th and total 3 records


select student_id,first_name, student_email,enrollment_date,year_of_experience,batch_date from students where first_name like "%am%";



select student_id,first_name, student_email,enrollment_date,year_of_experience,batch_date from students where first_name like "____";


--session7

select source_of_joining  from students order by enrollment_date ;



--this query wont work
select DISTINCT source_of_joining  from students order by enrollment_date desc limit 3;

--this will work because distinct combine both column source_of_joining,enrollment_date
select DISTINCT source_of_joining,enrollment_date  from students order by enrollment_date desc limit 3;



--session8 (Aggregate Functions)


--count
SELECT count(*) from students;

SELECT count(DISTINCT location) from students;

SELECT count(DISTINCT student_company) from students;


SELECT count(*) from students where batch_date LIKE '%-10-%';

select * from students;

SELECT count(*) from students where enrollment_date LIKE '2021-10-%';


--group BY
select source_of_joining,count(*) from students group By source_of_joining;

select source_of_joining,count(*) from students group By batch_data; #this will not work batch_data shoupd be part of select statement as well


select source_of_joining,location,count(*) from students group By source_of_joining,location;

select student_course,count(*) from students group By student_course;
select batch_date,student_course,count(*) from students group By batch_date,student_course;


select MIN(year_of_experience) from students;

select max(year_of_experience) from students;

--this wont work
select MIN(year_of_experience),first_name from students;


select first_name from students order by year_of_experience limit 1;

--each source of joining with max year of experience
select source_of_joining, MAX(year_of_experience) from students GROUP BY source_of_joining;

select source_of_joining, SUM(year_of_experience) from students GROUP BY source_of_joining;

select source_of_joining, AVG(year_of_experience) from students GROUP BY source_of_joining;

select student_company, AVG(year_of_experience) from students GROUP BY student_company;


--session9 (A few more Datatypes)
select * from course;
insert into course values (4,"Web Development",3.5,7500); -- it will roundoff decimal number while select


--decimal datatype
create table course_new (
    course_id int NOT NULL,
    course_name VARCHAR(50) not NULL,
    course_duration decimal(3,1) NOT NULL,
    course_fee VARCHAR(30) NOT NULL,
    PRIMARY KEY(course_id)
);

insert into course_new (course_id,course_name,course_duration,course_fee) values(1,"Big Data",6.4,5000),(2,"Data Science",3.6,2000),(3,"Data Analyst",2.2,7000);

select * from course_new;

UPDATE course_new set course_fee = 8000 where course_id = 1;

drop table course_new;

--timestamp datatype now() it wont chnage wile updating record
create table course_new (
    course_id int NOT NULL,
    course_name VARCHAR(50) not NULL,
    course_duration decimal(3,1) NOT NULL,
    course_fee VARCHAR(30) NOT NULL,
    changed_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY(course_id)
);

insert into course_new (course_id,course_name,course_duration,course_fee) values(1,"Big Data",6.4,5000),(2,"Data Science",3.6,2000),(3,"Data Analyst",2.2,7000);

select * from course_new;


UPDATE course_new set course_fee = 8600 where course_id = 1;
insert into course_new (course_id,course_name,course_duration,course_fee) values(4,"Business analyst",9,9000);




--timestamp datatype now() it will chnage wile updating record
create table course_new (
    course_id int NOT NULL,
    course_name VARCHAR(50) not NULL,
    course_duration decimal(3,1) NOT NULL,
    course_fee VARCHAR(30) NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() on update CURRENT_TIMESTAMP(),
    PRIMARY KEY(course_id)
);

insert into course_new (course_id,course_name,course_duration,course_fee) values(1,"Big Data",6.4,5000),(2,"Data Science",3.6,2000),(3,"Data Analyst",2.2,7000);

select * from course_new;


UPDATE course_new set course_fee = 8600 where course_id = 1;


--session10 (Logical Operators)

select * from students where location != 'indore';

select * from course_new where course_name like "%data%";

--get all course which do not have word data
select * from course where course_name not like "%data%";

--all students from indore source of joining linkedin and year of experience greater then 8

select * from students where source_of_joining = "linkedin" and year_of_experience > 8 and location = "indore";

--allstudents year of experience less then 8 or greater then 10
select * from students where  year_of_experience < 8 or year_of_experience > 12;

select * from students where year_of_experience not between 8 and 12;

--12 and 8 inclusive
select * from students where year_of_experience between 8 and 12;

--get list of students which work in company  wamart , google

select * from students where student_company = 'Walmart' or student_company = 'Google';
select * from students where student_company in ('Walmart','Google');
select * from students where student_company not in ('Walmart','Google');


select * from course;

--course more then 3 month is master program otherwise diploma

select course_id, course_name,course_fee,
CASE 
    WHEN course_duration > 3 THEN  "Masters"
    ELSE  "Diploma"
END as course_type
FROM course;


-- students working in Walmart is product based otherwise serive based

select *  from students;

select student_id,first_name,last_name,student_company,
CASE 
    WHEN student_company in ("Walmart", "Flipcart") THEN  "Product Based"
    ELSE  "Service Based"
END as company_type
from students;


--session11 (Joins in SQL)

select course_name from course where course_id = (select student_course from students where first_name="ravi");

select students.first_name,students.last_name, course.course_name from students join course on students.student_course = course.course_id;

create table students_latest as select * from students;

create table course_latest as select * from course;

select * from course_latest;
select * from students;

delete from course_latest where course_id = 3;

select students_latest.first_name,students_latest.last_name, course_latest.course_name from students_latest join course_latest on students_latest.student_course = course_latest.course_id;

--left join
select students_latest.first_name,students_latest.last_name, course_latest.course_name from students_latest left join course_latest on students_latest.student_course = course_latest.course_id;

--right join
select students_latest.first_name,students_latest.last_name, course_latest.course_name from students_latest right join course_latest on students_latest.student_course = course_latest.course_id;



--full outer join
select students_latest.first_name,students_latest.last_name, course_latest.course_name from students_latest left join course_latest on students_latest.student_course = course_latest.course_id
union
select students_latest.first_name,students_latest.last_name, course_latest.course_name from students_latest right join course_latest on students_latest.student_course = course_latest.course_id;

--cross JOIN
select * from students,course;


--session 12 (Difference between where and having in mysql)

select source_of_joinin, count(*) as total from students GROUP BY source_of_joining where total >1;

select source_of_joining, count(*) as total from students GROUP BY source_of_joining having total <2;

--count of people reigistered through linkedin not good way use where clause insted of having for filer
select source_of_joining, count(*) as total from students GROUP BY source_of_joining having source_of_joining = 'linkedin';

--better query
select source_of_joining, count(*) as total from students where source_of_joining = 'linkedin' GROUP BY source_of_joining;

--location from which more then 1 student enrolled who have more then 5 year of experiencee
select location,count(*) as total from students where year_of_experience > 10 group by location having total > 1;



--session13 (Over Clause | Partition By Clause)
--https://onecompiler.com/mysql
create table employee (
    fname VARCHAR(40),
    lname VARCHAR(30),
    age int,
    salary INT,
    location VARCHAR(40)
);

insert into employee values("ajay","sharma",25,10000,"indore");
insert into employee values("amit","verma",20,12000,"indore");
insert into employee values("sumit","verma",2,18000,"bhopal");
insert into employee values("Raja","verma",27,19000,"bhopal");
insert into employee values("ravi","sharma",21,24000,"chhindwara");
insert into employee values("hariom","dhawan",24,35000,"indore");
insert into employee values("nira","verma",30,45000,"bhopal");
insert into employee values("nira1","verma1",30,18000,"bhopal");
insert into employee values("nira1","verma1",30,24000,"bhopal");


--how many people from each location with avg salary
select location,count(*),avg(salary) from employee group by location;

--error fname and lname should be in group by
select fname,lname,location,count(*),avg(salary) from employee group by location;

o/p -
fname	lname	location	count(*)	avg(salary)
sumit	verma	bhopal	5	24800
ravi	sharma	chhindwara	1	24000
ajay	sharma	indore	3	19000


select fname,lname,location,
count(location) over(PARTITION BY location) as total,
avg(salary) over(PARTITION BY location) as avg
from employee;

o/p -
fname	lname	location	total	avg
sumit	verma	bhopal	5	24800
Raja	verma	bhopal	5	24800
nira	verma	bhopal	5	24800
nira1	verma1	bhopal	5	24800
nira1	verma1	bhopal	5	24800
ravi	sharma	chhindwara	1	24000
ajay	sharma	indore	3	19000
amit	verma	indore	3	19000
hariom	dhawan	indore	3	19000


--session 14 (Row Number Function in MySQL )

--we use row_number() with order by, we can also use with partion by (optional),row number starts from 1 for each partition
--row number does not handle duplicates so we have rank and dense rank
--show salary in desc ORDER 
select fname,lname,location,salary,ROW_NUMBER() over(order by salary desc) as row_num from employee;

--5th hightest salary
select * from (select fname,lname,salary,ROW_NUMBER() over(order by salary desc) as rownum from employee ) temptable where rownum = 5;

--row number based on partion by location 
select fname,lname,location,salary,ROW_NUMBER() over(PARTITION BY location order by salary desc) as row_num from employee;


--highest salary getter from each location
select * from (select fname,lname,location,salary, ROW_NUMBER() over(PARTITION BY location order by salary desc) as rownum from employee) temptable where rownum = 1;


--session 15 (Rank and Dense Rank in MySQL)

select fname,lname,salary,row_number() over(order by salary desc) as rownum from employee;

select fname,lname,salary,rank() over(order by salary desc) as rownum from employee;

select fname,lname,salary,DENSE_RANK() over(order by salary desc) as rownum from employee;


select * from (select fname,lname,salary,DENSE_RANK() over(order by salary desc) as rownum from employee) temptable where rownum = 4;


--session16 (CTE in SQL (Common Table Expression) | SQL WITH Clause | CTE Query Performance | Advanced SQL)

create table orders (
    order_id int,
    order_date date,
    oorder_emp_id int,
    order_status VARCHAR(20)
);


insert into orders values(1,'2023-03-03',1,"Pending"),(2,'2023-04-04',1,"Complete"),(3,'2023-05-03',1,"Closed"),(4,'2023-03-05',2,"Pending"),(5,'2023-05-03',1,"Complete"),(6,'2023-06-03',2,"Close"),(7,'2023-02-03',3,"Pending");

SELECT * from orders;

--total order each customer has placed
-- i want to calculate premium customer(who placed more order)

select oorder_emp_id,count(*) as total_customer from orders group by oorder_emp_id;

--avg order placed by each customer (sub query)
select avg(total_customer) as  average_customer_order from (select oorder_emp_id,count(*) as total_customer from orders group by oorder_emp_id) x;

--avg order placed by each customer (CTE/WITH Clause)
WITH toal_customers_tbl (oorder_emp_id,total_customer) as
(select oorder_emp_id,count(*) as total_customer from orders group by oorder_emp_id)
select avg(total_customer) as avg_total from toal_customers_tbl;


--i want to find premium customer who placed more orders then avg number of orders(sub query)
select * from (select oorder_emp_id,count(*) as total_ord from orders group by oorder_emp_id)  total_tbl
JOIN
(select avg(total_ord) as avg_cust_order from (select oorder_emp_id,count(*) as total_ord from orders group By oorder_emp_id) x) avg_tbl
on total_tbl.total_ord > avg_tbl.avg_cust_order;

--1.total customer_orders per customer
with total_customer_order (oorder_emp_id,total_order) AS (select oorder_emp_id,count(*) as total_order from orders GROUP BY oorder_emp_id)
select * from total_customer_order;

--2.avg customer_orders per customer
with total_customer_order (oorder_emp_id,total_order) AS (select oorder_emp_id,count(*) as total_order from orders GROUP BY oorder_emp_id),
average_orders_tbl(avg_order) as (select avg(total_order) as avg_order from total_customer_order)
select * from average_orders_tbl;

--3.get to know which customer are premium customer
with total_customer_order (oorder_emp_id,total_order) AS (select oorder_emp_id,count(*) as total_order from orders GROUP BY oorder_emp_id),
average_orders_tbl(avg_order) as (select avg(total_order) as avg_order from total_customer_order)
select * from total_customer_order join average_orders_tbl on total_customer_order.total_order > average_orders_tbl.avg_order;

--i want to find premium customer who placed more orders then avg number of orders(WITH CTE)

-- 3 step PROCESS
--1.calculate total order per custmoer
--2.calculate avg order per cusmter
--3.get to know which customer is premium

with total_customer_order (oorder_emp_id,total_order) AS (select oorder_emp_id,count(*) as total_order from orders GROUP BY oorder_emp_id),
average_orders_tbl(avg_order) as (select avg(total_order) as avg_order from total_customer_order)
select * from total_customer_order join average_orders_tbl on total_customer_order.total_order > average_orders_tbl.avg_order;




--subquery - query1(query2(query3))

--CTE
--query1
--query2
--query3

--better this one less time taken
select * from orders where order_id = 1;

--not recommended more time taken
with order_cte as (
    select * from orders
)
select * from order_cte where order_id = 1;



--session17(SQL Internals | Indexes in SQL | Order of Execution in SQL | Advanced SQL | SQL Scenario based)

--one of the query format
--select top 3 city from students order by salary desc;
select top 2 oorder_emp_id,count(*) as total_customer from orders group by oorder_emp_id order by total_customer desc;



--SQL iNTERVIEW QUESTION

--SESSION1


--SESSION2
--#176. Second Highest Salary
--soluiton1
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee);


#more generic solution
--soluiton2
select IFNULL((select DISTINCT salary from Employee order by salary desc limit 1 offset 1),NULL) as SecondHighestSalary;

--solution3
select IFNULL((select salary  from (select distinct salary, dense_rank() over(order by salary desc) as dense_rank_num from Employee) tmp where dense_rank_num = 2),NULL) as SecondHighestSalary;

--FOR 3rd highest
select IFNULL((select DISTINCT salary from Employee order by salary desc limit 1 offset 2),NULL) as SecondHighestSalary;




--178. Rank Scores - dense_rank()
select score, dense_rank() over(order by score desc) as "rank" from Scores;

--180. Consecutive Numbers
select distinct l1.num as ConsecutiveNums from Logs l1
join Logs l2 on l1.id = l2.id+1 and l1.num = l2.num
join Logs l3 on l1.id = l3.id+2 and l1.num = l3.num;

--181. Employees Earning More Than Their Managers
select e1.name as Employee from Employee e1 join Employee e2 on e1.managerId = e2.id where e1.salary > e2.salary;


--182. Duplicate Emails

--solution1
select email from (select email,count(*) as cnt from Person group by email) tmp where cnt > 1;

--solution2
select email from Person group by email having count(email) > 1;


--183. Customers Who Never Order
--solution1
select Customers.name as Customers from Customers left join Orders ON Customers.id = Orders.customerId where Orders.customerId is null;

--solution2
select name as Customers from Customers where id not in (select customerId from Orders);


--184. Department Highest Salary
select Department.name as Department,Employee.name as Employee,salary from Employee join Department on Department.id = Employee.departmentId where (departmentId,salary) in (select departmentId,max(salary) from Employee group by  departmentId);


--Relations in SQL
--one to one 
--In a one-to-one relationship in a relational database, each record in the first table is related to one and only one record in the second table, and vice versa.
CREATE TABLE Person (
    PersonID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

CREATE TABLE Address (
    AddressID INT PRIMARY KEY,
    Street VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    PersonID INT UNIQUE, -- Foreign key referencing Person table
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

--retrieve a person along with their address
SELECT Person.FirstName, Person.LastName, Address.Street, Address.City, Address.State, Address.ZipCode
FROM Person
JOIN Address ON Person.PersonID = Address.PersonID;


--one to many (many to one relation)
--one record in the first table can be associated with multiple records in the second table. However, each record in the second table is associated with only one record in the first table. This is commonly implemented by having a foreign key in the "many" side table that references the primary key in the "one" side table.
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT, -- Foreign key referencing Department table
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

-- write a query to retrieve employees along with their department
SELECT Employee.FirstName, Employee.LastName, Department.DepartmentName
FROM Employee
JOIN Department ON Employee.DepartmentID = Department.DepartmentID;



--many to many relation
--a many-to-many relationship occurs when each record in Table A can be related to multiple records in Table B, and vice versa.
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Enrollment (
    StudentID INT,
    CourseID INT,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);


-- Insert students
INSERT INTO Students (StudentID, StudentName) VALUES (1, 'John Doe');
INSERT INTO Students (StudentID, StudentName) VALUES (2, 'Jane Smith');

-- Insert courses
INSERT INTO Courses (CourseID, CourseName) VALUES (101, 'Mathematics');
INSERT INTO Courses (CourseID, CourseName) VALUES (102, 'History');

-- Enroll students in courses
INSERT INTO Enrollment (StudentID, CourseID) VALUES (1, 101);  -- John Doe in Mathematics
INSERT INTO Enrollment (StudentID, CourseID) VALUES (1, 102);  -- John Doe in History
INSERT INTO Enrollment (StudentID, CourseID) VALUES (2, 101);  -- Jane Smith in Mathematics

select * from Enrollment;
--Get all students enrolled in a specific course:
select Students.StudentID, Students.StudentName
FROM Students
JOIN Enrollment ON Students.StudentID = Enrollment.StudentID
WHERE Enrollment.CourseID = 101;  -- Replace with the desired CourseID


--Get all courses a specific student is enrolled in:
select Courses.CourseID,Courses.CourseName from Courses
JOIN Enrollment ON Courses.CourseID = Enrollment.CourseID
where Enrollment.StudentID = 1;

--all students' names from the Enrollment table along with the corresponding course they are enrolled in
select Students.StudentName, Courses.CourseName from Students 
JOIN Enrollment ON Students.StudentID = Enrollment.StudentID
JOIN Courses ON Courses.CourseID = Enrollment.CourseID; 



--Candidate Key:

--A candidate key is a set of one or more columns that can uniquely identify each record in a table.
--From all the candidate keys, one is selected as the primary key.
--Each candidate key must be unique, and no subset of the candidate key should be unique.
--It can be a single column or a combination of multiple columns.


CREATE TABLE Employees (
    EmployeeID INT,
    EmployeeSSN VARCHAR(9),
    EmployeeEmail VARCHAR(100),
    PRIMARY KEY (EmployeeID),
    UNIQUE (EmployeeSSN),
    UNIQUE (EmployeeEmail)
);


--In this example, both EmployeeSSN and EmployeeEmail are candidate keys. However, EmployeeID is chosen as the primary key.


--Composite Key:

--A composite key is a key that consists of two or more columns to uniquely identify a record.
--Unlike a candidate key, a composite key is not necessarily unique by itself; its uniqueness is derived from the combination of its columns.
--Composite keys are often used when a single column does not provide enough uniqueness.

CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    ProductID INT,
    OrderDate DATE,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    UNIQUE (CustomerID, ProductID, OrderDate)
);

--In this example, the combination of CustomerID, ProductID, and OrderDate forms a composite key for uniqueness in the Orders table.

--In summary, a candidate key is a concept that refers to a set of columns that can uniquely identify records, and a composite key is a specific type of key that is composed of multiple columns. A composite key can be a candidate key if it uniquely identifies records, but not all candidate keys are necessarily composite.




--Normalization
--Normalization is a database design technique that organizes tables and fields of a relational database to reduce redundancy and dependency. The main goals of normalization are to eliminate data anomalies, ensure data integrity, and simplify data maintenance.

--There are several normal forms (1NF, 2NF, 3NF, BCNF, etc.), 

--Normalization helps in avoiding data redundancy, improving data integrity, and making the database more maintainable. However, it's important to strike a balance and not over-normalize, as it may lead to complex queries and reduced performance in some cases.



--First Normal Form (1NF):
--Eliminate duplicate columns from the same table.
--Create a separate table for each group of related data.
--Identify a unique column or set of columns (primary key) for each table.

-- Unnormalized table
CREATE TABLE UnnormalizedTable (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Course1 VARCHAR(50),
    Course2 VARCHAR(50),
    Course3 VARCHAR(50)
);

-- 1NF: Separate table for courses
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    StudentID INT,
    CourseName VARCHAR(50),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);


--Second Normal Form (2NF):

--Meet the requirements of 1NF.
--Remove partial dependencies by moving subsets of data that apply to multiple rows to separate tables.
-- 1NF: Students and Courses tables
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    Grade VARCHAR(2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);


--Third Normal Form (3NF):

--Meet the requirements of 2NF.
--Eliminate transitive dependencies by removing columns not dependent on the primary key.

-- 2NF: Separate Enrollments table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Grades (
    EnrollmentID INT PRIMARY KEY,
    Grade VARCHAR(2),
    FOREIGN KEY (EnrollmentID) REFERENCES Enrollments(EnrollmentID)
);


--Redundancy
--Redundancy in the context of relational databases refers to the unnecessary repetition or duplication of data within a database. Redundancy can lead to several issues, including increased storage requirements, data inconsistency, and difficulties in maintaining and updating data. The process of minimizing redundancy is known as normalization, which is a crucial aspect of database design. Here are some points related to redundancy in SQL databases

--Types of Redundancy:
--Data Redundancy: The same data is stored in multiple places.
--Structural Redundancy: Unnecessary repetition of the same data structure.
--Functional Redundancy: Storing the same information in multiple tables.
-- Redundant Data
CREATE TABLE Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50),
    ManagerName VARCHAR(50)
);

-- Non-Redundant Data (Normalized)
CREATE TABLE Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

CREATE TABLE Manager (
    DeptID INT PRIMARY KEY,
    ManagerName VARCHAR(50),
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);


--By minimizing redundancy through normalization, databases become more efficient, easier to maintain, and less prone to data inconsistencies.