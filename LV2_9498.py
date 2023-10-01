## Test Grade
# Write program prints grade recevied test score 
# Grade follows table below
# Grade | Score
#   A   | 90 ~ 100
#   B   | 80 ~ 89
#   C   | 70 ~ 79
#   D   | 60 ~ 69
#   F   | ~ 59
# Condtion test score is given at first line it is integer number between 0 and 100

TestScore = int(input())
if 0 <= TestScore <= 100:
    if 90 <= TestScore <= 100 :
        print("A")
    elif 80<= TestScore <= 89 :
        print("B")
    elif 70<= TestScore <=79 :
        print("C")
    elif 60<= TestScore <=69 :
        print("D")
    elif TestScore <= 59 :
        print("F")
    else :
        pass

else :
    print("TestScore should be integer number and it is between 0 and 100")
