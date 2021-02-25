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

# average = calc_av_sum(matrix)
# print(matrix)
# print(average)

def calc_elements(matrix, average):
    count = 0
    for parentIndex, parentList in enumerate(matrix):
        print(f"parentInx: {parentIndex}, parent: {parentList}")
        for childIndex, child in enumerate(parentList):
            print(f"childInx: {childIndex}, child: {child}")
            if child > average and (parentIndex + childIndex) % 2 == 0:
                count += 1
    return count

# print(calc_elements(matrix, average))

lst = ['Петрова', 'Сидоров']
def print_lastnames(names):
    for name in names:
        if name[0] == 'П' and name[-1] == 'а':
            print(name)
# print_lastnames(lst)

pupils = [{"name":"User1","physics":5,"history":7}, {"name":"User2","physics":3,"history":2}, {"name":"User2","physics":6,"history":4}]
def calc_av_score(users):
    for user in users:
        av = (user["physics"] + user["history"]) / 2
        user["score"] = av

calc_av_score(pupils)

def print_good_students(students, needScore):
    for student in students:
        if student["score"] >= float(needScore):
            print(f'Good student is: {student["name"]}')

print_good_students(pupils, 4)