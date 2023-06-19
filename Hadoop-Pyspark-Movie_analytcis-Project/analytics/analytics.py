#necessary libraries of pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from os.path import abspath
import logging
from conn import connections
from pyspark.sql.functions import split, col
from pyspark.sql.functions import *
from conn import connections



def distinct_genres():
     movies=connections.movies_connect()
     logging.info("Read data from movies dataframe and finding the distinct list of  genres")
     movies_cast=movies.select(explode(split(col("genre"),'\\|')).alias("Genres"))
     movies_cast.select('Genres').distinct().show(30,False)

def genre_count():
     movies=connections.movies_connect()
     logging.info("Read data from movies dataframe and finding the count of movies for each genre")
     movies_cast=movies.select(col('movieid'),col('title'),explode(split(col("genre"),'\\|')).alias("Genres"))
     genre_count=movies_cast.groupby('Genres').agg(count('*').alias("genre_count")).show(30,False)

def top_viewed():
     ratings=connections.ratings_connect()
     movies=connections.movies_connect()
     logging.info("Read data from movies and ratings  dataframe and finding the top 10 most viewed movies")
     new=ratings.join(movies,ratings.movieid1 == movies.movieid,"inner")
     top_view=new.groupby("movieid",'title').agg(count("*").alias("top_viewed_movies")).sort(desc("top_viewed_movies")).show(10,False)
    
def title_with_alphaornum():
     movies=connections.movies_connect()
     logging.info("Read data from movies dataframe and finding the titles that are starting with numbers or alphabets")
     title_count=movies.filter(col('title').rlike("[0-9a-zA-Z]*$")).count()
     print(title_count)

def latest_movies():
     movies=connections.movies_connect()
     logging.info("Read data from movies dataframe and finding the movies that were released recently")
     extract_year= movies.withColumn("year", regexp_extract(col("title"), r"\(([^()]+)\)$", 1));
     extract_year.createOrReplaceTempView("extract_year")
     latest_release=extract_year.sort(col("year").desc())
     latest_release.show(10,True)
     return extract_year
     
     
     



