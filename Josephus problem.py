def is_power_of_2(n):
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True


def solving_josephus_problem(n):
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


print(solving_josephus_problem(9))

