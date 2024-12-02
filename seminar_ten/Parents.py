import Child
from seminar_ten.Child import child6
#task_1

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def parent_describe(self):
        print(f'{self.name}, {self.age}, {self.children}')

    def add_children(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f'{child.name} has been added to {self.name} children list')
        else:
            print(f'{child.name} that is {child.age} can not be added in the children list')

    def show_children(self):
        if self.children:
            for child in self.children:
                print(f'{child.name}')
        else:
            print(f'{self.name} has no children')

    def feed_child(self, child):
        if child in self.children and child.state =='hungry':
            child.state == 'fed'
            print(f'{child.name} is fed')
        else:
            print(f'{child.name} is not in {self.name} children list,'
                  f' let somebody else to feed him))')

    def calm_down(self, child):
        if child in self.children and child.state == 'hyper active':
            child.state == 'calmed down'
            print(f'{child.name} is calmed down')
        else:
            print(f'{child.name} is not in {self.name} children list,'
                  f' let somebody else to calm him down))')

    def fix_state(self, child):
        if child in self.children and child.state == 'other':
            child.state == 'fixed'
            print(f'{child.name} is fixed')
        else:
            print(f'{child.name} is not in {self.name} children list,'
                  f' let somebody else to fix him))')

p1 = Parent('Pavel', 45)

p1.add_children(Child.child1)
p1.add_children(Child.child3)
p1.add_children(Child.child5)
p1.add_children(Child.child8)

p1.feed_child(Child.child6)
p1.fix_state(Child.child3)

p1.show_children()

