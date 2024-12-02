#task_2
import random

class Human:
    def __init__(self, name,house):
        self.name = name
        self.satiation_level = 50
        self.house = house


    def add_house(self):
        self.house = House.street
        print(f'{self.name} lives in {House.street}')


    def eat(self):
        if True:
            self.satiation_level += 44
            House.money -= 20
            print(f'{self.satiation_level}, {House.money}')

    def go_for_grocery(self, unit, price): #переменные метода без селф
            self.satiation_level -= 13
            House.food += unit
            House.money -= price
            print(f'Now you have {House.food} units of food and {House.money} left')

    def go_for_work(self):
          House.money += 150
          self.satiation_level -= 30
          print(f'Your balance is {House.money} money units '
                f'and your satiation level {self.satiation_level}')

    def play_games(self): # переменные внутри метода без self
        self.satiation_level -= 16
        print('It is time to play games')

    def relax_time(self):
        self.satiation_level += 17
        print(f'your satiation level is {self.satiation_level}')


    def __str__(self):
        return (f'name: {self.name}, satiation level {self.satiation_level}, '
                f'money: {House.money}, food: {House.food}')

    def throw_dice(self):
        dice = random.randint(1, 6)
        print(f'Your dice is {dice}!')

        if self.satiation_level < 20:
            Human.eat(self)
        elif House.food < 10:
            Human.go_for_grocery(38,26)
        elif House.money < 50:
            Human.go_for_work(self)
        elif dice == 1:
            Human.go_for_work(self)
        elif dice == 2:
            Human.eat(self)
        elif dice == 3:
            Human.relax_time(self)
        else:
            Human.play_games(self)
        if self.satiation_level <=0:
            print(f'{self.name} has died of hunger')


        print(self.__str__())


class House:
    food = 50 #атрибуты класса, распространяются на все экземпляры
    money = 0

    def __init__(self, street):  #атрибуты, которые заполняют при создании экземпляра, доступны классу
        self.street = street
        self.type = 'apt'  #определённый атрибут экземпляра, доступен любому экземпляру, не доступен классу


hse = House('Victory street')
hse1 = House('Olymp')
hse3 = House('Willow lane')
h1 = Human('Leroy', hse)
h2 = Human('Aerka', hse)
h3 = Human('Mars', hse3)




# for day in range(1,366):
#     print(f'day {day}')
#     if not h1.throw_dice() or not h2.throw_dice():
#         print(f'person died on {day} day')
#
#         print(f' {h1.__str__()}, \n {h2.__str__()}')


for day in range(1,366):
    print(f'day {day}')
    if not h3.throw_dice():
        print(f'person died on {day} day')

        print(f' {h3.__str__()}')