# Write a program returns four basic operation
# After receiving the two integers A and B.
# Condition : A >= 1 , B <= 10^4

A, B = map(int, input().split())

if A >= 1 and B <= 10^4 :
    print(A+B)
    print(A-B)
    print(A*B)
    print(int(A/B))
    print(A%B)

else :
    print("A and B should integer, \n A is more than 0, B is not more than 10^4")

# A//B round down number ex) -1/2 => -0.5 => -1
# int(A/B) drop the decimal point -1/2 => -0.5 => 0