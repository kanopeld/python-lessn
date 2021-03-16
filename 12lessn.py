from random import randint, choice
from lessn_animals import Animal
from abc import ABC, abstractmethod

class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes) and (self.seconds == other.seconds)

    def __ne__(self, other):
        return not self.__eq__(self, other)

    def __add__(self, other):
        self.seconds += other.seconds
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60

        self.minutes += other.minutes
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

        self.hours += other.hours
        return self

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'


chars = ['A', 'B', 'C', 'D']

class Car:
    last_model = ''
    __counter = 0

    def __init__(self, model=''):
        self.model = model
        Car.__counter += 1

    def __len__(self):
        return len(self.model)

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def is_ok(model):
        return len(model) > 3

    @staticmethod
    def get_random_model():
        char = chars[randint(0, len(chars) - 1)]
        return f'{char}-{randint(1, 100)}'

class Horse(Animal):
    def voice(self):
        super(Horse, self).voice('*horse voice*')


class Donkey(Animal):
    def voice(self):
        super(Donkey, self).voice('*donkey voice*')


class Mul(Donkey, Animal):
    pass


class MyException(Exception):
    def __init__(self, message='AAA!'):
        super().__init__(message)


id = 0


class BookValidationError(Exception):
    def __init__(self, id, message):
        super().__init__(f'Invalid book {id}: {message}')


class PageCountError(BookValidationError):
    def __init__(self, id):
        super().__init__(id, 'page count invalid')


class AgeError(BookValidationError):
    def __init__(self, id):
        super().__init__(id, 'age invalid')


class Book:
    def __init__(self, page_count, age, author, price):
        global id
        self.id = id

        if page_count > 500:
            raise PageCountError(id)
        self.page_count = page_count

        if age < 2000 or age > 2020:
            raise AgeError(id)
        self.age = age

        self.author = author
        self.price = price
        id += 1


class A(ABC):
    @abstractmethod
    def do_smth(self):
        print('I am a parent')


class B(A):
    def do_smth(self):
        print('I am a child')

    def test(self):
        pass


class MyInterface(ABC):
    @abstractmethod
    def do_a(self, arg1):
        raise NotImplemented

    @abstractmethod
    def do_b(self, arg1, arg2):
        raise NotImplemented


class MyClass(MyInterface):
    def do_a(self, arg1):
        print(arg1)

    # def do_b(self, arg1, arg2):
    #     pass


if __name__ == '__main__':
    pass