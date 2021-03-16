from matrix_utils import matrix_classes
from matrix_utils import matrix_funcs

if __name__ == '__main__':
    m = matrix_classes.Matrix(2, 2)
    print(m)

    m1 = matrix_classes.Matrix(3, 3, 0, 10)
    print(m1)

    print(matrix_funcs.find_max(m1))