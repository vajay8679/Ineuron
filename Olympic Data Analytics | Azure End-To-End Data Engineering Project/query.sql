--count the number of athelete from each country
select Country, count(*) as Total_athelete from athletes
GROUP BY Country ORDER BY Total_athelete DESC;

--calculate the total medal won by each country
select Team_Country,SUM(Gold) as Total_Gold,SUM(Silver) as Total_silver,
SUM(Bronze) as Total_silver from medals GROUP by Team_Country ORDER BY Total_Gold DESC;

--calculate the average number of enteries by gender for each disipline:
SELECT Discipline,  AVG(Female) as avg_Female,AVG(Male) as avg_Male
from entriesgender where Discipline= 'Archery' GROUP by Discipline;