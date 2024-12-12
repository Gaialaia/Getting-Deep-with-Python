# Создайте класс Person, который имеет атрибуты name, age, и email. При
# установке значения атрибута name, оно должно начинаться с заглавной буквы.
# При установке значения атрибута age, оно должно быть целым числом в
# диапазоне от 0 до 120. При установке значения атрибута email, оно должно
from random import randrange

class Person():

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __getattribute__(self, item):
        superget = object.__getattribute__

        if item == 'name':
            return superget(self, item)

    def __setattr__(self, attr, value):
        if attr == 'name':
            if not value.istitle() or not value.isalpha():
                raise ValueError('invalid format')
        elif attr == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif attr == 'email':
            if '@' not in value:
                raise ValueError('invalid email')
        # self.__dict__[attr] = value





if __name__ == '__main__':
    p1 = Person('Papaya', 16, 'katya@.py')
    print(p1.name)













