# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом спискe.


numbers = input('enter string of numbers: ')
my_list = []
for i in numbers:
    i = int(i)
    my_list.append(i)
    max = my_list[0]
    for i in my_list:
        if i > max:
         max = i

print(f'{my_list}\n max number is {max}')



# numbers_str =  input('numbers: ').split()

# print(numbers_str)

# a, b, c, *_ =  input('numbers: ').split()
# print(a, b, c, *_)
