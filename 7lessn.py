from random import randint


def create_matrix(weight=2, height=2):
    matrix = []
    for _ in range(0, weight):
        row = []
        for _ in range(0, height):
            row.append(randint(0, 10))
        matrix.append(row)
    return matrix


matrix = create_matrix()


def print_matrix(matrix):
    for vert in matrix:
        for item in vert:
            print(f"Element is \"{item}\"")


# print_matrix(matrix)


def sum_matrix(matrix):
    acc = 0
    for vert in matrix:
        for item in vert:
            acc += item
    return acc


# print(sum_matrix(matrix))


def min(matrix):
    min = matrix[0][0]
    for vert in matrix:
        for item in vert:
            if item < min:
                min = item
    return min


# print(matrix)
# print(min(matrix))


def max(matrix):
    max = matrix[0][0]
    for vert in matrix:
        for item in vert:
            if item > max:
                max = item
    return max


def fact_loop(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


# print(fact_loop(3))


def fact_recursive(n):
    if n <= 1:
        return 1
    return n * fact_recursive(n - 1)


# print(fact_recursive(3))


def fib(n):
    if n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)


# print(fib(4))


def my_format(string, char='!'):
    result_string = f'{char}{string}{char}'
    return result_string


# print(my_format("Hello"))


def sum(*args):
    print(args)
    acc = 0
    for i in args:
        acc += i
    return acc


print(sum(1, 5, 70))


def my_func(a, b):
    summ = a + b
    diff = a - b
    return summ, diff, 0


summ, diff, _ = my_func(1, 2)


# 7.06
def sum_items(*args):
    if len(args) <= 0:
        return 0, 0
    acc = 0
    max = args[0]

    for item in args:
        acc += item
        if item > max:
            max = item

    return acc, max


# 7.07
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(value)


# print_kwargs(hello="Ilya", test="Qwerty")


def full_func(min, *args, **kwargs):
    print(args)
    print(kwargs)


full_func(1, 2, 3, name="Ilya")


def min2(x, *args):
    print(x, args)


min2(1, 2)


# 7.08
def avv(*args, mean_type=True):
    acc = 0
    count = 0

    if mean_type:
        for item in args:
            acc += item
            count += 1

        return acc / count

    acc = 1
    for item in args:
        acc *= item
        count += 1
    return acc ** (1 / count)


print(avv(2, 3, 4, mean_type=False))

lst = ["hello", "qwerty"]
print([i[::-1] for i in lst])

# 8.02
cars = [
    {
        "num": "ee2",
        "since": 1992,
    },
    {
        "num": "ff2134",
        "since": 1996,
    },
    {
        "num": "ea5",
        "since": 2020,
    },
]

print([car for car in cars if car["since"] > 2000])

old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {key + str(len(key)): value for key, value in old_dict.items()}
print(new_dict)


def unique(lst: list):
    seen = {}
    for i in lst:
        if not i in seen:
            seen[i] = 1
            continue
        seen[i] += 1
    return seen


if __name__ == '__main__':
    print("Hello")
    print(unique(1))
