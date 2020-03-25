# Many companies pay time-and-a-half for hours worked above 40
# in a given week. Write a program to input the number of hours
# worked and the hourly rate and calculate the total wages for the week.


def main():
    hours = eval(input("Enter number of hours worked: "))
    rate = eval(input("Enter hourly rate: "))
    if hours <= 40:
        print("Wages: $", hours * rate)
    else:
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        print("Wages: $", hours * rate + overtime_hours * overtime_rate)


main()
