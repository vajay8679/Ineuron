#Python program for functions

# def print_fun():
#     print("Hi Ajay")

# print_fun()


# def power_fun(num,exp):
#     num1 = num**exp
#     #print(num1)
#     return num1

# n = 3
# e = 4
# result = power_fun(n,e)
# print("Output of power function : ",result)



# def math_ops(num1,num2):
#     addition = num1+num2
#     subs = num1-num2
#     mul = num1*num2
#     div = num1/num2

#     return addition,subs,mul,div

# a = 4
# b = 2

# add,subs,mul,div = math_ops(a,b)
# print("Addition : ",add)
# print("Subtraction : ",subs)
# print("Multiplication : ",mul)
# print("Division : ",div)



#Impliment power function with key value inputs

#kwargs = {'num' : 3, 'exp : 4} 

def power_fun(**kwargs):
    result = kwargs["num"] ** kwargs["exp"]
    return result

output1 = power_fun(num=3,exp=4)
output2 = power_fun(exp=4,num=3) 

print("Output1 : " ,output1)
print("Output2 : " ,output2)