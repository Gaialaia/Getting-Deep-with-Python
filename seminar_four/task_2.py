# Правила игры «Камень, ножницы, бумага»: программа запрашивает у
# пользователя строку и выводит, победил он или проиграл. Камень бьёт
# ножницы, ножницы режут бумагу, бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число
# до тех пор, пока он не отгадает загаданное.




import random

def rock_scissors_paper():
    rsp = random.choice(['pap', 'sci', 'st'])
    while True:
        choice = input("Choose paper (pap), stone (st) or scissors (sci) and 's' to stop:    ")
        print(rsp)
        if choice == 'pap' and rsp == 'stone':
            print('You won')
        elif choice == 'st' and rsp == 'pap':
            print('You lost')
        if choice == 'st' and rsp == 'sci':
            print('You won')
        elif choice == 'sci' and rsp == 'st':
            print('You lost')
        if choice == 'sci' and rsp == 'pap':
            print('You won')
        elif choice == 'pap' and rsp == 'sci':
            print('You lost')
        elif choice == rsp:
            print('Appears to be a tie, maester!')
        elif choice == 's':
            print('See you later!')
            break


def guess_number():
    machine_number = random.randrange(1,100)
    while True:
        your_number = int(input("Enter your number: "))
        if your_number != machine_number:
            print('\U0001FAE0')
            print ("To stop the game enter 's': ")
            stop = input('')
            if stop: break
            continue
        elif your_number == machine_number:
            print(f'You guessed number! {machine_number} == {your_number}')

def games():
    game_to_play = int(input('Chose 1 for "Rock-Scissors-Paper or 2 for "Guess Number": '))
    if game_to_play == 1:
        rock_scissors_paper()
    elif game_to_play == 2:
        guess_number()
    else:
        print('Chose 1 or 2')

games()