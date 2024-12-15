#task_2, example that helped me to understand __getattribute__, __setattr__, p.500-501

class Person:

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
        # # self.__dict__[attr] = value
        super().__setattr__(attr, value) # lets to print instance.name without it gives error "object has no attr 'attr"


if __name__ == '__main__':
    p1 = Person('Papaya', 16, 'katya@.py')
    print(p1.name)













