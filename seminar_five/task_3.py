# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.




#
# def fib(n):
#     f1 = 0
#     f2 = 1


# n = int(input('enter n : '))
# for i in range(n):
#     if n >= 2:
#         n = (n-1) + (n-2)
#     print(n)



# def fib(n):
#     fib1 = 0
#     fib2 = 1
#
#     if n == 0:
#         return fib1
#     elif n == 1:
#         return fib2
#     else:
#         for i in range(2, n + 1):
#             fib3 = fib1 + fib2
#             fib1 = fib2
#             fib2 = fib3
#         return fib2
#
#
# print(fib(13))

n = int(input('enter n: '))
for i in range(2, n + 1):
    a
    c = a + b
    a = b
    b = c
    print(i)