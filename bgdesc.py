from ast import Str
from bs4 import BeautifulSoup
import requests
import re
from IPython import embed
#base website url
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

#find all background related information
array = soup.find_all('a',href=re.compile("background"))
length = len(array)-90 #change this back to -50 if all, 93 if only acolyte
isvariant = ["Investigator (SCAG)", "Investigator (VRGR)", "Spy", "Gladiator", "Guild Merchant", "Knight", "Pirate"]
hasvariant = ["City Watch", "Criminal", "Entertainer", "Guild Artisan", "Noble", "Sailor"]
notoc = ["Shipwright", "Smuggler"]
keywords = ["Features", "Variants", "Suggested Characteristics"]
#begin loop
i = 0
backgrounds = []
while i < length:
    units = array[i]
    refs = units['href']
    bgs = units.get_text() #this is background name/title
    if bgs in isvariant:
        i += 1
        continue
    #enters secondary url
    urlbgs = (url + refs) 
    reqbgs = requests.get(urlbgs)
    soupbgs = BeautifulSoup(reqbgs.text, "html.parser")

    #finds the correct text block background description 1
    textbgs = soupbgs.find(text=re.compile('Skill'))
    bgblock1 = textbgs.parent.parent
    bgs2 = bgblock1.get_text(strip=True)
    #
    #removes the hover text
    nohover = bgblock1.find_all(text=re.compile('Value:'))
    hovlen = len(nohover)
    i2 = 0
    while i2 < hovlen:
        hovunits = nohover[i2]
        hovunits.extract() #extract is broken for some reason...
        i2+=1
    
    #begin background description section 2 parsing
    toc0 = soupbgs.find(id=re.compile('toc0'))
    toc1 = soupbgs.find(id=re.compile('toc1'))
    toc2 = soupbgs.find(id=re.compile('toc2'))
    #######################################################
    toc0text = toc0.get_text()
    toc1text = toc1.get_text()
    toc2text = toc2.get_text()
    #######################################################
    toc0more = ""
    toc1more = ""
    toc2more = ""
    #######################################################
    toc0more2 = ""
    toc1more2 = ""
    toc2more2 = ""
    #######################################################
    if toc0text not in keywords:
        toc0more=(toc0.next_sibling.next_sibling.get_text(strip=True))
    else:
        toc1text = ""
        toc0more = ""
    if toc1text not in keywords:
        toc1more=(toc1.next_sibling.next_sibling.get_text(strip=True))
    else:
        toc1text = ""
        toc1more = ""
    if toc2text not in keywords:
        toc2more=(toc2.next_sibling.next_sibling.get_text(strip=True))
    else:
        toc2text = ""
        toc2more = ""
    ########################################################
    toc0more2=(toc0.next_sibling.next_sibling.next_sibling.get_text(strip=True))
    if toc0more2 in keywords:
        toc0more2 = ""
    toc1more2=(toc1.next_sibling.next_sibling.next_sibling.get_text(strip=True))
    if toc1more2 in keywords:
        toc1more2 = ""
    toc2more2=(toc2.next_sibling.next_sibling.next_sibling.get_text(strip=True))
    if toc2more2 in keywords:
        toc2more2 = ""
    #######################################################

    #
    fullbgdesc = (toc0text +" "+ toc0more +" "+ toc0more2 +" "+ toc1text +" "+ toc1more +" "+ toc1more2 +" "+ toc2text +" "+ toc2more  +" "+ toc2more2)
    backgrounds.append({
            'Background': bgs,
            'Proficiencies': bgs2,
            'Description': fullbgdesc,
    })
    #
    
    #print(bgs4)
    i += 1
print(backgrounds)



