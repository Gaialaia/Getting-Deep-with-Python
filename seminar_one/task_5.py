
# Задача 5. Игра «Компьютер угадывает число»
# Мальчик загадывает число между 1 и 100 (включительно). Компьютер может
# спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
# трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
# Напишите программу, которая с помощью цепочки таких вопросов и ответов
# мальчика угадывает число.
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать
# число за семь попыток.



import random
from random import randrange

from seminar_one.task_4 import number

# from random import randrange
# start = 0
# stop = 100
# boys_number = 70
# n = randrange(start, stop)
# count = 0
#
# while n!= boys_number:
#     n = randrange(start, stop)
#     print(n)
#     r = input("1 - ">" or 2 - "<" ")
#     if r == 1:
#         stop = n
#     if r == 2:
#         start = n
#         count += 1
#     print(n, count)
# print(n, boys_number, count)










# smaller = 0
# bigger = 100
#
#
# count = 0
# while n!= boys_number:
#     n = randrange(smaller, bigger)
#     count = + 1
#     if boys_number < n:
#         n = smaller
#         if boys_number > n:
#             n = bigger
#             continue
#
#
# print(boys_number, count)











