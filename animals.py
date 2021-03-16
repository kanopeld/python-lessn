from abc import ABC, abstractmethod

class Animal:
    pass


class FelineInterface(ABC):
    @abstractmethod
    def meow(self):
        raise NotImplemented


class CanineInterface(ABC):
    @abstractmethod
    def bark(self):
        raise NotImplemented


class FelineMixin:
    def meow(self):
        print(f'{self.name} meow')


class Pet(Animal):
    pass


class Cat(FelineMixin, Pet, FelineInterface):
    name = ''


class Dog(Pet, CanineInterface):
    def bark(self):
        print('Dog say bark')


class WildAnimal(Animal):
    pass


class Lion(FelineMixin, WildAnimal, FelineInterface):
    name = ''


class Wolf(WildAnimal, CanineInterface):
    def bark(self):
        print('Wolf say bark')


if __name__ == '__main__':
    def feline_say(interface: FelineInterface):
        interface.meow()

    cat = Cat()
    lion = Lion()

    feline_say(cat)
    feline_say(lion)

