#Python for Strings

tmp_str = "Ineuron Python classes"

print("Input Str ",tmp_str)
print("Input Str ",tmp_str.upper())

print("Length of input Str ",len(tmp_str))

#Iterate element w/o indexing

for i in tmp_str:
    print(i)


#Iterate element with indexing


for j in range(0,len(tmp_str)):
    print("indexing ",j, " and value is : ",tmp_str[j])

