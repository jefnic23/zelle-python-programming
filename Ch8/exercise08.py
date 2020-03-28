# The greatest common divisor (GCD) of two values can be computed using
# Euclid's algorithm. Starting with the values m and n, we repeatedly apply
# the formula: n, m = m, n%m until m is 0. At that point, n is the GCD of
# the original m and n. Write a program that finds the GCD of two numbers
# using this algorithm.


def main():
    n, m = eval(input("enter two numbers separated by a comma: "))
    while m != 0:
        n, m = m, n % m
    print("{} is the GCD".format(n))


main()
