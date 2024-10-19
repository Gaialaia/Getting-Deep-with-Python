
# Программа принимает целое число и возвращает его римское представление в
# виде строки.

digit = int(input("digit: "))

roman_digits = ['I', 'V', 'X',
                'L', 'C', 'D', 'M']



arabic_digits = [1, 2, 3, 4, 5, 10, 50, 100, 500, 1000]
#
# if digit <=5:
#     res = roman_digits [digit-1]
#     print(res)
#     if digit > 5 and digit < 10:
#         res = roman_digits[digit-1] + digit [digit-1]
#         print(res)

if digit <=3:
    res = roman_digits[0]*digit
    print(res)

elif digit == 4:
    res = roman_digits[0] + roman_digits[1]
    print(res)

elif digit == 5:
    res = roman_digits[1]
    print(res)
elif digit > 5 and digit <= 8:
    res = roman_digits[1] + ((roman_digits[0]) * (digit-5))
    print(res)

elif digit == 10:
    res = roman_digits[2]
    print(res)
elif digit == 9:
    res = roman_digits[0] + roman_digits[2]
    print(res)