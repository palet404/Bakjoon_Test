## Compare two integer Number

# Write program compare two integer number A and B
# Condition : Receving A and B at firstline, seprator is space
# first line prints one of the 3 results >,<,==
# If A is bigger than B prints ">" and if smaller than prints "<" if same prints "=="
# limtis : -10^4 <= A, B <= 10^4

A, B = map(int, input().split())

if -10**4<= (A and B) <= 10**4:
    if A > B :
        print(">")
    elif A < B :
        print("<")
    elif A == B :
        print("==")
    else :
        pass
else :
    print("A and B muste be integer number between -10^4 and 10^4")