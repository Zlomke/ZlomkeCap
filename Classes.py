from ast import Str
from bs4 import BeautifulSoup
import requests
import re
from IPython import embed
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

#1 barbarian
classes_array1 = []
class_unit = classes[1]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array1.append(class_unit)
classes_array1.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array1.append(class_subrefs)
#2 bard
classes_array2 = []
class_unit = classes[2]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array2.append(class_unit)
classes_array2.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array2.append(class_subrefs)
#3 cleric
classes_array3 = []
class_unit = classes[3]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array3.append(class_unit)
classes_array3.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array3.append(class_subrefs)
#4 druid
classes_array4 = []
class_unit = classes[4]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array4.append(class_unit)
classes_array4.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array4.append(class_subrefs)

#5 fighter
classes_array5 = []
class_unit = classes[5]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array5.append(class_unit)
classes_array5.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array5.append(class_subrefs)

#6 monk
classes_array6 = []
class_unit = classes[6]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array6.append(class_unit)
classes_array6.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array6.append(class_subrefs)
#7 paladin
classes_array7 = []
class_unit = classes[7]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array7.append(class_unit)
classes_array7.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array7.append(class_subrefs)
#8 ranger
classes_array8 = []
class_unit = classes[8]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array8.append(class_unit)
classes_array8.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array8.append(class_subrefs)
#9 rogue
classes_array9 = []
class_unit = classes[9]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array9.append(class_unit)
classes_array9.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array9.append(class_subrefs)
#10 sorcerer
classes_array10 = []
class_unit = classes[10]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array10.append(class_unit)
classes_array10.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array10.append(class_subrefs)
#11 warlock
classes_array11 = []
class_unit = classes[11]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array11.append(class_unit)
classes_array11.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array11.append(class_subrefs)
#12 wizard
classes_array12 = []
class_unit = classes[12]
classref = soup.find(text=class_unit).parent['href']
class_subarray = soup.find(text=class_unit).parent.parent.parent.parent.parent.next_sibling.next_sibling.find(class_="col-sm-4").find_all('a')
classes_array12.append(class_unit)
classes_array12.append(classref)
for class_rough_refs in class_subarray:
    class_subrefs = class_rough_refs['href']
    classes_array12.append(class_subrefs)

class_ref_lists = [classes_array, classes_array1, classes_array2, classes_array3, classes_array4, classes_array5, classes_array6, classes_array7, classes_array8, classes_array9, classes_array10, classes_array11, classes_array12]
for class_refs in class_ref_lists:
    print(class_refs)
