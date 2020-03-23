nat_nums = eval(input('Enter a whole number: '))


def sum_n(nat_nums):
    n = 0
    for i in range(nat_nums + 1):
        n += i

    return n


def sum_n_cubes(nat_nums):
    n = 0
    for i in range(nat_nums + 1):
        n += i ** 3

    return n


print(sum_n(nat_nums))
print(sum_n_cubes(nat_nums))
