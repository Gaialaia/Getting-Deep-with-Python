import csv

from abc import abstractmethod, ABC

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class GradesMarksCheck(Validator):

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    # def __set_name__(self, owner, name):   #class Student, class student attr, checks class attr marks, grades
    #     self.param_name = '_' + name
    #
    # def __get__(self, instance, owner):
    #     return getattr(instance, self.param_name)
    #
    # def __setattr__(self, instance, value):
    #     self.validate(value)
    #     setattr(instance, self.param_name, value)

    def validate(self, value):  #checks values
        if not isinstance(value, int):
            return TypeError(f'')
        if self.min_value is not None and value < self.min_value:
            return ValueError(f'')
        if self.max_value is not None and value > self.max_value:
            return ValueError(f'')


class NameCheck(Validator):

    def __init__(self, predicate=None):
        self.predicate = predicate
    #
    # def __set_name__(self, owner, name):
    #     self.private_name = '_' + name
    #
    # def __set__(self, obj, value):
    #     self.validate(value)
    #     setattr(obj, self.private_name, value)

    def validate(self, value):  # checks values
        if not isinstance(value, str):
            return TypeError(f'')
        if not value.isalpha() or not value.istitle():
            return ValueError(f'Write name in title and letters')
        return f'{value}'


class Student:
    marks = GradesMarksCheck(1,5)
    full_name = NameCheck(predicate=None)

    def __init__(self, full_name, marks):
        self.full_name = full_name
        self.marks = marks

    def __str__(self):
        return f'{self.full_name} {self.marks}'


s1 = Student('ji',10)

print(s1)
















