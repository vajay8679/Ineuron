# Python Program Strings

tmp_str = "IneuronPythonClasses"

print("Input Str : ",tmp_str)
print("Length Of Input Str : ",len(tmp_str))

# # Iterate elements without index
print("Without Index Iteration")
for char in tmp_str:
	print(char)


# # Iterate elements with index
print("With Index Iteration")
for idx in range(0,len(tmp_str)):
	print("Character at ",idx," index is : ",tmp_str[idx])

print("Input Str in Upper Case : ",tmp_str.upper())
print("Input Str in Lower Case : ",tmp_str.lower())



