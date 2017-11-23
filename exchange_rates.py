#!/usr/bin/python3

# This script will fetch the EUR-to-USD exchange rate for a given date.
# Source for exchange rate data:
# https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/usd.xml

import requests, re, pyperclip, calendar

# To prettify part of the ouput.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    date_format = input("Input the date in the following format 'dd.mm.yyyy'.\n>")
    date = date_format.split(".")
    d = date[0]
    m = date[1]
    y = date[2]
    date = "%s-%s-%s" % (y, m, d)
    fetchExchangeRates(date, date_format, d, m, y)

# This fucntion will check EUR-to-USD exchange rate for a given date.
# It will let you know in case the date is in wrong format, or if the
# the date happens to be on weekend and there is no data available.
def fetchExchangeRates(date, date_format, d, m, y):
    url = ("https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_refere"
    "nce_exchange_rates/html/usd.xml")
    date
    date_format
    data = requests.get(url)
    lines = data.text.split("\n")
    #day = findDay(d, m, y)
    day = calendar.weekday(int(y), int(m), int(d))

    if day == 5:
        print("That day is Saturnday and there is no exchange rate data"
        " available.")
        quit()
        
    elif day == 6:
        print("That day is Sunday and there is no exchange rate data"
        " available.")
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

main()