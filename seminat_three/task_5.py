# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами


word = input("enter first word: ").lower()
word_two = input("enter second word: ").lower()

count = 0
for i in word:
    for j in word_two:
        if i == j:
            count += 1
            if count == len(word) and count == len(word_two):
                print(f'This pair of words {word} and {word_two} an anagram!')


