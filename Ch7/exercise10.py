# The formula for Easter in the previous problem works for every
# year in the range 1900-2099 except for 1954, 1981, 2049, and
# 2076. For these 4 years it produces a date that is one week too
# late. Modify the above program to work for the entire range 1900 - 2099.


def main():
    year = eval(input("enter a year between 1900 and 2099: "))
    while 1900 >= year >= 2099:
        year = eval(input("enter a year between 1900 and 2099: "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    date = 22 + d + e
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        date -= 7
    if date <= 31:
        print("Easter is on March {}".format(date))
    else:
        print("Easter is on April {}".format(date - 31))


main()
