from abc import abstractmethod, ABC

class Shape(ABC):  # класс не является абстрактным, если не наследуется от ABC

    @abstractmethod
    def area(self,*args):
        pass

class Circle(Shape):
    def __init__(self):
        self.pi = 3.14

    def area(self, radius):
        Shape().area(self, radius)
        return self.pi*radius**2

class Triangle(Shape):

    def area(self,base, height):
        Shape().area(self, base, height)
        return base*height/2

class Rectangle(Shape):
    def area(self, side_one, side_two):
        Shape().area(self, side_one, side_two)
        return side_one * side_two




if __name__ == '__main__':

    c1 = Circle()
    t1 = Triangle()
    r1 = Rectangle()
    s = Shape()

    print(c1.area(15))
    print(t1.area(5,8))
    print(r1.area(5,5))
    print(s.area(5,4))