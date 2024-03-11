from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("left_anti_join_example").getOrCreate()

# Create DataFrames for Users and Purchases
data_users = [(1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "David")]
data_purchases = [(1, "Book"), (2, "Pen"), (5, "Notebook")]

columns_users = ["id", "name"]
columns_purchases = ["user_id", "item"]

df_users = spark.createDataFrame(data_users, columns_users)
df_purchases = spark.createDataFrame(data_purchases, columns_purchases)

# Perform Left Anti Join
df_non_purchasers = df_users.join(df_purchases, df_users.id == df_purchases.user_id, "left_anti")

# Show the result
df_non_purchasers.show()


# SELECT
#     *
# FROM
#     users u
# LEFT ANTI JOIN
#     purchases p ON u.id = p.user_id;



Table A (Users):

id	name
1	Alice
2	Bob
3	Charlie
4	David
null	Eve
Table B (Purchases):

user_id	item
1	Book
2	Pen
5	Notebook
null	Pencil


id	name
3	Charlie
4	David
null	Eve


Handling Null Values In Left Anto Join
As you've seen in the example, even though there's a null in the purchases table, nulls do not match with other nulls in standard join operations. Therefore, Eve is also listed as not having made a purchase.