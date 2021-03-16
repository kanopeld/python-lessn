from matrix_classes import Matrix


class InvalidMatrixError(Exception):
    def __init__(self):
        super().__init__('Invalid matrix')


def find_max(matrix: Matrix):
    if len(matrix.data) <= 0:
        raise InvalidMatrixError

    max = matrix.data[0]
    for row in matrix.data:
        for item in row:
            if item > max:
                max = item

    return max