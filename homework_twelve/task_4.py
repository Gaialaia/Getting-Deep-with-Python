
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price


    def __getattr__(self, item):
        superget = super().__getattribute__
        if item == 'name' or item == 'quantity' or item == 'price':
            return superget(self, item)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'


    def __setattr__(self, attr, value):
        if attr == 'price':
            if value < 0 and value is not isinstance(value,(int, float)):
                raise ValueError('Value error, value is to be  an integer or float type and > 0')
        elif attr == 'quantity':
            if value <= 0 and value is not isinstance(value,int):
                raise ValueError('Value error, value is to be an integer and > 0')
        super().__setattr__(attr, value)



if __name__ == '__main__':
    p = Product('Berry', 50, 7)
    p1 = Product('Mouse', 200, 656)
    print(p.price)
