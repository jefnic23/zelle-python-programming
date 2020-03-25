# Write a program that accepts a date in the form month/day/year
# and outputs whether or not the date is valid. For example 5/24/1962
# is valid, but 9/31/2000 is not. (September has only 30 days).


def main():
    month, day, year = input("Enter date as month/day/year ").split("/")
    month = eval(month)
    day = eval(day)
    year = eval(year)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            print("{0}/{1}/{2} is a valid date".format(month, day, year))
        else:
            print("{0}/{1}/{2} is not a valid date".format(month, day, year))
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            print("{0}/{1}/{2} is a valid date".format(month, day, year))
        else:
            print("{0}/{1}/{2} is not a valid date".format(month, day, year))
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day <= 29:
                print("{0}/{1}/{2} is a valid date".format(month, day, year))
            else:
                print("{0}/{1}/{2} is not a valid date".format(month, day, year))
        else:
            if day <= 28:
                print("{0}/{1}/{2} is a valid date".format(month, day, year))
            else:
                print("{0}/{1}/{2} is not a valid date".format(month, day, year))
    else:
        print("{0}/{1}/{2} is not a valid date".format(month, day, year))


main()
