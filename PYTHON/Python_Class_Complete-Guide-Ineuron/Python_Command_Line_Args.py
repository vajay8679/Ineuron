# Python command line arguments

import sys

# len() is an inbuilt function of Python which can be used
# to find the length of any iterable data type

n = len(sys.argv)

command_line_args = sys.argv

print("Total number of command line arguments : ", n)
print("What sre the input command line arguments ? ", command_line_args)

print("First Command Line Argument : ", sys.argv[0])
print("Second Command Line Argument : ", sys.argv[1])
print("Third Command Line Argument : ", sys.argv[2])
print("Fourth Command Line Argument : ", sys.argv[3])

