Movie Analytics Project:

The main goal of the project is to Analyze the data from various data sources and extract meaningful insights from the data and to know the audience interests.the data will be present in the hdfs storage layer in csv format with delimiter(::).We will be reading data from Hdfs layer and process the data using pyspark.

Tech stack used :
1.HDFS(Hadoop File System)
2.Spark

Architecture:
![image](https://user-images.githubusercontent.com/64748921/223407219-56726e51-0308-48f3-8a7d-df62253ab9e3.png)


Detailed  Explanation:
For this project there are 3 data sources named as ratings.csv,users.csv,movies.csv.
In the ratings.csv there are 4 columns userid , movieid , rating, timestamp. The userid gives the detail about the user,the movieid gives the information of the movie to which user gave rating. The rating will be in between 1 to 5. 
In the users.csv we have 4 columns userid,gender,occupation,zip-code.The userid gives information about the user.the gender gives information regarding the gender of the user and the occupation gives the info regarding occupation of the user and zipcode gives the information about the zipcode of the user.
In the movies.csv we have 3 columns. we have information regarding movieid,title genre.the moviid gives the id of the movie,the title represents the title for the movieand genre gives the information regarding to which genre it belongs to  this columnis again delimted by ‘|’.it has various values in that column like action, Thriller etc.

Our data is picked from the hdfs layer and read by the spark engine. After reading the data We can perform various analytical queries on the data and extract useful business insights like top 10 viewed movies,distinct list of genres,to which genre audience are giving more ratings etc.So that the movie industry can analyze the trends and can know the audience interests. 
Storage:
Finally we can store the data as table in hive meatstore if required we can also create real time dashboards by using some dashboarding tools.

To run this project :
First we have to keep our files in the hdfs using the command
hdfs dfs -put users.csv /
hdfs dfs -put movies.csv /
hdfs dfs -put ratings.csv /

After the files are placed in the hdfs we can run the script python main.py 


