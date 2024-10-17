

# Задание 2. Преобразование числа в шестнадцатеричное
# представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

# BIN = 2
# OCT = 8
# HEX = 16
#
# number: int = int(input("enter number: "))
# print(oct(number))
# res: str= ''
# test_num: int = number
# while number:
#     cur_num = number % OCT
#     res = str(cur_num) + res
#     number //= OCT
# print(f"Ox{res}")


number = int(input("enter an integer: "))
print(hex(number))
base = 16
letters = "0123456789ABCDEF"
new = ''
while number > 0:
    reminder = number % base
    new = str(reminder) + new
    num = number // base
    if reminder > 9:
        letter_id = reminder - 10
        reminder = letters[letter_id]

    break
print(new)



