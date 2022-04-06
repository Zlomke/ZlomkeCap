from ast import Str
from bs4 import BeautifulSoup
import requests
import re
from IPython import embed
import pandas as pd
#base website url
url = "http://dnd5e.wikidot.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
classes =["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
#0 artificer
classes_array = []
class_unit = classes[0]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array.append(class_unit)
classes_array.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array.append(class_subrefs)
base_class = classes_array[1]
classes_array.pop(1)
classes_array.pop(0)


class_page_ref = (url + base_class)
class_req = requests.get(class_page_ref)
class_soup = BeautifulSoup(class_req.text, "html.parser")
classtable = class_soup.find(class_="wiki-content-table")


# Defining of the dataframe
df = pd.DataFrame(columns=['Level', 'Proficiency Bonus', 'Features', 'Infusions Known', 'Infused Items', 'Cantrips Known', '1st', '2nd', '3rd', '4th', '5th'])

# Collecting Data
for row in classtable.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        level = columns[0]
        prof_bonus = columns[1]
        features = columns[2]
        infusions = columns[3]
        infused_items = columns[4]
        cantrips = columns[5]
        first = columns[6]
        second = columns[7]
        third = columns[8]
        fourth = columns[9]
        fifth = columns[10]
        df = df.append({'Level': level,'Proficiency Bonus': prof_bonus, 'Features': features, 'Infusions Known': infusions, 'Infused Items': infused_items, 'Cantrips Known': cantrips, '1st': first, '2nd': second, '3rd': third, '4th': fourth, '5th': fifth}, ignore_index=True)

#print(df.head(20))

class_desc = class_soup.find(id="toc0").parent

table_element1 = class_desc.find(id="toc15")
table_element1.decompose()
table_element2 = class_desc.find_all('tr')
for element in table_element2:
    element.decompose()

print(class_desc.get_text())

#i = 0
#while len(classes_array) < i:
#    subclass_page_ref = (url + classes_array[i])
#    subclass_req = requests.get(subclass_page_ref)
#    subclass_soup = BeautifulSoup(subclass_req.text, "html.parser")
#    i+=1