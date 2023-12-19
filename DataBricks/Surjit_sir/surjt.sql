--seek - quickly able to search
--scan - search row by row

--clustered - records will be physically ordered in the actual table

--non clustered index - except clustered index we search on ther keys then we create seperate structure for it , requred extra space and assign address of it , we can have multiple non clustered index but only one clustered index in a table and 

seek - select order_id,customer_id from orders where order_id = 5; search by binary - much faster
scan - select order_id,customer_id from orders where customer_id = 5; search row by row

