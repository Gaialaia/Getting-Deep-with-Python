# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение

n = int(input('enter n:  '))

def gen(n):
    for i in range(1,n):
        yield i

for i in gen(n):
    print(f'{i} **2')



g = (i**2 for i in range(1,n))

my_iter = iter(g)
print(my_iter)
print(next(my_iter))
print(next(my_iter))


# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

