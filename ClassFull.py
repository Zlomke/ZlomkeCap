from asyncore import loop
from os import remove
from tracemalloc import start
from bs4 import BeautifulSoup
import requests
import pandas as pd
#things
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
classes =["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
#

i = 0
t=0
while i < len(classes)-12:
    full_class = []
    class_page_ref = (url + "/" + classes[i])
    class_soup = BeautifulSoup(requests.get(class_page_ref).text, "html.parser")
    starting_paragraph = class_soup.find(id="page-content").p
    full_class.append(starting_paragraph)
    i2 = 0
    while i2 == 0:
        if starting_paragraph.__class__ == "feature":
            starting_paragraph = starting_paragraph.div.h1
            continue
        if starting_paragraph.__class__ == "wiki-content-table":
            good_table = pd.read_html(requests.get(class_page_ref).text)[t]
            t+=1
            full_class.append(good_table)
        if len(starting_paragraph.find_next_siblings()) == 1:
            starting_paragraph = starting_paragraph.next_sibling
            full_class.append(starting_paragraph.get_text())
            i2+=1
            continue
        starting_paragraph = starting_paragraph.next_sibling
        full_class.append(starting_paragraph.get_text())
    i+=1
print(full_class)