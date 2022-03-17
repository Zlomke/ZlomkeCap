from bs4 import BeautifulSoup
import requests
import re
#base website url
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

#find all background related information
array = soup.find_all('a',href=re.compile("background"))
length = len(array)-3
isvariant = ["Investigator (SCAG)", "Investigator (VRGR)", "Spy", "Gladiator", "Guild Merchant", "Knight", "Pirate"]
#begin loop
i = 0
while i < length:
    units = array[i]
    refs = units['href']
    bgs = units.get_text() #this is background name/title
    if bgs in isvariant:
        i += 1
        continue
    #stop when it reaches black fist double agent, all backgrounds following are not ones I want to include, also too many edge cases
    if refs == "/background:black-fist-double-agent":
        i += 1
        break
    #I do not want to include this version
    for variant in isvariant:
        if variant == bgs:
            i += 1
            continue
    #prints name of background
    print(bgs)
    i += 1
