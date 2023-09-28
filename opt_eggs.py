import numpy as np


def table_opt(floors, eggs) -> any:
    table = [[0 for floor in range(floors + 1)] for egg in range(eggs + 1)]
    for i in range(floors + 1):
        table[1][i] = i
    for i in range(1, eggs + 1):
        table[i][1] = 1
    # print(np.asmatrix(table))
    return table


def compute_opt(floors, eggs, table) -> int:
    #  [ 0  1  2  2  0  0  0  0  0  0  0]]
    for egg in range(2, eggs + 1):
        for floor in range(2, floors + 1):
            list_of_current_max = []
            for j in range(1, floor + 1):
                list_of_current_max.append(max(table[egg -1][j - 1], table[egg][floor-j]))
            table[egg][floor] = 1 + min(list_of_current_max)
    print(np.asmatrix(table))
    print(table[eggs][floors])

    return table[eggs][floors]


def manager_opt(floors, eggs):
    table = table_opt(floors, eggs)
    return compute_opt(floors, eggs, table)


manager_opt(11, 2)
