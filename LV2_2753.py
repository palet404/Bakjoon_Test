## Yun-year
# Write program figure out given year is Yun-year.
# Yun-year is year 4 and 400 multiple or not 100 multiple
# ex) 2012 is  Yun-year because 4 multiple and not 100 multiple
#     1900 is not Yun-year because 4 multiple but 100 mulitple
#     2000 is Yun-year because 4multiple and 400 multiple

# Condition : Year is given at first line, and natural number between 1 and 4000

YunYear = int(input())
if 1 <= YunYear <= 4000:
    Remain_div4 = YunYear%4
    Remain_div100 = YunYear%100
    Remain_div400 = YunYear%400
    if Remain_div4 ==0 and Remain_div400 == 0:
        print(1)
    elif Remain_div4 ==0 and Remain_div100 != 0:
        print(1)
    else :
        print(0)
else:
    print("Given year is not natural number or not between 1 and 4000")
