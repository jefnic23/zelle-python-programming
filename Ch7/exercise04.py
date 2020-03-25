def main():
    credit = eval(input("Enter number of credits earned: "))
    if credit < 7:
        print("You are a freshman")
    elif 7 <= credit < 16:
        print("You are a sophomore")
    elif 16 <= credit < 26:
        print("You are a junior")
    elif 26 <= credit:
        print("You are a senior")


main()
