# Python program for Lists


arr_list2 = [1,2,3,4,7]
arr_list3 = [1,2,"Hi",98.22,"Hello",[3,10,65]]

print(arr_list2)
print(arr_list3)


arr_list1 = []

# How to add values in lists dynamically?
# we will use append() method to insert elements

for i in range(1,11):
	arr_list1.append(i)

print(arr_list1)
list_len = len(arr_list1)
print("Length of the list : ",list_len)


arr_list4 = [4,58,90,20]
arr_list5 = [100,70,240,54,80]

arr_list6 = [4,58,90,20]
arr_list7 = [100,70,240,54,80]

result = arr_list4 + arr_list5
print(result)


#what is the difference between append() and extend()
arr_list4.append(arr_list5)

arr_list6.extend(arr_list7)
print("Append Output : ",arr_list4)
print("Extend Output : ",arr_list6)
print("Append Output Length: ",len(arr_list4))
print("Extend Output Length: ",len(arr_list6))


arr_list8 = [100,70,240,54,80]

# Iterate elements without index

for num in arr_list8:
	print(num)


# Iterate elements with index

for idx in range(0,len(arr_list8)):
	print("Element at ",idx," index is : ",arr_list8[idx])



