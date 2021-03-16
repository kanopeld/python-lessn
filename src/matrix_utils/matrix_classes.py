from random import randint


class Matrix:
    def __init__(self, length=5, height=5, random_from=0, random_to=0):
        self.length = length
        self.data = []
        for _ in range(length):
            row = []
            for _ in range(height):
                row.append(randint(random_from, random_to))
            self.data.append(row)

    def __str__(self):
        res = ("# " * self.length) + '\n'
        for row in self.data:
            for item in row:
                res += f'{item} '
            res += "\n"
        res += ("# " * self.length) + '\n'
        return res
