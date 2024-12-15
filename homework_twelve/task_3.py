class Book:
    id_counter = 1

    def __new__(cls, *args, **kwargs):  #create an instance
        instance = super().__new__(cls)
        cls.id_counter +=1
        return instance

    def __init__(self, name, author): #initialize an instance
        self.name = name
        self.author = author

    def __str__(self):
        return f'{self.name}, {self.author}'


if __name__ == '__main__':

    b = Book('Mark Lutz', 'Learning Python')
    b1 = Book('Collection of folk fairy tales', 'Aphanasiev')
    print(b1.id_counter)