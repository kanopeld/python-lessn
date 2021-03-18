from random import randint
from time import sleep
import sys
import argparse
import os


def create_generator():
    yield 1
    yield 2
    yield 3


def infinity_gen(rand_from, rand_to, diff):
    while True:
        yield randint(rand_from, rand_to)
        rand_from += diff
        rand_to += diff
        sleep(1)


def main():
    numbers = sys.argv[1:]
    sum = 0
    for item in numbers:
        if not item.isdigit():
            continue

        sum += int(item)

    print(sum)


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first-name', required=True)
    parser.add_argument('-ln', '--last-name', required=True)
    parser.add_argument('-br', '--born')

    args = parser.parse_args()

    with open('users.csv', 'a') as file:
        file.write(f'{args.first_name},{args.last_name},{args.born}\n')


def os_testing():
    file_path = os.path.realpath('./files')
    print(file_path)

    dir_name = os.path.dirname(file_path)
    print(dir_name)

    os.mkdir('test-mkdir')


if __name__ == '__main__':
    # <generator object createGenerator at 0x000000>
    # gen = create_generator()
    # print(f'{next(gen)}!')
    # print(f'{next(gen)}@')

    # for i in infinity_gen(0, 4, 2):
    #     print(i)
    # main()
    # arg_parse()
    os_testing()

