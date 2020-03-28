# A positive whole number n > 2 is prime if no number between 2 and sqrt(n)
# (inclusive) evenly divides n. Write a program that accepts a value of n as
# input and determines if the value is prime. If n is not prime, your program
# should quit as soon as it finds a value that evenly divides n.

from math import sqrt


def main():
    num = int(input("enter a whole number: "))
    root = int(sqrt(num))
    prime = True
    for i in range(2, root+1):
        if num % i == 0:
            prime = False
            break
    print(prime)


main()
