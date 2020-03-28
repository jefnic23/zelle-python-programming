# The Goldbach conjecture asserts that every even number is the sum of two
# prime numbers. Write a  program that gets a number from the user, checks
# to make sure that it is even, and then finds two prime numbers that add
# up to the number.


from math import sqrt


def main():
    num = int(input("enter a whole number: "))
    while num % 2 != 0:
        num = int(input("enter a whole number: "))
    prime_nums = []
    for n in range(2, num+1):
        root = int(sqrt(n))
        prime = True
        for i in range(2, root + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            prime_nums.append(n)
    done = False
    for n in prime_nums:
        for j in prime_nums:
            if n + j == num:
                print("{0} + {1} = {2}".format(n, j, num))
                done = True
                break
            if done:
                break


main()
