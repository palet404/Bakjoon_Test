FirstNum = input()
SecondNum = input()

FirstNum = int(FirstNum)

if len(FirstNum) and len(SecondNum) == 3 and FirstNum and int(SecondNum) > 0:

    print(FirstNum * int(SecondNum[2]))
    print(FirstNum * int(SecondNum[1]))
    print(FirstNum * int(SecondNum[0]))
    print(FirstNum * SecondNum)

else :
    print("Given two numbers are not natural number or aren't 3digit")