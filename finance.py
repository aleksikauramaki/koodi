# See details here: http://www.jarloo.com/yahoo_finance/
# Query: http://finance.yahoo.com/d/quotes.csv?s=AAPL&f=nb
# Info:
# https://stackoverflow.com/questions/10040954/alternative-to-google-finance-api

#Name, Bid, Divident, Divident yield, change today in precent

#file = http://finance.yahoo.com/d/quotes.csv?s=AAPL&f=nbdyp2
#read.file()

import requests, json, sys, re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def start():
    get_data(get_symbol())

def get_symbol():
    company = input("Which company do you want to look up?:\n>")
    symbol_url = ("http://d.yimg.com/aq/autoc?query=%s&region=US&lang=en-US"
        "&callback=YAHOO.util.ScriptNodeDataSource.callbacks" % company)
    
    symbol_data = requests.get(symbol_url)
    symbol_strings = re.findall(r'({.*})', symbol_data.text)

    symbol = {}    
    if symbol_strings:
        symbol = json.loads(symbol_strings[0])
    return symbol.get('ResultSet').get('Result')[0].get('symbol')

def get_data(company_symbol):
    data_url = ("http://finance.yahoo.com/d/quotes.csv?s=%s"
        "&f=nbdyp2" % company_symbol)
    stock_data = requests.get(data_url).text
    stock_data = stock_data.split(',')
    print(stock_data)
    name = stock_data[0]
    price = stock_data[1]
    divident = stock_data[2]
    dyield = stock_data[3]
    days_change = stock_data[4]
    print(bcolors.HEADER + "\n" + name + bcolors.ENDC + bcolors.OKGREEN + 
        "\n" + "Stock price:\t" + '$ ' + price + "\n" + "Todays chage:\t" +
        days_change + "\nDivident yield:\t" + dyield + '%' + bcolors.ENDC + "\n")

start()

'''http://finance.yahoo.com/d/quotes.csv?s=nokia&f=nbdyp2'''