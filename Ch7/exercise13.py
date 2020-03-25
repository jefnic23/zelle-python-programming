# The days of the year are often numbered from 1 through 365 (or 366).
# This number can be computed in three steps using int arithmetic:
# (a) dayNum = 31(month - 1) + day
# (b) if the month is after February subtract (4(month) + 23)//10
# (c) if it's a leap year and after February 29, add 1
# Write a program that accepts a date as month/day/year, verifies that
# it is a valid date, adn then calculates the corresponding day number.


def is_date_valid(month, day, year):
    is_valid = False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            is_valid = True
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            is_valid = True
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day <= 29:
                is_valid = True
        else:
            if day <= 28:
                is_valid = True
    return is_valid


def main():
    month, day, year = input("Enter date as month/day/year ").split("/")
    month = eval(month)
    day = eval(day)
    year = eval(year)
    if is_date_valid(month, day, year):
        day_num = (31 * (month - 1) + day)
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if month > 2:
                print(day_num + 1)
        else:
            if month > 2:
                print(day_num - (4 * month + 23)//10)
    else:
        print("{0}/{1}/{2} is not a valid date".format(month, day, year))


main()
