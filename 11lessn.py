class Dog:
    __name = ''
    __master = True
    __address = "Minsk"

    def __init__(self, name, color):
        self.__name = name
        self.color = color

    def bark(self):
        print(f"Woof {self.__name}, color is {self.color}")

    def set_name(self, new_name):
        if new_name == "Qwerty":
            return
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_master(self) -> bool:
        return self.__master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        print("Im here")
        self.__address = new_address


def main():
    dog1 = Dog("Rax", "brawn")
    dog1.bark()
    dog1.set_name("Qwerty")
    dog1.bark()
    print(dog1.get_name())
    print(dog1.address)
    dog1.address = "Riga"
    print(dog1.address)

    # bad_dog = {"name": "Rax", "age": 12}
    # def bad_bark(dog):
    #     print(f"Woof {dog['name']}")
    #
    # bad_bark(bad_dog)

class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self. y = y


class Line:
    point_a = None
    point_b = None

    def __init__(self, a: Point, b: Point):
        self.point_a = a
        self.point_b = b

    def length(self):
        diff = self.point_a.y - self.point_b.y
        if diff < 0:
            diff = -diff
        return diff


def points():
    line = Line(Point(1, 2), Point(1, 6))
    print(line.length())

if __name__ == '__main__':
    points()
