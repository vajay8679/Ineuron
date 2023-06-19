#necessary libraries of pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from os.path import abspath
import logging
from conn import connections
from analytics import analytics
from pyspark.sql.types import StructType,StructField, StringType, IntegerType




warehouse_location = abspath('spark-warehouse')


spark = SparkSession.builder.master("spark://localhost:7077").appName("demo").config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport().getOrCreate()

def old_movies():
    movies=analytics.latest_movies()
    movies.createOrReplaceTempView('movies')
    movies.show(10,True)
    logging.info("Finding the list of old movies")
    spark.sql("select * from movies order by year").show(10,True)

def movies_released_each_year():
    data_with_year=analytics.latest_movies()
    data_with_year.createOrReplaceTempView('data_with_year')
    logging.info("Finding the count of movies released each year")
    spark.sql("select year,count(year) from data_with_year group by year ").show()

def movie_count_by_rating():
    count_each_year=connections.ratings_connect()
    count_each_year.createOrReplaceTempView("count_each_year")
    logging.info("To find the count of number of movies  for each rating")
    spark.sql("select rating,count(movieid1) as movies_count_by_rating from count_each_year group by rating").show()

def users_rated_for_each_movie():
    user_rating_count=connections.ratings_connect()
    user_rating_count.createOrReplaceTempView("user_rating_count")
    logging.info("To find the count of number of users who gave rating for each movie")
    spark.sql("select movieid1,count(userid) as number_of_users from user_rating_count group by movieid1 ").show()

def avg_rating_for_movie():
    avg_rating=connections.ratings_connect()
    avg_rating.createOrReplaceTempView("avg_rating")
    logging.info("To find the average rating for each movie")
    spark.sql("select movieid1,avg(rating) as avg_rating from avg_rating group by movieid1").show()




if __name__ == '__main__':
     connections.movies_connect()
     connections.ratings_connect()
     connections.users_connect()
     analytics.distinct_genres()
     analytics.genre_count()
     analytics.top_viewed()
     analytics.title_with_alphaornum()
     analytics.latest_movies()
     old_movies()
     movies_released_each_year()
     movie_count_by_rating()
     users_rated_for_each_movie()
     avg_rating_for_movie()
    


     

   
    
