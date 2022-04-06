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
text = soupb.get_text()
print(text)

#for i in backgroundlinks:

#Acolyte

#go to http://dnd5e.wikidot.com/background:acolyte

#scrape Skill Proficiencies: Insight, Religion




#for btag in soup.find_all('a', attrs={'href': '/spells*'}):