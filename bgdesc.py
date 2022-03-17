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
length = len(array)-3
isvariant = ["Investigator (SCAG)", "Investigator (VRGR)", "Spy", "Gladiator", "Guild Merchant", "Knight", "Pirate"]
hasvariant = ["City Watch", "Criminal", "Entertainer", "Guild Artisan", "Noble", "Sailor"]
notoc = ["Shipwright", "Smuggler"]
keywords = ["Features", "Variants"]
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
    #enters secondary url
    urlbgs = (url + refs) 
    reqbgs = requests.get(urlbgs)
    soupbgs = BeautifulSoup(reqbgs.text, "html.parser")

    #finds the correct text block background description 1
    textbgs = soupbgs.find(text=re.compile('Skill'))
    bgblock1 = textbgs.parent.parent
    bgs2 = bgblock1.get_text()

    #removes the hover text
    nohover = bgblock1.find_all(text=re.compile('Value:'))
    hovlen = len(nohover)
    i2 = 0
    while i2 < hovlen:
        hovunits = nohover[i2]
        hovunits.extract() #extract is broken for some reason...
        i2+=1
    
    #begin background description section 2 parsing
    print(bgs)
    #print(bgs2)
    toc0 = soupbgs.find(id=re.compile('toc0'))
    toc1 = soupbgs.find(id=re.compile('toc1'))
    toc2 = soupbgs.find(id=re.compile('toc2'))
    print(toc0.get_text())

    if toc0.get_text() not in keywords:
        print(toc0.next_sibling.next_sibling.get_text())
    
    print(toc1.get_text())
    print(toc1.find_next_sibling('p').get_text())
    toc1check = toc1.find_next_sibling('p').next_sibling.next_sibling.get_text()
    if toc1check != 'Suggested Characteristics':
        print(toc1check)
    if toc2.get_text() == 'Suggested Characteristics':
        i+=1
        continue
    print(toc2.get_text())

    #print(bgs4)
    i += 1



