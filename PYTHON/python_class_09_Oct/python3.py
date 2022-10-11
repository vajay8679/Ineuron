#Python Program for Dictionary

# dict_exp = {"Ajay" : 28,"Ravi" : 25 ,"Sumit" : 24}
# print("Dict output ",dict_exp)

# print("Dict length ",len(dict_exp))


dict_exp = {}
dict_exp["Ajay"] = 28
dict_exp["Amit"] = 25
dict_exp["Sumit"] = 23

# print("Dict Output ",dict_exp)

# dict_exp["Ajay"] = 35

# print("Dict Output1 ",dict_exp)


for key,val in dict_exp.items():
    print("Key is : ",key, " and  value is :",val)


#how to get all keys?
#how to get all values from dictionary

print("Total Keys :",dict_exp.keys())
print("Total Keys :",dict_exp.values())


print(dict_exp["Ajay"])