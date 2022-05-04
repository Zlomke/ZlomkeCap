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
        df = df.append({'Level': level,'Proficiency Bonus': prof_bonus, 'Features': features, 'Infusions Known': infusions, 'Infused Items': infused_items, 
        'Cantrips Known': cantrips, '1st': first, '2nd': second, '3rd': third, '4th': fourth, '5th': fifth}, ignore_index=True)
#####

class_desc = class_soup.find(id="toc0").parent
table_element1 = class_desc.find(id="toc15")
table_element1.decompose()
table_element2 = class_desc.find_all('tr')
for element in table_element2:
    element.decompose()

#####

###Pre-Loop Setup
i = 0
subclass_info = []
while i < len(classes_array)-3:###This is -3 to see one or no minus
    ###Loop Setup
    subclass_unit = classes_array[i]
    subclass_req = requests.get(url + subclass_unit)
    subclass_soup = BeautifulSoup(subclass_req.text, "html.parser")
    ###Finding Body HTML
    subclass_desc = subclass_soup.find(id="toc0").parent
    ###Finding Tables
    wanted_tables = subclass_desc.find_all(class_="wiki-content-table")
    ###Pre-Loop Setup
    i2 = 0
    while i2 < len(wanted_tables):
        ###Loop Setup
        table_units = wanted_tables[i2]
        table_headers = table_units.find_all('th')
        table_headers.pop(0)
        table_headers_text = []
        for table_header_units in table_headers:
            table_headers_text.append(table_header_units.get_text())
        df2 = pd.DataFrame()
        for row2 in table_units.find_all('tr'):    
            ###Find all data for each column
            columns = row2.find_all('td')
            i_increase = len(table_headers_text)
            ###Defines Columns
            if(columns != []):
                i3 = 0
                i4 = 1
                if (i_increase >= 3):
                    i5 = 2
                
                while i3 < len(table_headers_text):
                    df2 = df2.append({
                        table_headers_text[i3] : columns[i3],
                        table_headers_text[i4] : columns[i4]
                        }, ignore_index=True)
                    i3+=i_increase
        i2+=1
    ###Append All Info To Array Per Subclass
    subclass_info.append({
        subclass_unit : subclass_desc,
    })
    i+=1

###Test Prints
print(df2.head(20))

###Class Level Table
#print(df.head(20))

###Class Text Description
#print(class_desc.get_text())

###Subclass Final Array
#print(subclass_info)
