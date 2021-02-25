from random import randint as get_rand

def create_matrix(x, y):
    rows = []
    for _ in range(x):
        tmp = []
        for _ in range(y):
            tmp.append(get_rand(0, 10))
        rows.append(tmp)

    return rows

def create_square_matrix(length):
    return create_matrix(length, length)

def sum_of_matrix_elements_by_divider(matrix, divider):
    sum = 0
    for parentList in matrix:
        for matrixItem in parentList:
            if matrixItem % divider == 0:
                sum += matrixItem
    return sum

# square_matrix = create_square_matrix(2)
# print(square_matrix)
# print(sum_of_matrix_elements_by_divider(square_matrix, 3))

def count_in_matrix(matrix, to_find):
    count = 0
    for parentList in matrix:
        for matrixItem in parentList:
            if matrixItem == to_find:
                count += 1
    return count

# matrix = create_matrix(2, 3)
# print(matrix)
# print(count_in_matrix(matrix, 2))

matrix = create_matrix(2, 2)

def calc_av_sum(matrix):
    count = 0
    sum = 0
    for parentList in matrix:
        for matrixItem in parentList:
            count += 1
            sum += matrixItem
    avv = sum / count
    return avv

average = calc_av_sum(matrix)
print(matrix)
print(average)

def calc_elements(matrix, average):
    count = 0
    for parentIndex, parentList in enumerate(matrix):
        print(f"parentInx: {parentIndex}, parent: {parentList}")
        for childIndex, child in enumerate(parentList):
            print(f"childInx: {childIndex}, child: {child}")
            if child > average and (parentIndex + childIndex) % 2 == 0:
                count += 1
    return count

print(calc_elements(matrix, average))
