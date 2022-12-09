# Python program for Dictionary

dict_exp = { "Shashank" : 28, "Rahul" : 27, "Amit" : 26}
print("Dictionary Output : ",dict_exp)
print("Dictionary Length : ",len(dict_exp))


dict_exp = {}
dict_exp["Shashank"] = 28
dict_exp["Rahul"] = 27
dict_exp["Amit"] = 26

print("Dictionary Output : ",dict_exp)

#changes for a value
dict_exp["Shashank"] = 25
print("Dictionary Output : ",dict_exp)


for key,val in dict_exp.items():
	print("Key is ",key," and Value is ",val)


# how to get all keys?
# how to get all values from dictionary?

print("Total Keys : ",dict_exp.keys())
print("Total Values : ",dict_exp.values())


print(dict_exp["Shashank"])