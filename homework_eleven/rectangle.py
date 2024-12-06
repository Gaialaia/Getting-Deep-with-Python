
class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height
        self.perimeter = self.width * self.height

    def __str__(self):
        if self.height is None:
            self.height = self.width
            return f'It is a square'
        return f'{self.__class__.__name__} perimeter {self.perimeter}'

    def perimeter(self):
        if self.height is None:
        self.height = self.width
        return f'It is a square'
        return f'{self.perimeter}'




if __name__ == '__main__':
    r = Rectangle(25,55)
    r1 = Rectangle(15)
    print(r.perimeter)

