import math

diameter = eval(input('Enter pizza diameter: '))
price = eval(input('Enter cost: '))


def area(diameter):
    return 1 / 4 * math.pi * diameter ** 2


def cost(price):
    sqin = area(diameter)
    return price / sqin


print(cost(price))
