import numpy as np
import math


# Initializes a matrix that will get the solutions to smaller problems with stopping conditions
# f(n,1)=n f(n,0)=0 f(n,1)=1

def table_opt(floors, eggs) -> any:
    table = [[0 for floor in range(floors + 1)] for egg in range(eggs + 1)]
    for i in range(floors + 1):
        table[1][i] = i
    for i in range(1, eggs + 1):
        table[i][1] = 1
    # print(np.asmatrix(table))
    return table


# Solve larger problems according to the formula f(n,e) = 1+min(1<=t<=n)max((t,e-1),(n-t,e)
def compute_opt(floors, eggs, table) -> int:
    for egg in range(2, eggs + 1):
        for floor in range(2, floors + 1):
            list_of_current_max = []
            for j in range(1, floor + 1):
                list_of_current_max.append(max(table[egg - 1][j - 1], table[egg][floor - j]))
            table[egg][floor] = 1 + min(list_of_current_max)
    print(np.asmatrix(table))
    print(table[eggs][floors])

    return table[eggs][floors]


def manager_opt(floors, eggs) -> int:
    table = table_opt(floors, eggs)
    return compute_opt(floors, eggs, table)


# manager_opt(105, 2)


def two_eggs(floor) -> int:
    if floor == 1:
        return 1
    x = 1
    count = 1
    while x < floor:
        x += count + 1
        count += 1
    return count


# print(two_eggs(10))

def two_eggs1(floor) -> float:
    a = 1
    b = 1
    c = -2 * floor
    return math.ceil((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))


print(two_eggs1(10))
