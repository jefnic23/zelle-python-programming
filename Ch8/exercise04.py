# The Syracuse (also called Collatz or Hailstone) sequence is generated by
# starting with a natural number and repeatedly applying the following function
# until reaching 1:
# syr(x) =  x/2 if x is even, 3x + 1 if x is odd
# For example, the Syracuse sequence starting with 5 is: 5, 16, 8, 4, 2, 1. It is
# an open question in mathematics whether this sequence will always go to
# 1 for every possible starting value.
# Write a program that gets a starting value from the user and then prints
# the Syracuse sequence for that starting value.


def main():
    num = eval(input('enter a whole number: '))
    print(num, end=" ")
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = 3*num + 1
        print(int(num), end=" ")


main()
