#Python program for tuples

arr_tuple = (10,20,30,40,50)

print("Tuple output :" , arr_tuple)

#Iterate element w/o indexing

for i in arr_tuple:
    print(i)


#Iterate element with indexing

for i in range(0,len(arr_tuple)):
    print("Index : ",i," value : ",arr_tuple[i])

