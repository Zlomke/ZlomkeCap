from asyncore import loop
from bs4 import BeautifulSoup
import requests
import re
#things
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#begin code)

#text = soup.get_text()
backgroundlinks = soup.find_all(href=re.compile("background"))
#print(backgroundlinks)


urlb = (url + "/background:acolyte")
#print(urlb)
reqb = requests.get(urlb)
soupb = BeautifulSoup(reqb.text, "html.parser")
text = soupb.find(text=re.compile("Skill"))
backgfeats = text.parent.parent

nohover2 = []
myrange = [1, 2, 3]
for nohover in myrange:
    nohover = backgfeats.find('span')
    nohover2 = nohover.find('span')
    nohover2.extract()

extext = backgfeats.find('span')
extext1 = extext.findChildren("span", recursive=false)
for child in extext1:
    child.extract()


backgfeattext = (backgfeats.get_text())
print(backgfeattext)

#li = soup.find('li', {'class': 'text'})
#children = li.findChildren("a" , recursive=False)
#for child in children:
#    print child


#for i in backgroundlinks:

#Acolyte

#go to http://dnd5e.wikidot.com/background:acolyte

#scrape Skill Proficiencies: Insight, Religion




#for btag in soup.find_all('a', attrs={'href': '/spells*'}):