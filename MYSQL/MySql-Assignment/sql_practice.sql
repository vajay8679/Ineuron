
create DATABASE sql_practice;

use sql_practice;


-- 1. Write a query to display the columns in a specific order, such as order date, salesman ID, order number, and purchase amount for all orders.

--create table for order details 
create table if not exists orders
(
    ord_no int not NULL,
    purch_amt double NOT NULL,
    ord_date DATE NOT NULL,
    customer_id int NOT NULL,
    salesman_id int NOT NULL,
    constraint pk primary key (ord_no),
);

--insert data into table orders 
insert into orders values(70001,150.5,'2012-10-05',3005,5002);
insert into orders values(70009,270.65,'2012-09-10',3001,5005);
insert into orders values(70002,65.26,'2012-10-05',3002,5001);
insert into orders values(70004,110.5,'2012-08-17',3009,5003);
insert into orders values(70007,948.5,'2012-09-10',3005,5002);
insert into orders values(70005,2400.6,'2012-07-27',3007,5001);
insert into orders values(70008,5760,'2012-09-10',3002,5001);
insert into orders values(70010,1983.43,'2012-10-10',3004,5006);
insert into orders values(70003,2480.4,'2012-10-10',3009,5003);
insert into orders values(70012,250.45,'2012-06-27',3008,5002);
insert into orders values(70011,75.29,'2012-08-17',3003,5007);
insert into orders values(70013,3045.6,'2012-04-25',3002,5001);

select * from orders;

select ord_date as Order_Date,salesman_id as Salesman_Id,ord_no as Order_Number,purch_amt as Purchase_Amount from orders;


------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################


-- 2. From the following table, write a SQL query to locate salespeople who live in the city of 'Paris'. Return salesperson's name, city.

--create table for sales person details
create table if not exists sales_persons_details
(
    salesman_id int not null,
    name varchar(50),
    city varchar(80),
    commission double,
    constraint pk Primary Key (salesman_id)
);

--insert data into table sales_persons_details 
insert into sales_persons_details values(5001,'James Hoog','New York',0.15);
insert into sales_persons_details values(5002,'Nail Knite','Paris',0.13);
insert into sales_persons_details values(5005,'Pit Alex','London',0.11);
insert into sales_persons_details values(5006,'Mc Lyon','Paris',0.14);
insert into sales_persons_details values(5007,'Paul Adam','Rome',0.13);
insert into sales_persons_details values(5003,'Lauson Hen','San Jose',0.12);

select * from sales_persons_details;

select name,city from sales_persons_details where city = 'Paris';

----------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################


-- 3. From the following table, write a SQL query to select a range of products whose price is in the range Rs.200 to Rs.600. Begin and end values are included. Return pro_id, pro_name, pro_price, and pro_com.

create table if not exists products 
(
    pro_id int not NULL,
    pro_name varchar(50) not null,
    pro_price double not null,
    pro_com int not null,
    constraint pk PRIMARY KEY (pro_id) 
);

insert into products VALUES(101,'Motherboard',3200.00,15);
insert into products VALUES(102,'Keyboard',450.00,16);
insert into products VALUES(103,'ZIP drive',250.00,14);
insert into products VALUES(104,'Speaker',550.00,16);
insert into products VALUES(105,'Monitor',5000.00,11);
insert into products VALUES(106,'DVD drive',900.00,12);
insert into products VALUES(107,'CD drive',800.00,12);
insert into products VALUES(108,'Printer',2600.00,13);
insert into products VALUES(109,'Refill cartridge',350.00,13);
insert into products VALUES(110,'Mouse',250.00,12);

select * from products;

select pro_id as Product_Id,pro_name as Product_Name,pro_price as Product_Price,pro_com as Pro_Com from products where pro_price between 200 and 600;


------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################


-- 4.From the following table, write a SQL query to find the items whose prices are higher than or equal to $550. Order the result by product price in descending, then product name in ascending.

select pro_name as Product_Name,pro_price as Product_Price from products where pro_price >= 550 order by pro_price desc,pro_name;


------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################


-- 5. From the following table, write a SQL query to find details of all orders excluding those with ord_date equal to '2012-09-10' and salesman_id higher than 5005 or purch_amt greater than 1000.Return ord_no, purch_amt, ord_date, customer_id and salesman_id.

select ord_no as Order_Number,purch_amt as Purchase_Amout,ord_date as Order_Date,customer_id as Customer_Id,salesman_id as Salesman_Id from orders where 
(ord_date != '2012-09-10') and (salesman_id <= 5005 or purch_amt <= 1000);



------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################

-- 6. Create the table world with your schema and find the below queries !

create table if not exists world 
(
    id int not null AUTO_INCREMENT,
    name varchar(100) not NULL,
    continent varchar(50) not NULL,
    area int not null,
    population bigint not null,
    gdp bigint not NULL,
    constraint pk primary key (id)
);

insert into world(name,continent,area,population,gdp) values('Afghanistan','Asia',652230,25500100,20343000000);
insert into world(name,continent,area,population,gdp)  values('Albania','Europe',28748,2831741,12960000000);
insert into world(name,continent,area,population,gdp)  values('Algeria','Africa',2381741,37100000,188681000000);
insert into world(name,continent,area,population,gdp)  values('Andorra','Europe',468,78115,3712000000);
insert into world(name,continent,area,population,gdp)  values('Angola','Africa',1246700,20609294,100990000000);
insert into world(name,continent,area,population,gdp)  values('Dominican Republic','Caribbean',48671,9445281,58898000000);
insert into world(name,continent,area,population,gdp)  values('China','Asia',9596961,1365370000,8358400000000);
insert into world(name,continent,area,population,gdp)  values('Colombia','South America',1141748,47662000,369813000000);
insert into world(name,continent,area,population,gdp)  values('Comoros','Africa',1862,743798,616000000);
insert into world(name,continent,area,population,gdp)  values('Denmark','Europe',43094,5634437,314889000000);
insert into world(name,continent,area,population,gdp)  values('Djibouti','Africa',23200,886000,1361000000);
insert into world(name,continent,area,population,gdp)  values('Dominica','Caribbean',751,71293,499000000);


--1. Write a query to fetch which country has the highest population?
select name as Country_Name,population as Maximum_Population from world order by population desc limit 1;

--2.write a query to fetch the name of the country which has the least gdp?
select name as Country_Name,gdp as Minimum_Gdp from world order by gdp asc limit 1;

--3. Write a query to fetch the name of the country which ends with letter C?
select name as Country_Name from world where name like '%c';

--4.write a query to fetch the name of the country which starts with letter D?
select name as Country_Name from world where name like 'D%';

--5.write query to fetch which continent has highest gdp?
select continent as Continent_Name,sum(gdp) as Maximum_GDP_Continent from world group by (continent) order by Maximum_GDP_Continent desc limit 1; 

--6.Give the total GDP of Africa?
select continent as Continent_Name,sum(gdp) as Total_GDP from world where continent = 'Africa'; 

--7.write a query to fetch the total population for each continent?
select continent as Continent_Name,sum(population) as Total_Population_Per_Continent from world group by (continent); 

--8. For each relevant continent show the number of countries that has a population of at least 200000000?
select continent as Continent_Name,count(name) as Number_Of_Country from world  where population >= 200000000 group by continent; 



------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################


--7. Problem statement: Suppose we have two table students and course
create table students
(student_id int,
student_name varchar(60) not null,
city varchar(60) not null,
primary key(student_id)
);


create table course
(student_id int,
course_name varchar(60) not null,
Marks int not null,
primary key(student_id),
foreign key(student_id) references students(student_id)
);


insert into students values(200,'John Doe','Delhi'),
(210,'John Doe','Delhi'),
(220,'Moon ethan','Rajasthan'),
(230,'Jessie','Bangalore'),
(240,'Benbrook','Bihar'),
(250,'Ethan','Bihar'),
(260,'Johnnie','Bangalore'),
(270,'Goh','Delhi'),(380,'John Doe','Delhi'),
(280,'Pavi','Delhi'),
(290,'Sanvi','Rajasthan'),
(300,'Navyaa','Bangalore'),
(310,'Ankul','Bihar'),
(311,'Hitanshi','Bihar'),
(312,'Aayush','Bangalore'),
(313,'Rian','Delhi');


insert into course values(200,'Datascience',75),
(210,'Datascience',75),
(220,'Dataanalyst',80),
(230,'Dataanalyst',80),
(240,'Dataanalyst',84),
(250,'Dataanalyst',50),
(260,'Datascience',80),
(270,'Datascience',99),
(380,'Datascience',45),
(280,'Datascience',78),
(290,'Dataanalyst',78),
(300,'Computer vision',90),
(310,'Computer vision',90),
(311,'Computer vision',75),(312,'Computer vision',39);

select * from course;
select * from students;


--Questions :
--q1. write a query to fetch the names of the students having maximum marks in each course?
select tmp.student_id,std.student_name,tmp.course_name,tmp.Marks,tmp.max_marks_in_each_course
from (select *,
             row_number() over(partition by course_name order by Marks desc) as max_marks_in_each_course
      from course) tmp  inner join (select student_name,student_id from students  ) std
      on  std.student_id =tmp.student_id 
where tmp.max_marks_in_each_course = 1;

--q2. write a query to fetch the names of the students having 3th highest marks from each course?
select tmp.student_id,std.student_name,tmp.course_name,tmp.Marks,tmp.3rd_max_marks_in_each_course
from (select *,
             row_number() over(partition by course_name order by Marks desc) as 3rd_max_marks_in_each_course
      from course) tmp  inner join (select student_name,student_id from students  ) std
      on  std.student_id =tmp.student_id 
where tmp.3rd_max_marks_in_each_course = 3;

--q3. write a query to fetch the names of the students having minimum marks in each course?
select tmp.student_id,std.student_name,tmp.course_name,tmp.Marks,tmp.min_marks_each_in_course
from (select *,
             row_number() over(partition by course_name order by Marks asc) as min_marks_each_in_course
      from course) tmp  inner join (select student_name,student_id from students  ) std
      on  std.student_id =tmp.student_id 
where tmp.min_marks_each_in_course = 1;

--q4. write a query to fetch the names of the students having 4th least marks from each course?
select tmp.student_id,std.student_name,tmp.course_name,tmp.Marks,tmp.4th_min_marks_each_in_course
from (select *,
             row_number() over(partition by course_name order by Marks asc) as 4th_min_marks_each_in_course
      from course) tmp  inner join (select student_name,student_id from students  ) std
      on  std.student_id =tmp.student_id 
where tmp.4th_min_marks_each_in_course = 4;

--q5. write a query to fetch the city name of the students who have 2nd highest marks?
select tmp.student_id,std.city,tmp.course_name,tmp.Marks,tmp.2nd_max_marks_in_each_course
from (select *,
             row_number() over(partition by course_name order by Marks desc) as 2nd_max_marks_in_each_course
      from course) tmp  inner join (select city,student_id from students) std
      on  std.student_id =tmp.student_id 
where tmp.2nd_max_marks_in_each_course = 2;

--q6. write a query to fetch the count of each city?
select city,count(*) as city_count from students group by city;

--q7. write a query to fetch the names of the students who are from the same city?
select city,GROUP_CONCAT(student_name) as student from students group by city;

--q8.write a query to fetch the names of students starting with 'A'?
select student_name from students where student_name like 'A%';

--q9.write a query to fetch the count of students' names having the same marks in each course?
select course_name,count(*) from course group by course_name;  

select count(std.student_id) as total_number,tmp.course_name
from (select *,
             row_number() over(partition by course_name ) as 2nd_max_marks_in_each_course
      from course) tmp  inner join (select city,student_id from students) std
      on  std.student_id =tmp.student_id 
group by tmp.course_name;


--q10.write a query to fetch the count of students from each city?
select count(*) as total_num_of_student,city from students group by city;

--Hint : You must use Joins, Windows functions and CTE


------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################


--8. Create a table below.
--(player_id, event_date) is the primary key of this table.


create table if not exists player_records
(
    player_id int not null,
    device_id int not null,
    event_date date not null,
    games_played int not null,
    constraint pk PRIMARY KEY (player_id,event_date)
);

insert into player_records values(1,2,'2016-03-01',5);
insert into player_records values(1,2,'2016-05-02',6);
insert into player_records values(2,3,'2017-06-25',1);
insert into player_records values(3,1,'2016-03-02',0);
insert into player_records values(3,4,'2018-07-03',5);

select * from player_records;



--This table shows the activity of players of some games.Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.Write an SQL query to report the first login date for each player.Return the result table in any order.The query result format is in the following example.

select 
     tmp.player_id,tmp.event_date
from (select *,
        row_number() over(partition by player_id order by event_date asc) as row_num
     from player_records) tmp
where tmp.row_num = 1;



------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################



--9. Create a table below.
--product_id is the primary key for this table.low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
create table if not exists products 
(
    product_id int not null,
    low_fats enum('Y','N'),
    recyclable enum('Y','N'),
    constraint pk PRIMARY KEY (product_id)
);

insert into products values(0,'Y','N');
insert into products values(1,'Y','Y');
insert into products values(2,'N','Y');
insert into products values(3,'Y','Y');
insert into products values(4,'N','N');

select * from products;

--Write an SQL query to find the ids of products that are both low fat and recyclable.Return the result table in any order.The query result format is in the following example.

select product_id from products where low_fats = 'Y' and recyclable = 'Y';




------------------------------------------------------------------------------------------------------------------------------------------------------
--######################################################################################################################################################



--10. Create a table below.
create table if not exists country_desc
(
    name varchar(70) not null,
    region varchar(50) not null,
    area bigint not null,
    population bigint not null,
    gdp bigint
);


insert into country_desc values('Afghanistan','South Asia',652225,26000000,null);
insert into country_desc values('Albania','Europe',3200000,3200000,6656000000);
insert into country_desc values('Algeria','Middle East',2400000,32900000,75012000000);
insert into country_desc values('Andorra','Europe',468,64000,null);


--1. Select the statement that shows the sum of population of all countries i
select sum(population) as Total_population_of_worlds from country_desc where region='Europe';

--2. Select the statement that shows the number of countries with population smaller than 150000
select count(name) as Total_Count from country_desc where population < 150000;

--3. Select the list of core SQL aggregate functions
select region,
       sum(gdp) as total_gdp_by_each_region,
       max(gdp) as max_gdp_by_each_region,
       min(gdp) as min_gdp_by_each_region,
       avg(gdp) as avg_gdp_by_each_region,
       count(*) as total_gdp_by_each_region
from country_desc group by region;

--4. Select the result that would be obtained from the following code: (Invalid use of Group by function so we are getting error)
 SELECT region, SUM(area)
   FROM country_desc 
   WHERE SUM(area) > 150000
   GROUP BY region;


--5. Select the statement that shows the average population of 'Poland', 'Germany' and 'Denmark'
 SELECT AVG(population) FROM country_desc WHERE name in ('Poland', 'Germany', 'Denmark');


--6. Select the statement that shows the medium population density of each region
 SELECT region, SUM(population)/SUM(area) AS density FROM country_desc GROUP BY region;


--7. Select the statement that shows the name and population density of the country with the largest population
 SELECT name, population/area AS density_of_Country FROM country_desc where population = (select max(population) from country_desc);

