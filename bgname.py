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
#begin loop
i = 0
while i < length:
    units = array[i]
    refs = units['href']
    bgs = units.get_text() #this is background name/title

    #extract dissenter, causes issues because it is formatted differently and does not contain pertinent information
    if refs == "/background:dissenter":
        i += 1
        continue

    #prints name of background
    print(bgs)
    i += 1
