# Write a program that uses a while loop to determine how long it takes
# for an investment to double at a given interest rate. The input will be an
# annualized interest rate, and the output is the number of years it takes an
# investment to double. Note: the amount of the initial investment does not
# matter; you can use $1.


def main():
    invest = 1
    double = invest*2
    rate = eval(input("Enter annualized interest rate: "))
    years = 0
    while invest <= double:
        invest += 1*rate
        years += 1
    print(years)


main()
