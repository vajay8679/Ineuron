# Python Nested If-Else with logical operators


marks = input("Enter student's final marks (Must be a integer) : ")
marks = int(marks)

if marks>=90:
	print("A+ Grade !!")
elif marks<90 and marks>=80:
	print("A Grade !!")
elif marks<80 and marks>=75:
	print("B+ Grade !!")
elif marks<75 and marks>=70:
	print("B Grade !!")
else:
	print("C Grade !!")