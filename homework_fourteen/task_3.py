

class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialization rectangle instance
        >>> test_rectangle = Rectangle()
        """
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        """
        The function sets rectangle width and height
        >>> test_rectangle = Rectangle()
        >>> test_rectangle.set_dimensions(7,7)
        """
        self.width = width
        self.height = height

    def __str__(self):
        return (f'{self.__class__.__name__} '
                f'width {self.width}, height {self.height}')

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'({self.width}, {self.height})')

    def perimeter(self):
        """

        The function calculates rectangle perimeter
        >>> rect = Rectangle(4,4)
        >>> rect.perimeter()
        32
        """
        perimeter = 2 * self.width * self.height

        if self.height == 0:
            self.height = self.width
            perimeter = 2 * self.width * self.height
        return perimeter

    def area(self):
        """
        The function calculates rectangle perimeter
        >>> test_rectangle = Rectangle(7,7)
        >>> test_rectangle.area()
        49
        """
        area = self.height * self.width
        if self.height == 0:
            self.height = self.width
            area = self.height * self.width
        return area


if __name__ == '__main__':
    import doctest
    doctest.testmod()
