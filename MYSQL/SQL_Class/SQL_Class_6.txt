create database test;

use test;

create table employees(
  emp_id int,
  emp_name varchar(50),
  mobile BIGINT,
  dept_name varchar(50),
  salary int 
);

insert into employees values(1,'Shashank',778768768,'Software',1000);
insert into employees values(2,'Rahul',876778877,'IT',2000);
insert into employees values(3,'Amit',098798998,'HR',5000);

insert into employees values(4,'Nikhil',67766767,'IT',3000);

select * from employees;

--- Create views in SQL
create view employee_data_for_finance as select emp_id, emp_name,salary from employees;

select * from employee_data_for_finance;

--- Create logic for department wise salary sum
create view department_wise_salary as select dept_name, sum(salary) from employees group by dept_name;

drop view department_wise_salary;

create view department_wise_salary as select dept_name, sum(salary) as total_salary from employees group by dept_name;

select * from department_wise_salary;

# Union and Union all

create table student
(
    stu_id int,
    name varchar(50), 
    email varchar(50), 
    city varchar(50)
 );
 
 insert into student values(1,'Shashank','abc@gmail.com', 'lucknow');
 insert into student values(2,'Rahul','abc1@gmail.com', 'mp');
  insert into student values(3,'Amit','ab2@gmail.com', 'noida');
   insert into student values(4,'Nikhil','abc3@gmail.com', 'bangalore');
    insert into student values(5,'Sunny','ab4@gmail.com', 'bangalore');
    
create table student2
(
    stu_id int,
    name varchar(50), 
    email varchar(50), 
    city varchar(50)
 );


insert into student2 values(1,'Shashank','abc@gmail.com', 'lucknow');
 insert into student2 values(6,'Anuj','abc5@gmail.com', 'mp');
  insert into student2 values(8,'Mohit','ab7@gmail.com', 'noida');
   insert into student2 values(10,'Sagar','abc10@gmail.com', 'bangalore');
    insert into student2 values(5,'Sunny','ab4@gmail.com', 'bangalore');
    
select * from student2;


--- We are organizing an tournament between College-1 and College-2, we need details of all students from both college
select * from student
UNION
select * from student2;

--- how to use union all
select * from student
UNION ALL
select * from student2;

--- Case 1 - Not Failed

select stu_id, `name` from student
UNION
select `name`, stu_id from student2;

--- Case 2 - Not Failed
select stu_id, name from student
UNION
select stu_id, name from student2;

--- Case 3 - Not Failed
select stu_id as stu_id_college_1 , name from student
UNION
select stu_id as stu_id_college_2, name from student2;

--- Case 4 - Not Failed
select stu_id from student
UNION
select email from student2;


select 1 as salary
UNION
select 'Shashank' as name;

select 1 as salary, 'Hello' as message
UNION
select 'Shashank' as name;

--- Common table expression

create table amazon_employees(
    emp_id int,
    emp_name varchar(20),
    dept_id int,
    salary int

 );

 insert into amazon_employees values(1,'Shashank', 100, 10000);
 insert into amazon_employees values(2,'Rahul', 100, 20000);
 insert into amazon_employees values(3,'Amit', 101, 15000);
 insert into amazon_employees values(4,'Mohit', 101, 17000);
 insert into amazon_employees values(5,'Nikhil', 102, 30000);

 create table department
 (
    dept_id int,
    dept_name varchar(20) 
  );

  insert into department values(100, 'Software');
    insert into department values(101, 'HR');
      insert into department values(102, 'IT');
        insert into department values(103, 'Finance');

--- Write a query to print the name of department along with the total salary paid in each department
--- Normal approach
select d.dept_name, tmp.total_salary
from (select dept_id , sum(salary) as total_salary from amazon_employees group by dept_id) tmp
inner join department d on tmp.dept_id = d.dept_id;

--- how to do it using with clause??
with dept_wise_salary as (select dept_id , sum(salary) as total_salary from amazon_employees group by dept_id)

select d.dept_name, tmp.total_salary
from dept_wise_salary tmp
inner join department d on tmp.dept_id = d.dept_id;

select * from dept_wise_salary;


--- Write a Query to generate numbers from 1 to 10 in SQL

with recursive generate_numbers as   
(
  select 1 as n
  union 
  select n+1 from generate_numbers where n<10
) 

select * from generate_numbers;


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

--- for our CTO 'Asha', present her org chart

with recursive emp_hir as  
(
   select id, name, manager_id, designation from emp_mgr where name='Asha'
   UNION
   select em.id, em.name, em.manager_id, em.designation from emp_hir eh inner join emp_mgr em on eh.id = em.manager_id
)

select * from emp_hir;

--- Print level of employees as well
with recursive emp_hir as  
(
   select id, name, manager_id, designation, 1 as lvl from emp_mgr where name='Asha'
   UNION
   select em.id, em.name, em.manager_id, em.designation, eh.lvl + 1 as lvl from emp_hir eh inner join emp_mgr em on eh.id = em.manager_id
)

select * from emp_hir;
