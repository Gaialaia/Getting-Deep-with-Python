# Задание 1. Рамка
# Напишите программу, которая рисует прямоугольную рамку с помощью
# символьной графики. Для вертикальных линий используйте символ
# вертикального штриха (|), а для горизонтальных — дефис (-). Пусть ширину и
# высоту рамки определяет пользователь.

length = int(input(" Enter frame length: "))
width = int(input(" Enter frame width: "))
length_corr = length - 1
for i in range(length):
    length_corr = '|'
    s = " " * width
    d = "-" * width
    if i == 0: print(length_corr,s,length_corr)
    if i == length-1: print(length_corr,s,length_corr)
    else:
            print(length_corr,d,length_corr)
