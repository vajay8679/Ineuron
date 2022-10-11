#Python program for Lists

# arr_list1 = []
# arr_list2 = [1,2,3,4,5,6]
# arr_list3= [1,2,"Hi",4,5,"Hello"]


# print(arr_list1)
# print(arr_list2)
# print(arr_list3)



#How to add values in lists dynamically?
#We will use append() method to insert element

#arr_list1 = []

# for i in range(7):
#     arr_list1.append(i)

# len_arr = len(arr_list1)
# print(arr_list1)

# print("length of array :",len_arr)


# arr4 = [2,3,4,5,6]
# arr5 = [10,1,3,4,55,34,42,24]


# arr7 = [2,3,4,5,6]
# arr6 = [10,1,3,4,55,34,42,24]

# result = arr4 + arr5
# print(result)



#What is the difference between append() and extend()

# arr4.append(arr5)

# arr7.extend(arr6)

# print("append result : ",arr4)
# print("extend result : ",arr7)

# print("Length of append result : ",len(arr4))
# print("Length of extend result : ",len(arr7))


arr_list8 = [10,20,30,40,50,60,70,80]

#Iterate element w/o indexing

for i in arr_list8:
    print(i)


#Iterate element with indexing


for j in range(0,len(arr_list8)):
    print("indexing ",j, " and value is : ",arr_list8[j])

