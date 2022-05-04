from bs4 import BeautifulSoup
import requests
#things
url = "http://dnd5e.wikidot.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
#begin code



thing = soup.find_all('a')
 for stuff = thing.find(class_="col-md-7")
print(stuff)