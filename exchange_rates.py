#!/usr/bin/python3

# This script will fetch the EUR-to-USD exchange rate for a given date.
# Source for exchange rate data:
# https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/usd.xml

import requests, re, pyperclip

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

date_format = input("Input the date in the following format 'dd.mm.yyyy'.\n>")
date = date_format.split(".")
d = date[0]
m = date[1]
y = date[2]
date = "%s-%s-%s" % (y, m, d)

def fetchExchangeRates():
# This fucntion will check EUR-to-USD exchange rate for a given date.
    url = ("https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_refere"
    "nce_exchange_rates/html/usd.xml")
    global date
    global date_format
    data = requests.get(url)
    lines = data.text.split("\n")
    day = findDay()

    if day == "Saturnday" or day == "Sunday":
        print("That day is %s and there is no exchange rate data available." % day)
        quit()

    for iter in lines:
        value = re.search('TIME_PERIOD="(.*?)"', iter)
        if value:
            if value.group(1) == date:
                rate = re.search('OBS_VALUE="(.*?)"', iter).group(1)
                print("On %s one Euro was equal to %s USD" % (date_format, rate))
                pyperclip.copy(rate)
                print(bcolors.OKBLUE + "Value copied to clipboard." + bcolors.ENDC)
                quit()

    print("Date not found. Make sure you included leading zeroes.")

def findDay():
# This function will check what day of the week a given date is.
# Works for years between 1700 - 2300
# Equation from: https://blog.artofmemory.com/how-to-calculate-the-day-of-the-week-4203.html
    global d
    global m
    global y

    year_code = (int(y[2]+y[3]) + int(int(y[2]+y[3]) / 4)) % 7

    mon = m.lstrip("0")
    if mon == "1":
        month_code = 0
    elif mon == "2":
        month_code = 3
    elif mon == "3":
        month_code = 3
    elif mon == "4":
        month_code = 6
    elif mon == "5":
        month_code = 1
    elif mon == "6":
        month_code = 4
    elif mon == "7":
        month_code = 6
    elif mon == "8":
        month_code = 2
    elif mon == "9":
        month_code = 5
    elif mon == "10":
        month_code = 0
    elif mon == "11":
        month_code = 3
    elif mon == "12":
        month_code = 5

    century = y[0] + y[1]
    if century == "17":
        century_code = 4
    elif century == "18":
        century_code = 2
    elif century == "19":
        century_code = 0
    elif century == "20":
        century_code = 6
    elif century == "21":
        century_code = 4
    elif century == "22":
        century_code = 2
    elif century == "23":
        century_code = 0

    if int(y) % 4 == 0 and mon == "1" or mon == "2":
        leap_year_code = 1
    else:
        leap_year_code = 0

    day = ((year_code + month_code + century_code + int(d.lstrip("0")) 
        + leap_year_code) % 7)

    if day == 0:
        return "Sunday"
    elif day == 1:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 1:
        return "Wednesday"
    elif day == 1:
        return "Thursday"
    elif day == 1:
        return "Friday"
    elif day == 1:
        return "Saturnday"

fetchExchangeRates()

''' Huom! myös tallentaa
sen clipboardille, jotta ei tartte erikseen kopioida sitä komentoriviltä.
ja sitten tee lopulta semmonen, että sieltä dripinvesting sivulta hakee
sen excelin ja siitä laskee tiettyjä arvoja tai vaikka palauttaa tiettyjä
arvoja. Se vois vaikka kattoa mitä tietoja on saatavilla ja palauttaa ne
mitä on saatavilla.'''