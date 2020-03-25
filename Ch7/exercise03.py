def main():
    while True:
        score = eval(input("Enter exam score: "))
        if 90 <= score <= 100:
            print("Grade: A")
            break
        elif 80 <= score <= 89:
            print("Grade: B")
            break
        elif 70 <= score <= 79:
            print("Grade: C")
            break
        elif 60 <= score <= 69:
            print("Grade: D")
            break
        elif 0 <= score <= 60:
            print("Grade: F")
            break
        else:
            continue


main()
