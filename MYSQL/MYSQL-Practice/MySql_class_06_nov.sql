
create DATABASE test_db;

use test_db;

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
insert into employee value(3,'Sumit',22,'2021-08-11',11000,'Noida');
insert into employee value(4,'Raja',27,'2021-08-12',50000,'Gurgaon');
select * from employee;



--how to perform multi updates

--dont use it for lab environment # 0 = off,1 = on
SET SQL_SAFE_UPDAES = 0;

update employee set age = 20,salary=25000 where hiring_date = '2021-08-10';


--may be it can require commit command to update data before SELECT command
commit;

select * from employee;


create table auto_inc_exmp
(
    id int  AUTO_INCREMENT,
    name VARCHAR(20),
    PRIMARY KEY (id)
);


insert into auto_inc_exmp(name) values('Ajay');
insert into auto_inc_exmp(name) values('Rahul');

select * from auto_inc_exmp;

--use of limit 
select * from employee limit 2;


--sorting data in mysql
select * from employee;

--arrange data in ascending order
select * from employee order by name;

--arrange data in descending order
select * from employee order by name desc;


--display employee data in desc order of salary and if salaries are same for more than one employees
--arrange their data in ascending order of name
select * from employee order by salary desc,name asc;

--when we ignore multilevel ordering
select * from employee order by salary desc;


--write a query to find the employee who is getting maximum salary
select * from employee order by salary desc limit 1; 

--write a query to find the employee who is getting minimum salary
select * from employee order by salary limit 1; 


--conditional operators -> <,>,<=,=>
--logical operators -> AND,OR,NOT

SELECT * from employee;

--list all employee who are getting salary more then 20000
select * from employee where salary>20000;

--list all employee who are getting salary less then  20000
select * from employee where salary<20000;

--list all employee who are getting salary more then or equal to 20000
select * from employee where salary>=20000;

--list all employee who are getting salary less then or equal to 20000
select * from employee where salary<=20000;


--filter the record where age of employees is not equal to 20;
--we can use != ir we can use <>
select * from employee where age != 20;
select * from employee where age <> 20;

--sfind those employee who joined the company on 2021-08-11 and their salary is less than 11500
select * from employee where hiring_date = '2021-08-11' and salary <11500;


--sfind those employee who joined the company after 2021-08-11 or their salary is less than 25000
select * from employee where hiring_date = '2021-08-10' or salary <20000;

select * from employee;

--how to use between operation in where clause
--get all employees data who joined the company between hiring_date 2021-08-05 to 2021-08-11
select * from employee where hiring_date between '2021-08-09' and '2021-08-10';


--get all employees data who are getting salary in the range of 10000 to 20000
select * from employee where salary between 10000 and 20000;



--how to use LIKE operation in where clause
-- % -> Zero,one or more than one characters;
-- _ -> only one characters

-- get all those emplyees whose name starts with 'A'
select * from employee where name like  'A%';

-- get all those emplyees whose name ends with 'y'
select * from employee where name like  '%y';


-- get all those emplyees whose name starts with 'A' and ends with 'y'
select * from employee where name like  'A%y';

--get all those employees whose name will have exact 5 characters
select * from employee where name like '_____';

--return all those employees whose name contains atleast 5 characters
select * from employee where name like '%____%';


insert into employee values(10,'Kapil',null,'2021-08-10',10000,'Assam');
insert into employee values(11,'Rohit',30,'2021-08-10',null,'Assam');

--get all data where age is null
select * from employee where age is null;

--get all data where salary is not null
select * from employee where salary is not null;


--table and data for group GROUP BY
create table orders_data
(
    cust_id int,
    order_id int,
    country VARCHAR(50),
    state VARCHAR(50)
);


insert into orders_data values(1,100,'USA','Seattle');
insert into orders_data values(2,101,'INDIA','UP');
insert into orders_data values(2,103,'INDIA','Bihar');
insert into orders_data values(4,108,'USA','WDC');
insert into orders_data values(5,109,'UK','London');
insert into orders_data values(4,110,'USA','WDC');
insert into orders_data values(3,120,'INDIA','AP');
insert into orders_data values(2,121,'INDIA','Goa');
insert into orders_data values(1,131,'USA','Seattle');
insert into orders_data values(6,142,'USA','Seattle');
insert into orders_data values(7,150,'USA','Seattle');


--calculate total orders placed country wise
select country,count(*) as order_count_by_each_country from orders_data group by country;


select age,sum(salary) as total_salary_by_each_age_group from employee group by age;


--calculate different aggregated matrices for salary
select age,
       sum(salary) as total_salary_by_each_age_group,
       max(salary) as max_salary_by_each_age_group,
       min(salary) as min_salary_by_each_age_group,
       avg(salary) as avg_salary_by_each_age_group,
       count(*) as total_employee_by_each_age_group
from employee group by age;


select * from employee;
