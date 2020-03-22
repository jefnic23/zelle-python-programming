import math

radius = eval(input('Enter sphere radius: '))

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return 4 / 3 * math.pi * radius ** 3

print(sphereArea(radius))
print(sphereVolume(radius))
