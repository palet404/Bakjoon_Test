A, B, C = map(int,input().split())

if 2<= A and B and C <= 10**4 :
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)
else :
    print("A,B,C should between 2 and 10,000")