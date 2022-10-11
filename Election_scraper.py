"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jana Karbanova
email: xkarbanovaj@gmail.com
discord: JanaK#0342
"""

import sys
import csv
import re
import requests
from bs4 import BeautifulSoup as BS

attr = re.compile(r"t[1,2]sa1 t[1,2]sb2")
attr2 = re.compile(r"t[1,2]sa2 t[1,2]sb3")


def open_url(weblink: str) -> requests.models.Response:
    unit = requests.get(weblink)
    return unit


def replace_character(object, ch1: str, ch2: str) -> str:
    """takes text content of the soup and change unwanted character/string
     for new one, takes only text content"""
    if ch1 in object.text:
        object1 = object.text.replace(ch1, ch2)
    else:
        object1 = object.text
    return object1


def cycle_replace_character(object2, ch1: str, ch2: str) -> list:
    """passes through the list and changes unwanted character/string
     for new one in the list """
    party_change_char = []
    for p in object2:
        pp = replace_character(p, ch1, ch2)
        party_change_char.append(pp)
    return party_change_char


def cycle_replace_direct(object3: list, ch1: str, ch2: str) -> list:
    """changes unwanted character/string for new one in the cleaned list """
    for i, p in enumerate(object3):
        if ch1 in p:
            object3[i] = p.replace(ch1, ch2)
    return object3


def main() -> None:

    data_all = list()
    parties_names_changed_char2 = list()

    if len(sys.argv) != 3:
        print(f"Chybny pocet zadanych argumentu ({len(sys.argv)})")
        quit()

    url = str(sys.argv[1])
    output_file = str(sys.argv[2])

    district = open_url(url)
    soup = BS(district.text, 'html.parser')
    number = soup.find_all("td", class_="cislo")
    city = soup.find_all("td", class_="overflow_name")
    run = 0
    print(f"STAHUJI DATA Z VYBRANEHO URL: {url}")
    for n, c in zip(number, city):

        # collects links to data of individual cities
        link = "https://volby.cz/pls/ps2017nss/" + str(n.find('a')['href'])
        # this finds only the first 'a' tag, not the one with X

        data = open_url(link)
        soup_unit = BS(data.text, 'html.parser')
        voter = soup_unit.find(headers='sa2')
        envelope = soup_unit.find(headers='sa3')
        votes_valid = soup_unit.find(headers='sa6')

        # collects and cleans list of parties, runs only 1x,
        # cleans also coma in the party name, which affects proper import to excel
        if run == 0:
            parties_names = soup_unit.find_all(headers=attr, class_="overflow_name")
            parties_names_changed_char = cycle_replace_character(parties_names, ch1="\xa0", ch2=" ")
            parties_names_changed_char2 = cycle_replace_direct(parties_names_changed_char, ch1=",", ch2=" ")
        run = +1

        # collects and cleans (through for loop) list of votes for parties for 1 city
        parties = soup_unit.find_all(headers=attr2, class_="cislo")
        party = cycle_replace_character(parties, ch1="\xa0", ch2="")

        # cleans the numbers from unwanted characters/strings
        voter1 = replace_character(voter, ch1="\xa0", ch2="")
        envelope1 = replace_character(envelope, ch1="\xa0", ch2="")
        votes_valid1 = replace_character(votes_valid, ch1="\xa0", ch2="")

        # makes a list of results for 1 city
        data_list = [n.text, c.text, voter1, envelope1, votes_valid1] + party

        # makes final  result - a list of lists of all cities
        data_all.append(data_list)

    header = ['code', 'location', 'registered', 'envelopes', 'valid'] + \
             parties_names_changed_char2

    # control print
    #    print(header)
    #    for c in data_all:
    #       print(c, sep="\n")

    # saving as csf file
    with open(output_file, mode="w", encoding='utf-8', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_all)
        print(f"UKLADAM DO SOUBORU: {output_file}")

    return


try:
    main()
except:
    print("Z duvodu chybneho zadani argumentu ukoncuji program")
    quit()
print(f"UKONCUJI Election_scraper")
print("--------------------------")
