# A babysitter charges $2.50 an hour until 9:00 PM when the
# rate drops to $1.75 an hour (the children are in bed).
# Write a program that accepts a starting time and ending
# time in hours and minutes and calculates the total babysitting bill.
# You may assume that the starting and ending times are in a single
# 24-hour period. Partial hours should be appropriately prorated.


def main():
    starting_time = input("enter starting time as hours:minutes ")
    ending_time = input("ending ending time as hours:minutes ")
    start_hour = eval(starting_time.split(":")[0])
    start_minutes = eval(starting_time.split(":")[1])
    end_hour = eval(ending_time.split(":")[0])
    end_minutes = eval(ending_time.split(":")[1])
    if end_hour < 21:
        total_hours = (end_hour + end_minutes / 60) - (start_hour + start_minutes / 60)
        print("babysitter bill: $", total_hours * 2.5)
    else:
        early = 21 - (start_hour + start_minutes / 60)
        late = (end_hour + end_minutes / 60) - 21
        print("babysitter bill: $", early * 2.5 + late * 1.75)


main()
