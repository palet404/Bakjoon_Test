# Write a program that outputs A+B 
# After receiving the two integers A and B.
# Condition : 

A, B = map(int,input().split())

if A > 0 and B < 10:
    print(A+B)
else :
    print("A, B should be integer and A should bigger than0, B smaller than 10")

# A = input()
# B = input()
# -> "Receiving the two integers A and B" means
# Program should receive two data(integers) at the same time(one line), 
# Not receive it separately 
##########################################################################
# A, B = int(input()).split()
# -> split() is for str
# -> int() can't conver str has space or other character
##########################################################################
# A, B = int(input().split())
# -> int() is for ele not for list
###########################################################################
# A, B = map(int(),input().split())
#     ^^^^
# TypeError: 'int' object is not callable
# () is not needed for map funtion

###########################################################################
# Model answer
# Didn't follow problems conditon
# Map(func, iterable)
# Make an iterator that computes the function using arguments from each of the iterables. 
# Stops when the shortest iterable is exhausted.