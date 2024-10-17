# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fraction


from fractions import Fraction

f_one = input("enter a/b: ")
f_two = input("enter c/d: ")

n, d = map(int, f_one.split('/'))
print(n,d)

n1, d1 = map(int, f_two.split('/'))
print(n1,d1)

f1 = Fraction(n,d)
f2 = Fraction(n1,d1)

fr_sum = f1 + f2
fr_mlt = f1 * f2

print(fr_sum, fr_mlt)

