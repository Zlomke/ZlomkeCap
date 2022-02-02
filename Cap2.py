from asyncore import loop
from bs4 import BeautifulSoup
import requests
import re
#things
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#begin code

#print a list of all hrefs, or all text labels of each background
backgroundlinks = soup.find_all('a', re.compile("background"))
print(backgroundlinks)
#/////////////////////////////////////////////////////////////////////////////////////////////
#looping the link finding
#for bglinks in soup.find_all('a', href=re.compile("background")):
#    urlbgs = (url + bglinks['href'])
#    reqbgs = requests.get(urlbgs)
#    
#    soupbgs = BeautifulSoup(reqbgs.text, "html.parser")
#    textbgs = soupbgs.find(textbgs=re.compile("Skill"))
#    backgfeats = textbgs.parent
#    nohover = backgfeats.find('span')
#    nohover2 = nohover.find('span')
#    nohovera = nohover2.parent.next_sibling.next_sibling.span
#    nohoverb = nohover2.parent.next_sibling.next_sibling.next_sibling.next_sibling.span

#urlb = (url + "/background:acolyte")
#print(urlb)
#reqb = requests.get(urlb)
#soupb = BeautifulSoup(reqb.text, "html.parser")
#text = soupb.find(text=re.compile("Skill"))
#backgfeats = text.parent.parent

#print out the text result, the features on the background page
#backgfeattext = (backgfeats.get_text())
#print(backgfeattext)
#print(soupbgs)
#/////////////////////////////////////////////////////////////////////////////////////////////
#bgcounter = 0
#urlall = 0

#while x < len(backgroundlinks):
#    
#    x = x+1


#nohover = backgfeats.find('span')
#nohover2 = nohover.find('span')
#nohovera = nohover2.parent.next_sibling.next_sibling.span
#nohoverb = nohover2.parent.next_sibling.next_sibling.next_sibling.next_sibling.span
#deletehover = nohover2 + nohovera+ nohoverb
#deletehover.replace_with("")
#type(nohovera)
#counter = 0
#while counter != 4:
#  nohover2.extract()
#  counter += 1
#else:
#    print("no more")

#extext = backgfeats.find('span')
#extext1 = extext.findChildren("span", recursive=False)
#for child in extext1:
#    child.extract()




#li = soup.find('li', {'class': 'text'})
#children = li.findChildren("a" , recursive=False)
#for child in children:
#    print child


#for i in backgroundlinks:

#Acolyte

#go to http://dnd5e.wikidot.com/background:acolyte

#scrape Skill Proficiencies: Insight, Religion




#for btag in soup.find_all('a', attrs={'href': '/spells*'}):