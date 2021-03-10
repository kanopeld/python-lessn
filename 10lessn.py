import json
from random import randint
from local_module import hello_local_module
import test.sub_module as submodule

def main():
    file = open("files/file.txt")
    lines = []
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line)

    print(file)
    file.close()
    # print(lines[0])
    # print(lines[-1])
    # print(lines[:2])
    # print(lines[:])

    file = open("files/file.txt")
    # print(file.readlines())
    file.close()

    with open('files/file.txt') as my_file:
        for line in my_file.readlines():
            print(line)

    with open('files/file.txt', 'a') as my_file:
        my_file.writelines(['line1', 'line2'])


def task10_04():
    with open("files/zore-one.txt") as incoming:
        with open("files/zero-one-output.txt", "w") as output:
            for line in incoming.readlines():
                print(f"devore {line}")
                edited = line.replace("0", "@").replace("1", "0").replace("@", "1")
                print(f"after {line}")

                output.write(edited)


def task10_05():
    with open("files/zore-one.txt") as incoming:
        even = open("files/even.txt", "w")
        odd = open("files/odd", "w")

        for index, line in enumerate(incoming.readlines()):
            diff = (index + 1) % 2
            if diff == 0:
                even.write(line)
            else:
                odd.write(line)

        even.close()
        odd.close()


def json_01():
    with open("files/json.json", "w") as json_file:
        data = json.dumps({"name": "Ilya", "age": 25})
        print(data)
        json_file.write(data)


def json_02():
    with open("files/json.json") as json_file:
        data = json.loads(json_file.read())
        print(data)
        print(f"Name is {data['first_name']}")
        # json_file.write(data)
        if data['is_teacher']:
            print("Good")


def task10_07():
    def create_matrix(n):
        matrix = []
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(randint(1, 10))
            matrix.append(row)
        return matrix

    with open("files/matrix.json", "w") as file:
        matrix = create_matrix(4)
        file.write(json.dumps({"matrix": matrix}))

    with open("files/matrix.json") as file:
        data = json.loads(file.read())
        loaded_matrix = data["matrix"]

        for parentIndex, rows in enumerate(loaded_matrix):
            for valueIndex, value in enumerate(rows):
                if value % 2 == 0:
                    loaded_matrix[parentIndex][valueIndex] = 0

        print(loaded_matrix)


if __name__ == '__main__':
    hello_local_module()
    submodule.hello_sub_module()