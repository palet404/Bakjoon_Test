A, B = map(int, input().split())

if A >= 1 and B <= 10^4 :
    print(A+B)
    print(A-B)
    print(A//B)
    print(A%B)

else :
    print("A and B should integer, \n A is more than 0, B is not more than 10^4")