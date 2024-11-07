
# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке

# words_list = ["pancake", "pumpkin", "beer", "mango", "lemon", "beer", "odd", "odd", "apple", "vine",
#               "maple", "mango", "beer"]

# words_list_dict = {}
# for i in words_list:
#     c = words_list.count(i)
#     words_list_dict.setdefault(i,c)
# print(words_list_dict)



def count_values(words_list):
    words_list_dict = {}
    for i in words_list:
        c = words_list.count(i)
        words_list_dict.setdefault(i,c)
    return words_list_dict

# print(count_values(["pancake", "pumpkin", "beer", "mango", "lemon", "beer", "odd", "odd", "apple", "vine",
#             "maple", "mango", "beer"]))


