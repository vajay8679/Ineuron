#Python Program for Set

#create empty set

set_var = set()
set_var.add(4)
set_var.add(5)
set_var.add(7)
set_var.add(10)
set_var.add(10)
set_var.add(8)
set_var.add(10)
set_var.add(14)

print(set_var)
print("length of set : ",len(set_var))


set_list = list(set_var)
print("Type casting: ",set_list)

#Iteration with index

for i in range(0,len(set_var)):
    print("Index : ",i," value : ",set_var[i])

