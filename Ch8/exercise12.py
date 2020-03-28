# Modify the previous program to get its input from a file.


def main():
    file = open(input("enter name of file to load: ") + ".txt", "r")
    temp = file.readline()
    heating = 0
    cooling = 0
    while temp != "":
        if eval(temp) < 60:
            heating += 60 - eval(temp)
            temp = file.readline()
        elif eval(temp )> 80:
            cooling += eval(temp) - 80
            temp = file.readline()
        else:
            temp = file.readline()
    print("heating days: {0}\ncooling days: {1}".format(heating, cooling))


main()
