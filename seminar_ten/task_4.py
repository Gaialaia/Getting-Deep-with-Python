class Animal:

    def __init__(self, name):
        self.name = name


    def show_size(self):
        pass

    def show_weight(self):
        pass


    def __str__(self):
        return f'{self.__class__.__name__} {self.name}'






class Bird(Animal):

    def __init__(self, name, wingspan):
        self.wingspan = wingspan
        super().__init__(name)



    def show_size(self):
        wing_length = 0
        return wing_length


    def __str__(self):
        return f'{super().__str__()} {self.wingspan}'




class Fish(Animal):

    def __init__(self, name, max_depth):
        self.max_depth = max_depth
        super().__init__(name)


    def show_size(self):
        if self.max_depth < 10:
            print(f'{self.name} is shallow water fish')
        elif self.max_depth < 100:
            print(f'{self.name} is deep water fish')
        else:
            print(f'{self.name} is average water fish')


    def __str__(self):
        return f'{super().__str__()} {self.max_depth}'


class Mammal(Animal):

    def __init__(self, name, weight):
        self.weight = weight
        super().__init__(name)


    def show_weight(self):
        if self.weight < 1:
            print(f'{self.name} is a tiny mammal')
        elif self.weight > 100:
            print(f'{self.name} is a giant mammal')
        else:
            print(f'{self.name} is an usual mammal')

    def __str__(self):
        return f'{super().__str__()} {self.weight}'

class Animal_factory():

    def create_animal(animal_type, *args):
        animal_classes = {'bird': Bird,
                          'mammal': Mammal,
                          'fish' : Fish
                          }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            print(f' wrong {animal_type}')


bird1 = Animal_factory.create_animal('bird', 'Fluffy', 120)
fish1 = Animal_factory.create_animal('fish', 70, 'Guru')
mammal1 = Animal_factory.create_animal('mammal', 'Kitty', 30)


