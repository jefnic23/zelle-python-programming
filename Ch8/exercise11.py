# Heating and cooling degree-days are measure used by utility companies
# to estimate energy requirements. If the average temperature for a day is
# below 60, then the number of degrees below 60 is added to the heating
# degree-days. If the temperature is above 80, the amount over 80 is added
# to the cooling degree-days. Write a program that accepts a sequence of
# average daily temps and computes the running total of cooling and heating
# degree-days. The program should print these two totals after all the data
# has been processed.


def main():
    temp = input("enter average daily temperature: ")
    heating = 0
    cooling = 0
    while temp != "":
        if eval(temp) < 60:
            heating += 60 - eval(temp)
            temp = input("enter average daily temperature: ")
        elif eval(temp) > 80:
            cooling += eval(temp) - 80
            temp = input("enter average daily temperature: ")
        else:
            temp = input("enter average daily temperature: ")
    print("heating days: {0}\ncooling days: {1}".format(heating, cooling))


main()
