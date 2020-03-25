def main():
    while True:
        score = eval(input("Enter quiz score: "))
        if score == 5:
            print("Grade: A")
            break
        elif score == 4:
            print("Grade: B")
            break
        elif score == 3:
            print("Grade: C")
            break
        elif score == 2:
            print("Grade: D")
            break
        elif score == 1 or score == 0:
            print("Grade: F")
            break
        else:
            continue


main()
