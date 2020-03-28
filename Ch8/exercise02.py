# The NWS computes the windchill index using the following formula:
# 35.74 + 0.6125T - 35.75(V ** 0.16) + 0.4275T(V ** 0.16)
# Where T is the temperature in degrees Fahrenheit, and V is the wind speed
# in miles per hour.
# Write a program that prints a nicely formatted table of windchill values.
# Rows should represent wind speed for 0 to 50 in 5 mph increments, and
# the columns represent temperatures from -20 to +60 in 10-degree increments.
# Note: the formula only applies for wind speeds in excess of 3 miles per hour.


def main():
    mph = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    temp = [-20, -10, 0, 10, 20, 30, 40, 50, 60]
    for t in temp:
        if t == -20:
            print("     {}".format(t), end=" ")
        else:
            print(t, end=" ")
    print("\n    -------------------------------")
    for v in mph:
        if v < 10:
            print(v, end="  | ")
        else:
            print(v, end= " | ")
        for t in temp:
            if v < 3:
                print(t, end=" ")
            elif v > 3:
                windchill = int(35.74 + 0.6125*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16))
                print(windchill, end=" ")
        print("")


main()
