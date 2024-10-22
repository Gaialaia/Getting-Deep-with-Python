# написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.


def max_of_two(a,b):
    if a > b:
        return a
    return b

def max_of_three():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    if max_of_two(a,b) > c:
        return max_of_two(a,b)
    elif max_of_two(a,b) < c:
        return  c

print(f'The biggest number is {max_of_three()}')

