# Program for map(), reduce(), filter()


arr_list = [2,3,5,8]

add_five_lambda = lambda x : x + 5
square_lambda = lambda x : x * x

result_add_five = list(map(add_five_lambda, arr_list))
result_square = list(map(square_lambda, arr_list))

print("Result for Add Five Map : ",result_add_five)
print("Result for Square Map : ",result_square)


# add individual elements of two given lists

arr_list1 = [2,3,5,8]
arr_list2 = [6,8,10,20] 

# sum_list = [8, 11, 15, 28]

sum_list_lambda = lambda x,y : x+y

sum_list_result = list(map(sum_list_lambda, arr_list1, arr_list2))
print("Sum List Result : ",sum_list_result)

from functools import reduce


arr_list3 = [2,3,5,8]
sum_ele = lambda x,y : x+y

result_reduce = reduce(sum_ele,arr_list3)

print("Result of Reduce : ", result_reduce)


seq_num = [0, 1, 2, 3, 5, 8, 13]

# filter even numbers

filter_logic = lambda x : x%2 == 0

even_num_list = filter(filter_logic, seq_num)
print("Filter even number result : ",list(even_num_list))



