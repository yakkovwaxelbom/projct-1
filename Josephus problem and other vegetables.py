import re
import numpy as np


def is_power_of_2(n) -> bool:
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


def solving_josephus_problem(n) -> int:
    if is_power_of_2(n):
        return 1
    else:
        k = 0
        while 2 ** k < n:
            k += 1
        k -= 1
        survives = (n - 2 ** k) * 2 + 1
        print(2 ** k)
        return survives


# print(solving_josephus_problem(9))


def find_nax_word(word: str) -> tuple:
    abc = {}
    for i in word:
        abc.update({i: 0})
    for i in word:
        abc.update({i: abc.get(i) + 1})
    return max([(value, key) for key, value in abc.items()])


# print(find_nax_word("Hello World"))


def find_nax_word1(word) -> tuple:
    abc = {}
    for i in word:
        abc[i] = 0
    for i in word:
        abc[i] += 1
    abc.pop(' ')
    return max((value, key) for key, value in abc.items())


#
# print(find_nax_word1('Yaakov wakselbom is the king of kings and dovi amiram is not'))
#
# # #
# a = 'Hello World'
# # b = re.search(pattern,a)
# # print(b)
# b = 'Hello World'
#
# text = "This is a test string ."
#
# match = re.match(a, b)
#
# if match:
#     print("Found a match!")
# else:
#     print("No match found.")
#
# pattern = '[^0-9]'
# test_string = ''
# result = re.match(pattern, test_string)
#
# if result:
#     print("Search successful.")
# else:
#     print("Search unsuccessful.")
#

# word=str(word)
# print(abc)
# abc.pop(' ')

def euclid(a, b) -> int:
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return euclid(b, a % b)


# print(euclid(230, 100))


def third_maximum_number(array: list) -> float:
    for i in range(2):
        index = a.index(max(array))
        del array[index]
    return max(array)


def connecting_matrices(matrix1: list, matrix2: list) -> list:
    solution = [[0 for column in range(len(matrix1[0]))] for row in range(len(matrix1))]
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                solution[i][j] = matrix1[i][j] + matrix2[i][j]
        return solution
    else:
        raise ValueError("Illegal connecting")


def matrix_multiplication(matrix1: list, matrix2: list) -> np:
    if len(matrix1[0]) == len(matrix2):
        solution = [[0 for column in range(len(matrix2[0]))] for row in range(len(matrix1))]
        for r in range(len(matrix2[0])):
            for i in range(len(matrix1)):
                current_cell = 0
                for j in range(len(matrix2)):
                    current_cell += matrix1[i][j] * matrix2[j][r]
                    solution[i][r] = current_cell
        return np.asmatrix(solution)
    else:
        raise ValueError("Illegal multiplication")


def recession_matrix_multiplication(matrix1: list, matrix2: list) -> np:
    if len(matrix1) <= 1:
        return [sum(a * b for a, b in zip(matrix1[0], matrix2[0]))]


    # I divide the matrices into 8 matrices whose size is n/2
    a, b, c, d, e, f, g, h = [], [], [], [], [], [], [], []
    for i in range(len(matrix1) // 2):
        a.append([j for j in matrix1[i][:len(matrix1) // 2]])
    for i in range(len(matrix1) // 2):
        b.append([j for j in matrix1[i][len(matrix1) // 2:]])
    for i in range(len(matrix1) // 2):
        c.append([j for j in matrix1[i + len(matrix1) // 2][:len(matrix1) // 2]])
    for i in range(len(matrix1) // 2):
        d.append([j for j in matrix1[i + len(matrix1) // 2][len(matrix1) // 2:]])
    for i in range(len(matrix2) // 2):
        e.append([j for j in matrix2[i][:len(matrix2) // 2]])
    for i in range(len(matrix2) // 2):
        f.append([j for j in matrix2[i][len(matrix2) // 2:]])
    for i in range(len(matrix2) // 2):
        g.append([j for j in matrix2[i + len(matrix2) // 2][:len(matrix2) // 2]])
    for i in range(len(matrix2) // 2):
        h.append([j for j in matrix2[i + len(matrix2) // 2][len(matrix2) // 2:]])
    # I recursively call each sub-matrix
    a_e = recession_matrix_multiplication(a, e)
    b_g = recession_matrix_multiplication(b, g)
    a_f = recession_matrix_multiplication(a, f)
    b_h = recession_matrix_multiplication(b, h)
    c_e = recession_matrix_multiplication(c, e)
    d_g = recession_matrix_multiplication(d, g)
    c_f = recession_matrix_multiplication(c, f)
    d_h = recession_matrix_multiplication(d, h)
    # I connect the sub-matrices to solve a quarter matrix
    quadrant1 = connecting_matrices(a_e, b_g)
    quadrant2 = connecting_matrices(a_f, b_h)
    quadrant3 = connecting_matrices(c_e, d_g)
    quadrant4 = connecting_matrices(c_f, d_h)
    x, y = [], []
    for i in range(len(quadrant1[0])):
        x.append(quadrant1[i] + quadrant2[i])
    for i in range(len(quadrant1[0])):
        y.append(quadrant3[i] + quadrant4[i])
    return x + y


def transpose_matrix(matrix: list) -> np:
    solution = [[0 for column in range(len(matrix))] for row in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            solution[j][i] = matrix[i][j]
    return np.asmatrix(solution)


a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
b = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(recession_matrix_multiplication(a,b))

