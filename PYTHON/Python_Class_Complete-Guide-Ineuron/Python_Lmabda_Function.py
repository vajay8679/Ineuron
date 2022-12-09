# Program for Lambda Function

add_lambda_exm = lambda x,y : x+y

square_lambda_exm = lambda x : x * x


num1 = 2
num2 = 3

add_result = add_lambda_exm(num1,num2)

square_result = square_lambda_exm(num2)

print("Sum of ",num1," and ",num2," is = ",add_result)
print("Square of ",num2," is = ",square_result)