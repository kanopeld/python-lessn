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




if __name__ == '__main__':
    main()
