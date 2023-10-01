A, B, C = map(int, input().split())

if 1 <= (A and B and C) <= 10**12 :
    print(A+B+C)
else :
    print("A, B, C must be in between 1 and 10^12")