#Python program for try & except

a = 10

#Normal exceptions capturing

# try:
#     result = a/0

# except:
#     print("Some error occur !!")


# Capture all exceptions

# try:
#     print("Before Division")
#     result = a/0
#     print("After Division")

# except  Exception as err:
#     print("Some error occur !!",str(err))



#Capture specific exceptions

# try:
#     print("Before Division")
#     result = a/0
#     print("After Division")

# except  ZeroDivisionError as err:
#     print("Some error occur !!",str(err))



# arr_list = [1,2,3,4,5]

# try:
#     print("10th Element :- ",arr_list[9])
# except Exception as err:
#     print("error Failed ",str(err))



name = input("Enter your name :")
age = int(input("Enter your age :"))

try:
    if (age<18):
        raise Exception("Can not register for this application ")
    print("Valid User")
except Exception as err:
    print("Failed Execution - ",str(err))