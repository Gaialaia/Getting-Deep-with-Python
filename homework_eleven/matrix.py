#task_1
import random

class Matrix:

    def __init__(self, row, col, digit_one=0, digit_two=20):
        self.row = row
        self.col = col
        self.digit_one = digit_one
        self.digit_two = digit_two
        self.data = [[random.randint(digit_one, digit_two) for j in range(self.row)] for i in range(self.col)]

    def __add__(self, other):
        a = self.row + other.row
        b = self.col + other.col
        if self.row != other.row or self.col != other.col:
            return f'enter even quantity of rows on cols'
        return Matrix(a,b) #загадочный способ сложения

    def __sub__(self, other):
        a = self.row - other.row
        b = self.col - other.col
        if self.row != other.row or self.col != other.col:
            return f'enter even quantity of rows on cols'
        return Matrix(a, b) # выводит пустые матрицы

    def add_matrices(self, other):
        if self.row != other.row or self.col != other.col:
            return f'enter even quantity of rows on cols'
        res =  [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in range(len(self.data))]
        return f'{self.data} + {other.data} = {res}'

    def subtract_matrices(self, other):
            if self.row != other.row or self.col != other.col:
                return f'enter even quantity of rows on cols'
            res = [[self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] for i in
                   range(len(self.data))]
            return f'{self.data} - {other.data} = {res}'

    def transpose_matrice(self):
        transposed_matrix = [[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))]
        return f'{self.__class__.__name__} {self.data} transposed matrix: {transposed_matrix}'


    def __str__(self):
        # return f'{self.__class__.__name__}: {self.data}'
        matrix= '\n'.join('\t'.join(map(str, row)) for row in self.data)
        return matrix

if __name__ == '__main__':
    m = Matrix(3,2)
    m1 = Matrix(3,2)
    m2 = Matrix(2,2,7, 77)
    print(m.add_matrices(m1))
    print(m.subtract_matrices(m1))
    print(m2.transpose_matrice())
