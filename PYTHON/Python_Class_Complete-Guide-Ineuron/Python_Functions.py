# Python program for functions

def print_func():
	print("Hello ! This is my first python function ..")


print_func()


def power_func(num,exp):

	result = num**exp
	return result



n = 3
e = 4
output = power_func(n,e)
print("Output of Power Function : ",output)


def math_ops(num1,num2):

	addition = num1 + num2
	subs = num1 - num2
	mul = num1 * num2
	div = num1/num2

	return addition,subs,mul,div


n1 = 7
n2 = 3

add,subs,mul,div = math_ops(n1,n2)

print(" Addition of ",n1," , ",n2," = ",add)
print(" Substraction of ",n1," , ",n2," = ",subs)
print(" Multiplication of ",n1," , ",n2," = ",mul)
print(" Division of ",n1," , ",n2," = ",div)



# implement power function with key value inputs
# kwargs = {'num' : 3, 'exp' : 4}

def power_func(**kwargs):
	result = kwargs['num'] ** kwargs['exp']
	return result





# n = 3
# e = 4
output1 = power_func(num=3,exp=4)
output2 = power_func(exp=4,num=3)
print("Output1 of Power Function : ",output1)
print("Output2 of Power Function : ",output2)






















