# Modify the previous program to find every prime number less than or equal to n.


from math import sqrt


def main():
    num = int(input("enter a whole number: "))
    for n in range(2, num+1):
        root = int(sqrt(n))
        prime = True
        for i in range(2, root + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n, end=" ")


main()
