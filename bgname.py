from tokenize import String
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

    #enters secondary url
    urlbgs = (url + refs) 
    reqbgs = requests.get(urlbgs)
    soupbgs = BeautifulSoup(reqbgs.text, "html.parser")

    #finds the correct text block
    textbgs = soupbgs.find(text=re.compile('Skill'))
    bgblock1 = textbgs.parent.parent
    bgs2 = bgblock1.get_text()

    #removes the hover text
    nohover = bgblock1.find_all(text=re.compile('Value:'))
    hovlen = len(nohover)
    i2 = 0
    while i2 < hovlen:
        hovunits = nohover[i2]
        hovunits.extract()
        i2=i2+1
    
    #prints name of background
    #print(bgs)
    #prints background description 1
    print(bgs2)
    i += 1
