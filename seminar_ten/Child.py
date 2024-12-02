#task_1
import Parents

class Child:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    def get_state(self):
        if self.state == 'hungry':
            print(f'Feed {self.name}')
        elif self.state == 'calm':
            print(f'{self.name} is calm')
        elif self.state == 'other':
            print(f'Consult mother')
            if not self.state:
                print(f'{self.name} is fine')

child1 = Child('Leonardo', 5, 'hungry')
child2 = Child('Clement', 6, 'calm')
child3 = Child('Ragnar', 12, 'other')
child4 = Child('Vasilisa', 7, 'hyper active')
child5 = Child('Merzcana', 25, 'hungry')
child6 = Child('Ayax', 17, 'hungry')

child7 = Child('Polina', 27, 'hyper active')
child8 = Child('Violetta', 89, 'hungry')




