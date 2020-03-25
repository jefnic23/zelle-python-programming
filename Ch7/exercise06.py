def main():
    limit = eval(input("enter speed limit: "))
    clock = eval(input("enter clocked speed: "))
    if clock <= limit:
        print("your speed is legal")
    else:
        fine = 50
        for x in range(clock - limit):
            fine += 5
        if clock > 90:
            fine += 200
        print("your speeding ticket is $", fine)


main()
