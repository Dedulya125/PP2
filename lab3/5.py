# A Python program to print all 
# permutations using library function 
from itertools import permutations 


# Get all permutations of [1, 2, 3]

f = input()
perm = permutations(f) 

# Print the obtained permutations 
for i in list(perm):
	print("", end=", ")
	for j in i:
	    print (j, end="")