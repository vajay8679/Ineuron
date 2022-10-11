#Program for map(),reduce(),filter()

# arr_list = [2,3,5,8]

# arr_five_lambda = lambda x:x+5

# square_lambda = lambda x:x*x

# res1 = list(map(arr_five_lambda,arr_list))
# res2 = list(map(square_lambda,arr_list))

# print("Result add ,",res1)

# print("Result square ,",res2)


#add individual elements of two given lists

# arr_list1 = [2,3,5,8]
# arr_list2 = [6,9,10,20]

# sum_lists = lambda x,y : x+y

# sum_lists_result = list(map(sum_lists,arr_list1,arr_list2))

# print("Resultsss",sum_lists_result)


# from functools import reduce

# arr_list3 = [2,3,5,8]
# sum_ele = lambda x,y : x+y

# arr_reduce = reduce(sum_ele,arr_list3)

# print("Reduction data : ",arr_reduce)


seq_num = [0,1,2,3,5,8,13]

#filter even number

filter_logic = lambda x : x%2==0
even_num = filter(filter_logic,seq_num)

print("Even number filtered : ",list(even_num))