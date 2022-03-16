from tabulate import tabulate
import asyncio
from tokenize import String
from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import json
import pandas as pd
from prettytable import PrettyTable as pt
#things
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
hrefb = "/background:acolyte"
#begin code


# ******************** This code works, pulls up a text list of every background and its description
myfile = open("C:/Users/Learner/Desktop/Cole Zlomke/backgrounds.txt", "w")
a_dictionary = {"a" : 1, "b" : 2}
array = soup.find_all('a',href=re.compile("background"))
length = len(array)-3
i = 0
while i < length:
    units = array[i]
    refs = units['href']
    bgs = units.get_text()
    #extract dissenter
    if refs == "/background:dissenter":
        i += 1
        continue
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
    #prints to file
    myfile.write(bgs + "\n")
    myfile.write(str(bgs2) + "\n")
    
    i += 1
myfile.close()
# ******************************************



#/////////////////////////////////////////////////////////////////////////////////////////////
#redo soup for the specific backg url
#urlbgs = (url + hrefb) 
#reqbgs = requests.get(urlbgs)
#soupbgs = BeautifulSoup(reqbgs.text, "html.parser")
#finds the correct text block
#textbgs = soupbgs.find(text=re.compile('Skill'))
#bgblock1 = textbgs.parent.parent
#removes the hover text
#nohover = bgblock1.find('span').find('span')
#nohover2 = bgblock1.find('span').next_sibling.next_sibling.find('span')
#nohover3 = bgblock1.find('span').next_sibling.next_sibling.next_sibling.next_sibling.find('span')
#nohover.extract()
#nohover2.extract()
#nohover3.extract()
#prints
#print(bgblock1.text)
#//////////////

#backgfeats = textbgs.parent
#nohover = backgfeats.find('span')
#nohover2 = nohover.find('span')
#nohovera = nohover2.parent.next_sibling.next_sibling.span
#nohoverb = nohover2.parent.next_sibling.next_sibling.next_sibling.next_sibling.span
#print(nohoverb)

#//////////
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