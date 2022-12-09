#Python if-else with logical operator

# a = 10
# b = 6

# if a < b:
#     print("True Condition  - a is less than b!!")
# else:
#     print("False Condition  - a is not less than b!!")


name = input("Enter your name (Must be string) :",)
age = input("Enter your age (Must be integer !!) :",)
age = int(age)
if age >= 18 and name == "Ajay":
    print("Completely Matched !!")
else:
    print("Not Matched !!")