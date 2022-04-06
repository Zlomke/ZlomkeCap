from ast import Str
from bs4 import BeautifulSoup
import requests
import re
from IPython import embed
#base website url
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

racetocs = ["toc2","toc3","toc4","toc6","toc8","toc9","toc10","toc11","toc12",]
base_array = soup.find_all(id=racetocs)
race_div = soup.find(id="toc2").parent.parent
rough_race_list = race_div.select('p > a')
length = len(rough_race_list) #change back to -67 or no minus
i = 0
races = []
race_urls = []
race_info = []
while i < length:
    units = rough_race_list[i]
    refs = units['href']
    race_url = (url + refs)
    race_urls.append(race_url)
    races.append(units.get_text())
    req_races = requests.get(race_url)
    soup_in_race = BeautifulSoup(req_races.text, "html.parser")
    toc0 = soup_in_race.find(id="toc0").next_sibling.next_sibling
    toc0_lines = toc0.select('ul > li', recursive=False)
    race_info.append({
        'Race': units.get_text(),
        'Description': toc0_lines
    })
    i+=1
#print(races)
#print(race_urls)
print(race_info)