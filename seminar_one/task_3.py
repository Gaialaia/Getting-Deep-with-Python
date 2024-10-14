# Задача 3. Простые числа
# Напишите программу, которая считает количество простых чисел в заданной
# последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу. Последовательность
# задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна
# итерация — одно число

count = 0
r = int(input("Enter quantity of numbers: "))
for i in range(r):
    i = int(input("Enter a number: "))
    for k in range(2, int(i ** 0.5)):
        if i // k:
            print('It is not a simple number')
            break
    else:
            count+= 1
print('Simple digit quantity is ', count )



















