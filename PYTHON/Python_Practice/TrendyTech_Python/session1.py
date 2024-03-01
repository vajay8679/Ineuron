# IDE (VS Code, Sublime, Pycharm, Jupyter notebook, databricks community version, google colab, Terminal )

# https://colab.research.google.com/

# Python is interpreted language we have to write code line by line

print("Hello Data Enigneering")


# - single line comment
"""
Multi line comment 
"""

# Variables in Python

course_fee = 800
course_fee = 850

print(course_fee)


# there are five main simple data types in python - string , int, float, bool , None

instructor_name = "Sumit Mittal"
course_fee = 800
course_ration = 8.7
is_starting_soon = True
total_income = None

print(type(instructor_name))
print(type(course_fee))
print(type(course_ration))
print(type(is_starting_soon))
print(type(total_income))

print(course_fee + 50.5)
# print(instructor_name + 1) Error data types are different

course_fee = course_fee + (course_fee * .1)
print(course_fee)

# in python everything can be string


course_fee = "800"

# course_fee = course_fee + (course_fee * .1)  #error at runtime not at compile time

#Type Casting

course_fee = int(int(course_fee) + (int(course_fee) * .1))
print(course_fee)


#String Concat and Format

first_name = "Ajay"
last_name = "Kumar"

print(first_name + "  " + last_name)

print("MY first name is " + first_name + " and last name is " + last_name)

print("----------"*9)
print(f"MY first name is {first_name} and last name is {last_name}" )
print("----------"*9)


#Input field

salary = input("What is your current salry ")
hike = input("What is the hike percentage ")

new_salary = int(salary) + int(int(salary)*int(hike)/100)
print(f"The New Salary hiek is : {new_salary} ")