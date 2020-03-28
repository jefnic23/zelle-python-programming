# Write a program that computes the fuel efficiency of a multi-leg journey.
# The program will first prompt for the starting odometer reading and then
# get information about a series of legs. For each leg, the user enters the
# current odometer reading and the amount of gas used (separated by a
# space). The user signals the end of the trip with a blank line. The program
# should print out the miles per gallon achieved on each leg and the total
# MPG for the trip.


def main():
    starting = eval(input("enter starting odometer reading: "))
    leg = input("enter current odometer reading and amount of gas used, separated by a space: ")
    mpg = []
    while leg != "":
        current = eval(leg.split()[0])
        gas = eval(leg.split()[1])
        miles = current - starting
        leg_mpg = miles / gas
        mpg.append(leg_mpg)
        print("{} MPG this leg".format(leg_mpg))
        starting = current
        leg = input("enter current odometer reading and amount of gas used, separated by a space: ")
    print("{} MPG for the trip".format(sum(mpg) / len(mpg)))


main()
