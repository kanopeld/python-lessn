import os
import argparse


template = """def main():
    pass

if __name__ == '__main__':
    main()
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', required=True)
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()
    os.mkdir(args.dir)

    with open(f'{args.dir}/{args.file}', 'w') as file:
        if '.py' not in args.file:
            return
        file.write(template)


if __name__ == '__main__':
    main()
