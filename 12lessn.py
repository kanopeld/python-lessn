from random import randint, choice

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


if __name__ == '__main__':
    car1 = Car(Car.get_random_model())
    Car('b')
    Car('t')

    print(Car.get_counter())
    print(Car.is_ok(car1))
    print(Car.get_random_model())
