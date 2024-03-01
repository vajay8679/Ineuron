#Arithmetic operator - + , - , / , *, ** , % , //  ------> preceding from left to right   * , / , + , -

bigdata_fee = 200
azure_fee = 300
bigdata_enrollment = 20
azure_enrollment = 30

total_revenue = ( bigdata_fee * bigdata_enrollment + azure_fee * azure_enrollment )
# print(f"Total Revenue is : {total_revenue} ")

avg_revenue = ( bigdata_fee * bigdata_enrollment + azure_fee * azure_enrollment ) / (bigdata_enrollment + azure_enrollment)

bigdata_fee = bigdata_fee + 50
bigdata_fee +=  50
bigdata_fee *=  2

# print(bigdata_fee)
#
#
# print(f"Avg Revenue is : {avg_revenue} ")
#
# print(5 + 4 * 9)

# print( (5 + 4) * 9)
#
# print(15 / 4 )
# print(15 // 4 )
# print(15 % 4 )
#
# print(2 ** 3 )

# print(2 ** 3 ** 2) # right side binding for this

import math

# total_sales = 20000.60
total_sales = -20000.60

# print(math.ceil(total_sales))
# print(math.floor(total_sales))
# print(math.fabs(total_sales))


#Conditional Statements

# marks = int(input("Enter the marks : "))
# marks = int(marks)

#1.
# if marks >= 35:
#     if marks > 80:
#         print("Grade A")
#     else:
#         print("you Passed but cant acheive A grade")
# else:
#     print("Fail")

#2.
# if marks > 80:
#     print("Grade A")
# if marks >= 35:
#     print("You passed but cant achieve Grade A")
# else:
#     print("Fail")

# #3.
# if marks > 80:
#     print("Grade A")
# elif marks >= 35:
#     print("You passed but cant achieve Grade A")
# else:
#     print("Fail")


#Logical Operator - and , or
#comparision operator - == , < , > , !=, >= , <=

# age = int(input("Enter your age here : "))
# criminal_record = input("Do you have criminal reocrd wirte yes/no : ")
#
# if age >= 18 and criminal_record == "no":
#     print("Eligible to vote")
# else:
#     print("You are not able to vote")


#membership operator

# name = "Ajay Verma"
# print("ajay" not in name)


#What is string - A secquence of character - ' ' , " ", """ """

# name = 'Sumit\'s" training is really good'
# print(name)

# if we did not specify in varible then string is comment
"""
this is comment
"""

# name = """Sumit classes is really good and
#              he is offering big data course
#         """

# name = """Sumit classes is really good and \n he is offering big data course
#         """

# name = """Sumit classes is really good and \t he is offering big data course
#         """
# print(name)


#String related operations

#concatenation

# fname = input("Enter first name : ")
# lname = input("Enter last name : ")
# print(fname + " " + lname)

# name = "Ajay verma"
# print(len(name))

#indexing - help to get a particular character - index start from 0
#slicing - helps to get a slice
#string is immutable you cannot make modifications to the dtring
order_status = "order complete"

# print(order_status[2])
# print(order_status[-1])

# order_status[5] = "_" #error immutable
# print(order_status[0:4]) #5 excluded
# print(order_status[6:14])

length = len(order_status)

# print(order_status[6:length])
print(order_status[6:])
print(order_status[:8])
print(order_status[:])

#print last 5 character
print(order_status[-5:])
print(order_status[-5:len(order_status)])

#print everything after space
index = order_status.find(" ")
print(order_status[index+1:])

#print the first word
# print(order_status[0:index])

# print(order_status[-5:-1])
# print(order_status[1:9:2])

#revers the string
# print(order_status[::-1])

print(order_status.find("s")) #if finds then first occurence and if not find then -1 if we use index it will give error
# print(order_status.index("s")) #error

print(order_status.endswith("complete"))
print(order_status.capitalize())

order_status1 = "        Order complete   "
print(order_status1.strip())
print(order_status1.lstrip())
print(order_status1.rstrip())

print(order_status.replace("complete","completed"))


# basic data types - int, float, bool, None, string
#sequence - List, tuple, string, range - sequence matter
#sequence is not important - set, dictionary

order_df = "1,2013-03-12 00:00:00,1124,  CLOSED  "

new_df = order_df.split(",")
print(new_df)
print(new_df[3])
print(new_df[3].strip())
print(new_df[3].lower().strip())
print(new_df[3].upper().strip())