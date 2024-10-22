# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру.

def number_amount(number):
    amount = 0
    while number > 0:
        last_digit = number % 10
        amount += last_digit
        number //= 10
    print(amount)

def maximum(number):
    max_number = 0
    while number > 0:
        last_digit = number % 10
        if last_digit > max_number:
            max_number = last_digit
        number //= 10
    print(max_number)

def minimum(number):
    min_number = number % 10
    while number > 0:
        last_digit = number % 10
        if last_digit < min_number:
            min_number = last_digit
        number //= 10
    print(min_number)

while True:
    number = int(input("Enter a few digit number: "))
    operation = input("Chose 'max' or 'min' or '+': ")
    if operation == '+':
        number_amount(number)
        break
    elif operation == 'maximum':
        maximum(number)
        break
    elif operation == 'minimum':
        minimum(number)
        break
