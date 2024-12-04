class Animal:

    def __init__(self, name):
        self.name = name

    def animal_name(self):
        return self.name


    def show_size(self):
        pass

    def show_weight(self):
        pass


    def __str__(self):
        return f'Animal kind: {self.__class__.__name__}, animal name: {self.name}'


class Bird(Animal):

    def __init__(self, name, wingspan=0):
        self.wingspan = wingspan
        Animal.__init__(self, name)

    def show_wing_length(self):
        wing_length = self.wingspan / 2
        return wing_length

    def __str__(self):
        return f'{super().__str__()} wing length: {self.wingspan}'


class Fish(Animal):

    def __init__(self, name, max_depth):
            self.max_depth = max_depth
            Animal.__init__(self,name)


    def show_size(self):
        if self.max_depth < 10:
            return f'{self.name} is shallow water fish'
        elif self.max_depth < 100:
            return f'{self.name} is deep water fish'
        else:
            return f'{self.name} is average water fish'


    def __str__(self):
        return f'{super().__str__()} maximum living depth: {self.max_depth}'


class Mammal(Animal):

    def __init__(self, name, weight):
        self.weight = weight
        Animal.__init__(self,name)


    def show_weight(self):
        if self.weight < 1:
            return f'{self.name} is a tiny mammal'
        elif self.weight > 100:
            return f'{self.name} is a giant mammal'
        else:
            return f'{self.name} is an usual mammal'

    def __str__(self):
        return f'{super().__str__()}, weight: {self.weight}'

class Animal_factory:

    # def __init__(self, Animal.__class__.name):


    def create_animal(animal_type ,*args):

        animal_classes = {'bird': Bird,
                          'mammal': Mammal,
                          'fish' : Fish
                          }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            return f' wrong {animal_type}'


if __name__ == '__main__':

    animal1 = Animal_factory.create_animal('bird', 'Fluffy', 120)
    animal2 = Animal_factory.create_animal('fish', 70, 'Guru')
    animal3 = Animal_factory.create_animal('mammal', 'Kitty', 30)
    animal4 = Animal_factory.create_animal('mammal', 'cat', 25)
    print(animal4.show_weight())
    print(animal1.show_wing_length())
    print(animal1.animal_name())

    bird2 = Bird('Windy', 20)
    fish2 = Fish('Flounder', 20)
    elephant = Mammal('Bambie', 500)
    print(elephant)
    print(fish2)
    print(fish2.show_size())
    print(elephant.show_weight())
    print(bird2.__getstate__())



