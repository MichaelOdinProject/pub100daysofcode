# work out if given year is a leap year
# normal year = 365
# leap years = 366 (extra day in Feb)
# on every year that is divisible by 4
#     except every year that is evenly divisible by 100
#         unless the year is also evenly divisible by 400

# e.g year 2000
# 2000 / 4 = 500 (leap)
# 2000 / 100 = 20 (not leap)
# 2000 / 400 = 5 (leap)

year = int(input("Please choose a year to check:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP YEAR!")
        else:
            print("NOT LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("NOT LEAP YEAR!")
