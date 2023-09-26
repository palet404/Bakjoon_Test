# '''
# Write a program that outputs A+B 
# After receiving the two integers A and B.

# '''

ReceivedNumLst = input().split()
A, B = [int(i) for i in ReceivedNumLst]
Result = A+B
print(Result)

# A = input()
# B = input()
# -> "Receiving the two integers A and B" means
# Program should receive two data(integers) at the same time(one line), 
# Not receive it separately 

# A, B = int(input()).split()
# -> split() is for str
# -> int() can't conver str has space or other character

# A, B = int(input().split())
# -> int() is for ele not for list