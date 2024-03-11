from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("left_semi_join_example").getOrCreate()

# Create DataFrames for Users and Purchases
data_users = [(1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "David")]
data_purchases = [(1, "Book"), (2, "Pen"), (5, "Notebook")]

columns_users = ["id", "name"]
columns_purchases = ["user_id", "item"]

df_users = spark.createDataFrame(data_users, columns_users)
df_purchases = spark.createDataFrame(data_purchases, columns_purchases)

# Perform Left Semi Join
df_purchasers = df_users.join(df_purchases, df_users.id == df_purchases.user_id, "left_semi")

# Show the result
df_purchasers.show()


# SELECT
#     *
# FROM
#     users u
# LEFT SEMI JOIN
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


+---+-----+
| id| name|
+---+-----+
|  1|Alice|
|  2| Bob |
+---+-----+


Handling Null Values In Left Semi Join
As you've seen in the example, you cannot match null values with other null values. Therefore, rows with null values as the join key are excluded from the result.

Pros And Cons
Pros:

Performance: Generally faster than other joins as it only needs to check for the existence of keys without needing to shuffle and join all corresponding data.
Simplicity: The result is straightforward, containing only rows from the left DataFrame that have matches in the right DataFrame.
Cons:

Less Intuitive: The concept might be less intuitive for those used to SQL joins, as it doesn't return a combined result set.