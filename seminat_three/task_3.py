# Задача 3. Проверка палиндрома
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).

# 'Won’t lovers revolt now'


phrase = input('enter phrase or word: ').lower()

phrase.lower().strip().replace(' ','')
# if ',' or '.' or '’' or '?'or '!' in phrase:
#     phrase.replace(',', '').replace(' ','').replace('’','') \
#     .replace('?','').replace('!','')

phrase_list=[]

for i in phrase:
    phrase_list.append(i)
print(f'phrase {phrase_list}')
ph = list(reversed(phrase_list))
print(f'reversed phrase {ph}')
if phrase_list == ph:
    print('This string is a palindrome!')


