#Program for List Comprehension

arr_list = [2,3,4,512,11,13,14,11]

#create another list which holds only even values
# arr_even = []
# for i in arr_list:
#     if i%2 ==0:
#         arr_even.append(i)

# print("Eeven Numbers : ",arr_even)

# even_list = [i for i in arr_list if i%2==0]
# print(even_list)

#create another list which will have even values before odd values

result = [num for num in arr_list if num%2==0] + [num for num in arr_list if num%2 != 0]
print("Even - Odd element List :",result)