import math

radius = eval(input('Enter sphere radius: '))


def sphere_area(radius):
    return 4 * math.pi * radius ** 2


def sphere_volume(radius):
    return 4 / 3 * math.pi * radius ** 3


print(sphere_area(radius))
print(sphere_volume(radius))
