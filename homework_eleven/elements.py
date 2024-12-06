#task_2

import random

class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava().__class__.__name__
        elif isinstance(other,Water):
            return Dirt().__class__.__name__
        elif isinstance(other, Air):
            return Dust().__class__.__name__

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Geyser().__class__.__name__
        elif isinstance(other, Earth):
            return Coal().__class__.__name__
        elif isinstance(other, Air):
            return Gas().__class__.__name__


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Fog().__class__.__name__
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning().__class__.__name__
        elif isinstance(other, Earth):
            return Dust().__class__.__name__
        elif isinstance(other, Water):
            return Fog()

class Coal:
    pass

class Clay:
    def __str__(self):
        return f'You have {self.__class__.__name__} so you can make pots'

class Fog:
    def __str__(self):
        return f'Now it is {self.__class__.__name__}'

class Storm:
    pass

class Lightning:
    pass

class Lava:
    pass

class Dirt:
    pass

class Steam:
    def __str__(self):
        return f'There is {self.__class__.__name__} so go to banya'

class Dust:
    pass

class Geyser:
    pass

class Gas:
    pass

def mix_two_elements():
    elements = [Earth(), Fire(), Water(), Air()]
    element_one = random.choice(elements)
    element_two = random.choice(elements)
    mixture = element_one + element_two
    if mixture is None:
        mix_two_elements()
    return print(mixture)


if __name__ == '__main__':
    earth1 = Earth()
    fire1 = Fire()
    water1 = Water()
    air1 = Air()
    print(earth1+water1)
    print(air1+fire1)
    print(water1+earth1)
    mix_two_elements()



