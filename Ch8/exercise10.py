# Modify the previous program to get its input from a file.


def main():
    file = open(input("enter name of file to load: ") + ".txt", "r")
    starting = eval(file.readline())
    leg = file.readline()
    mpg = []
    print("Starting odometer: {}".format(starting))
    while leg != "":
        current = eval(leg.split()[0])
        gas = eval(leg.split()[1])
        miles = current - starting
        leg_mpg = miles / gas
        mpg.append(leg_mpg)
        print(current, gas)
        print("{} MPG this leg".format(leg_mpg))
        starting = current
        leg = file.readline()
    print("{} MPG for the trip".format(sum(mpg) / len(mpg)))


main()
