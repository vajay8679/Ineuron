# Program for List Comprehension

arr_list = [3,6,7,4,1,2,15,10,12,11]

# Create another list which will have only even values
even_element_list = []

for num in arr_list:
	if num%2 == 0:
		even_element_list.append(num)

print("Even Elements List : ",even_element_list)

even_element_list = [ num for num in arr_list if num%2 == 0 ]
print("Even Elements List : ",even_element_list)



# Create another list which will have even values before odd values
result = [ num for num in arr_list if num%2 == 0 ] + [ num for num in arr_list if num%2 != 0 ]
print("Even-Odd Elements List : ",result)