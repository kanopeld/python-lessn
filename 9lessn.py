from functools import reduce
import time

if __name__ == '__main__':
    # Start 9.01
    def print_name(name):
        print(f"Hello, {name}")


    print_name_2 = lambda name: print(f"Hello, {name}")

    # print_name("Ilya")
    # print_name_2("Ilya")
    # End 9.01

    # Start 9.02

    print_names = lambda names: [print_name_2(name) for name in names]
    # print_names(["Ilya", "Vasia"])

    # End 9.02

    # Start 9.03

    # print(list(map(lambda x: str(x), [1, 2, 3])))

    # End 9.03

    result = filter(lambda x: x > 4, [1, 2, 3, 4, 5, 6])
    # print(list(result))

    # Start 9.04
    # print(list(filter(lambda x: "k" in x, ["Ilya", "Nikolai"])))
    # End 9.04

    result = reduce(lambda a, x: a + x, [1, 2, 3])

    # print(result)

    # Start 9.05
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    filtered = list(filter(lambda x: x % 3 == 0, nums))
    result = reduce(lambda x, y: x * y, filtered)

    # print(result)
    # print(reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, nums)))
    # End 9.05

    def print_copyright(func):
        def wrap():
            print("It is my code")
            func()
        return wrap

    def counter(func):
        count = 0
        def wrap():
            nonlocal count
            count += 1
            func()
            print(f"count is {count}")
        return wrap

    @print_copyright
    def print_hello():
        print("Hello!")


    @print_copyright
    @counter
    def print_bye():
        print("Bye!")


    # decorator_hello = print_copyright(print_hello)
    # decorator_hello()

    # print_hello()
    # print_bye()
    # print_bye()
    # print_bye()

    # Start 9.06
    def calc_time(func):
        def wrap(*args, **kwargs):
            start_at = time.time()
            res = func(*args, **kwargs)
            end_at = time.time()
            print(f"{end_at - start_at}")
            return res
        return wrap


    @calc_time
    def long(n):
        for _ in range(n):
            pass


    @calc_time
    def short(n, x):
        for _ in range(n, x):
            pass


    long(100500 * 1000)
    short(1, x=100)
    # End 9.06
