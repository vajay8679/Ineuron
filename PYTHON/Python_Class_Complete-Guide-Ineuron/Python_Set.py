# Python program for Set


# create empty set
set_var = set()

set_var.add(2)
set_var.add(4)
set_var.add(2)
set_var.add(2)
set_var.add(5)
set_var.add(4)
set_var.add(3)
set_var.add(6)
set_var.add(3)

print("Content of Set : ",set_var)
print("Length of Set : ",len(set_var))

set_list = list(set_var)

print("Content of Set after List conversion: ",set_list)

# Iterate elements with index

for idx in range(0,len(set_list)):
	print("Element at ",idx," index is : ",set_list[idx])

