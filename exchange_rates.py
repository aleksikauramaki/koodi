#!/usr/bin/python3



# This script will fetch the USD-to-EUR exchange rate for a given date.
# https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/usd.xml

from xml.etree import ElementTree
import requests

print("This script will fetch the exchange rate for USD to EUR for a"
    "given date.")
date = input("Input the date in the following format 'dd.mm.yyyy'.\n>")
date = date.split(".")
d = date[0]
m = date[1]
y = date[2]
date = "%s-%s-%s" % (y, m, d)

print(date)

url = ("https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_refere"
    "nce_exchange_rates/html/usd.xml")

data = requests.get(url)

#xml = ElementTree.fromstring(data.content)
#e = ElementTree.parse(data.content).getroot()

''' Huom! tee tähän semmonen että tää hakee sen oikean exchange
raten sieltä sivulta ja printtaa sen, mutta samalla myös tallentaa
sen clipboardille, jotta ei tartte erikseen kopioida sitä komentoriviltä.
ja sitten tee lopulta semmonen, että sieltä dripinvesting sivulta hakee
sen excelin ja siitä laskee tiettyjä arvoja tai vaikka palauttaa tiettyjä
arvoja. Se vois vaikka kattoa mitä tietoja on saatavilla ja palauttaa ne
mitä on saatavilla.'''
