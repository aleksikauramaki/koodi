from sys import argv

script, date = argv

date_split = date.split(".")
dots = "."*20

day = int(date_split[0])
month = int(date_split[1])
year = int(date_split[2])

def calculate_date():
    global day
    global month
    global year

    if (day > 30 and (month == 1 or month == 3 or month == 5 
        or month == 7 or month == 8 or month == 10)):
        day = 1
        month += 1
    elif (day > 29 and (month == 2 or month == 4 or month == 6 
        or month == 9 or month == 11)):
        day = 1
        month += 1
    elif (day > 30 and month == 12):
        day = 1
        month = 1
        year += 1
    else:
        day += 1

def print_date():
    global day
    global month
    global year

    print("%s.%s.%s" % (day, month, year) + dots + "\nXXX\t\t\t\tx h\n")


print_date()
calculate_date()
print_date()
calculate_date()
print_date()
calculate_date()
print_date()
calculate_date()
print_date()