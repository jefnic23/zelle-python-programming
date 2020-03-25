# A year is a leap year if it is divisible by 4, unless it
# is a century year that is not divisible by 400. (1800 and
# 1900 are not leap years while 1600 and 2000 are). Write a
# program that calculates whether a year is a leap year.


def main():
    year = eval(input("enter a year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


main()
