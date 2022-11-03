# Hive_Assignments

1. Download vechile sales data -> https://github.com/shashank-mishra219/Hive-Class/blob/main/sales_order_data.csv
2. Store raw data into hdfs location
3. Create a internal hive table "sales_order_csv" which will store csv data sales_order_csv .. make sure to skip header row while creating table
4. Load data from hdfs path into "sales_order_csv" 
5. Create an internal hive table which will store data in ORC format "sales_order_orc"
6. Load data from "sales_order_csv" into "sales_order_orc"

Perform below menioned queries on "sales_order_orc" table :

a. Calculatye total sales per year
b. Find a product for which maximum orders were placed
c. Calculate the total sales for each quarter
d. In which quarter sales was minimum
e. In which country sales was maximum and in which country sales was minimum
f. Calculate quartelry sales for each city
h. Find a month for each year in which maximum number of quantities were sold
Footer


#####################PRACTICAL OPERATIONS###################################

 STEP - 1 (Download vechile sales data -> https://github.com/shashank-mishra219/Hive-Class/blob/main/sales_order_data.csv)


Downloaded Data from github and took sales_order_data.csv file in one seperate folder with name Hive_Assignment

git clone https://github.com/shashank-mishra219/Hive-Class.git


 STEP - 2 (Store raw data into hdfs location)STEP - 2 (Store raw data into hdfs location)

I created table sales_order_data.csv into hdfs and move into a folder

vim sales_order_data.csv

copy data into  hive_class folder

cp sales_order_data.csv /tmp/hive_class/


 STEP - 3  (Create a internal hive table "sales_order_csv" which will store csv data sales_order_csv .. make sure to skip header row while creating table)


create a database

create database hive_assignment;

use hive_assignment;

create table sales_order_csv
(
ORDERNUMBER int,
QUANTITYORDERED int,
PRICEEACH float,
ORDERLINENUMBER int,
SALES float,
STATUS string,
QTR_ID int,
MONTH_ID int,
YEAR_ID int,
PRODUCTLINE string,
MSRP int,
PRODUCTCODE string,
PHONE string,
CITY string,
STATE string,
POSTALCODE string,
COUNTRY string,
TERRITORY string,
CONTACTLASTNAME string,
CONTACTFIRSTNAME string,
DEALSIZE string
)
row format delimited
fields terminated by ','
tblproperties("skip.header.line.count"="1")
; 



 STEP - 4 (Load data from hdfs path into "sales_order_csv")


load data local inpath 'file:///tmp/hive_class/sales_order_data.csv/' into table sales_order_csv;


 STEP - 5 (Create an internal hive table which will store data in ORC format "sales_order_orc")


create table sales_order_orc
(
ORDERNUMBER int,
QUANTITYORDERED int,
PRICEEACH float,
ORDERLINENUMBER int,
SALES float,
STATUS string,
QTR_ID int,
MONTH_ID int,
YEAR_ID int,
PRODUCTLINE string,
MSRP int,
PRODUCTCODE string,
PHONE string,
CITY string,
STATE string,
POSTALCODE string,
COUNTRY string,
TERRITORY string,
CONTACTLASTNAME string,
CONTACTFIRSTNAME string,
DEALSIZE string
)
stored as orc;


 STEP - 6 (Load data from "sales_order_csv" into "sales_order_orc")


from sales_order_csv insert overwrite table sales_order_orc select *;

set hive.cli.print.header = true;




 ###############Perform below menioned queries on "sales_order_orc" table########################



 a. Calculatye total sales per year


select YEAR_ID as Year,SUM(SALES) as total_sales_per_year from sales_order_orc group by YEAR_ID;


 b. Find a product for which maximum orders were placed


select SUM(QUANTITYORDERED) as Total_Qantity,PRODUCTLINE as Max_order_Product from sales_order_orc group by PRODUCTLINE order by Total_Qantity desc limit 1;





 c. Calculate the total sales for each quarter




select sum(SALES) as total_sales_each_quarter,QTR_ID as Quarter from sales_order_orc group by QTR_ID;

 d. In which quarter sales was minimum

select sum(SALES) as total_sales,QTR_ID as Quarter from sales_order_orc group by QTR_ID order by total_sales limit 1;







 e. In which country sales was maximum and in which country sales was minimum



select sum(SALES) as Total_Sales,COUNTRY from sales_order_orc group by COUNTRY order by Total_Sales limit 1
UNION ALL
select sum(SALES) as Total_Sales,COUNTRY from sales_order_orc group by COUNTRY order by Total_Sales desc limit 1;


 f. Calculate quartelry sales for each city

select city,quarter,sum(sales) as total_sales
from 
( select city, case
      when MONTH_ID >3 and MONTH_ID < 7 then "Q2"
      when month_id >6 and month_id < 10 then 'Q3'
      when month_id >9 and month_id <13 then 'Q4'
      else 'Q1' 
      end as quarter,
      sales
  from sales_order_orc
) t1 
group by city,quarter
order by city,quarter;



 h. Find a month for each year in which maximum number of quantities were sold Footer



select year_id,
       month_id, 
       total_sales
 
from
(   select  year_id,
            month_id,
            total_sales,dense_rank() over (partition by year_id order by total_sales desc) as ranks 
    from (  select  YEAR_ID,
                    month_id,
                    sum(sales) as total_sales 
            from sales_order_orc 
            group by YEAR_ID,
                  month_id
          ) tbl1 
) tbl2
where ranks = 1;




For Output - Go to Image Forlder
For more Reference - hive_assignment_commands.txt
