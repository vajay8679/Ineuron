#Python command line arguments

import sys

n = len(sys.argv)
comand_line_args = sys.argv

print("Number of lines",n)
print("What are the input command line arguments?",comand_line_args)

print("First Command line argument :",sys.argv[0])
print("Second Command line argument :",sys.argv[1])