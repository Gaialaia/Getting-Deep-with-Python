# Задача 1. Нахождение наибольшего общего делителя (НОД) двух
# чисел
# Программа принимает два целых числа и находит их наибольший общий
# делитель (НОД)


a = int(input("enter first number: "))
b = int(input("enter second number :"))

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print (a + b)


import math
math.gcd(a,b)