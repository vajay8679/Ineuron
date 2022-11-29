create DATABASE test;

use test;

create table employees
(
    emp_id int,
    emp_name VARCHAR(50),
    mobile  BIGINT,
    dept_name VARCHAR(50), 
    salary int
);


insert into employees values(1,'Shashank',7247593467,'Software',1000);
insert into employees values(2,'Amit',9247593467,'IT',2000);
insert into employees values(3,'Rahul',8247593467,'HR',5000);
insert into employees values(4,'Sumit',6247593467,'IT',3000);


SELECT * from employees;

--create views in SQL
create view employee_data_for_finance as select emp_id,emp_name,salary from employees;

select * from employee_data_for_finance;

--create logic department wise salary sum
create view department_wise_salary as select dept_name,sum(salary) from employees group by dept_name;

select * from department_wise_salary;

drop view department_wise_salary;

create view department_wise_salary as select dept_name,sum(salary) as total_salary from employees group by dept_name;

select * from department_wise_salary;



--UNION and UNION ALL Operation
CREATE table student
(
    stu_id int,
    name VARCHAR(50),
    email VARCHAR(50),
    city VARCHAR(50)
);

insert into student VALUES (1,'ajay','abc@gmail.com','indore');
insert into student VALUES (2,'amit','abc1@gmail.com','mp');
insert into student VALUES (3,'sumit','abc2@gmail.com','noida');
insert into student VALUES (4,'raja','abc3@gmail.com','banglore');
insert into student VALUES (5,'ravi','abc4@gmail.com','banglore');

select * from student;


CREATE table student2
(
    stu_id int,
    name VARCHAR(50),
    email VARCHAR(50),
    city VARCHAR(50)
);

insert into student2 VALUES (1,'ajay','abc@gmail.com','indore');
insert into student2 VALUES (6,'Anuj','abc5@gmail.com','mp');
insert into student2 VALUES (8,'Mohi','abc6@gmail.com','noida');
insert into student2 VALUES (10,'raja','abc10@gmail.com','banglore');
insert into student2 VALUES (5,'ravi','abc4@gmail.com','banglore');

--we are oranizing a tournament between college-1 and college-2 we need details of all students from both college
select * from student
UNION
select * from student2;

select * from student
UNION ALL
select * from student2;


--case 1 - not failed
select stu_id,name from student
UNION
select name,stu_id from student2;

--case 2 - not failed
select stu_id,name from student
UNION
select stu_id,name from student2;


--case 3 - not failed
select stu_id as stu_id_college_1,name from student
UNION
select stu_id,name from student2;


--case 4 - not failed
select stu_id from student
UNION
select name from student2;


--case 4 - not failed
select stu_id from student
UNION
select email from student2;



select 1 as salary 
UNION
select 'ajay' as name;


--common table expression

create table amazon_employees
(
    emp_id int,
    emp_name VARCHAR(50),
    dept_id int,
    salary int
);

insert into amazon_employees VALUES (1,'Ajay',100,10000);
insert into amazon_employees VALUES (2,'Rahul',100,30000);
insert into amazon_employees VALUES (3,'Amit',101,15000);
insert into amazon_employees VALUES (4,'Mohit',101,17000);
insert into amazon_employees VALUES (5,'Shashank',102,30000);


create table department
(
    dept_id int,
    dept_name VARCHAR(50)
);

insert into department VALUES (100,'Software');
insert into department VALUES (101,'HR');
insert into department VALUES (102,'IT');
insert into department VALUES (103,'Finance');

--write q query to print the name of department along with the total salary paid in each department
--Normal Approach
SELECT d.dept_name,tmp.total_salary
from (select dept_id,sum(salary) as total_salary from amazon_employees group by dept_id) tmp
inner join department d on tmp.dept_id = d.dept_id;

--how to do it using with clause??
with dept_wise_salary as (select dept_id,sum(salary) as total_salary from amazon_employees group by dept_id)

select d.dept_name,tmp.total_salary
from dept_wise_salary tmp
inner join department d on tmp.dept_id = d.dept_id;

select * from dept_wise_salary;




--write a query to generate numbers from 1 to 10 in SQL

with recursive generate_numberss as 
(
    select 1 as n
    union 
    select n+1 from generate_numberss where n<10
)

select * from generate_numberss;



create table emp_mgr
(
id int,
name varchar(50),
manager_id int,
designation varchar(50),
primary key (id)
);


insert into emp_mgr values(1,'Shripath',null,'CEO');
insert into emp_mgr values(2,'Satya',5,'SDE');
insert into emp_mgr values(3,'Jia',5,'DA');
insert into emp_mgr values(4,'David',5,'DS');
insert into emp_mgr values(5,'Michael',7,'Manager');
insert into emp_mgr values(6,'Arvind',7,'Architect');
insert into emp_mgr values(7,'Asha',1,'CTO');
insert into emp_mgr values(8,'Maryam',1,'Manager');


select * from emp_mgr;


--for our CTO 'Asha', present her org chart

with recursive emp_hir as
(
    select id,name,manager_id,designation from emp_mgr where name = 'Asha'
    UNION
    select em.id,em.name,em.manager_id,em.designation from emp_hir eh inner join emp_mgr em on eh.id = em.manager_id
)

select * from emp_hir;



with recursive emp_hir as  
(
   select id, name, manager_id, designation,1 as lvl from emp_mgr where name='Asha'
   UNION
   select em.id, em.name, em.manager_id, em.designation,eh.lvl + 1 as lvl from emp_hir eh inner join emp_mgr em on eh.id = em.manager_id
)

select * from emp_hir;