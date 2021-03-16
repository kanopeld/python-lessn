if __name__ == '__main__':
    x = 2

    def h():
        global x
        x = x + 1
        print(x)

    h()

    def h():
        print(x)

    h()