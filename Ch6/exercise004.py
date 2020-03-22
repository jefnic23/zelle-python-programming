nat_nums = eval(input('Enter a whole number: '))

def sumN(nat_nums):
    n = 0
    for i in range(nat_nums+1):
        n += i

    return n

def sumNCubes(nat_nums):
    n = 0
    for i in range(nat_nums+1):
        n += i ** 3

    return n

print(sumN(nat_nums))
print(sumNCubes(nat_nums))

