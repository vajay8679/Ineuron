# Python program for try & except

a = 10

# Normal exception capturing
try:
	result = a/0
except:
	print("Some error occured !!")


# # Capture all exceptions
try:
	print("Before divsion")
	result = a/0
	print("After divsion")
except Exception as err:
	print("Failed Execution - ",str(err))


# # Capture sepecific exception
try:
	print("Before divsion")
	result = a/0
	print("After divsion")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))


arr_list = [1,2,3,4,5]

try:
	print("10th Element - ",arr_list[9])
except Exception as err:
	print("Failed Execution - ",str(err))


name = input("Enter your name : ")
age = int(input("Enter your age : "))


try:
	if (age<18):
		raise Exception("Can not register for this application, Age must be greater than 18 !!")
	print("Valid User !!")
except Exception as err:
	print("Failed Execution - ",str(err))



# multiple exceptions
a = 0
inp_dict = {'Shashank' : 10, 'Rahul' : 15}
arr_list = [1,2,5,8]

try:
	print("Before Core Logic")
	result = a/0
	get_amit = inp_dict['Amit']
	tenth_element = arr_list[9]
	print("After Core Logic")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))
except KeyError as err:
	print("Failed Execution - ",str(err))
except IndexError as err:
	print("Failed Execution - ",str(err))



# use of else block
a = 10
inp_dict = {'Shashank' : 10, 'Rahul' : 15, 'Amit' : 20}
arr_list = [1,2,5,8]

try:
	print("Before Core Logic")
	result = a/10
	get_amit = inp_dict['Amit']
	tenth_element = arr_list[2]
	print("After Core Logic")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))
except KeyError as err:
	print("Failed Execution - ",str(err))
except IndexError as err:
	print("Failed Execution - ",str(err))
else:
	print("If there is no exception the this code block will be executed")


# use of finally block
a = 10
inp_dict = {'Shashank' : 10, 'Rahul' : 15, 'Amit' : 20}
arr_list = [1,2,5,8]

try:
	print("Before Core Logic")
	result = a/10
	get_amit = inp_dict['Amit']
	tenth_element = arr_list[9]
	print("After Core Logic")
except ZeroDivisionError as err:
	print("Failed Execution - ",str(err))
except KeyError as err:
	print("Failed Execution - ",str(err))
except IndexError as err:
	print("Failed Execution - ",str(err))
else:
	print("If there is no exception the this code block will be executed")
finally:
	print("This block will always execute doesn't matter exception occured or not")










