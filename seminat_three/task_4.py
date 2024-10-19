
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов

import random, string

psw_length = (input('Enter password length: '))
psw_length = int(psw_length)

choice_list = string.ascii_letters + string.digits + string.punctuation
print(choice_list)

psw = random.choices(choice_list, k=psw_length)
psw_str = ''.join(psw)

print(f'Your password is {psw_str}')
