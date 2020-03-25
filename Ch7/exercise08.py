# A person is eligible to be a US senator if they are at
# least 30 years old and have been a US citizen for at least
# 9 years. To be a US representative these numbers are 25
# and 7, respectively. Write a program that accepts a person's
# age and years of citizenship as input and outputs their
# eligibility for the Senate and House.


def main():
    age = eval(input("enter age: "))
    citizen = eval(input("enter years of citizenship: "))
    if age >= 30 and citizen >= 9:
        print("you are eligible for the Senate and House")
    elif age >= 25 and citizen >= 7:
        print("you are only eligible for the House")
    else:
        print("you are not eligible for Congress")


main()
