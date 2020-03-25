def main():
    weight = eval(input("Enter weight in pounds: "))
    height = eval(input("Enter height in inches: "))
    bmi = weight * 720 / height ** 2
    if bmi > 25:
        print("bmi is {}, you are above the healthy range".format(bmi))
    elif 19 <= bmi <= 25:
        print("bmi is {}, you are within the healthy range".format(bmi))
    elif bmi < 19:
        print("bmi is {}, you are below the healthy range".format(bmi))


main()
