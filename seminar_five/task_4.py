# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки

# for i in line: # повтор количества букв = количеству символов в строке * количество циклов * количество символов в 27
#    for k in line: # повтор количества букв = количеству символов в строке 3
#       for j in line: # без повтора букв строка целиком 9 раз количество букв * количество символов в строке (последний цикл всегда)
#          print(f' i: {i}   k: {k}   j: {j}')


# for i in line:
#     count += 1
#     i = line[start:0 + count]
#     print(i)

line = input('Enter line: ')
def substrings(line):
    for i in range(len(line)):
        for j in range(i + 1, len(line) + 1):
            yield line[i:j]
for i in substrings(line):
    print(i)

















