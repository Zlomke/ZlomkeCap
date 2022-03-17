from bs4 import BeautifulSoup
import requests
import re
from IPython import embed
#base website url
url = "http://dnd5e.wikidot.com"

# Acolyte Example
res = requests.get(f'{url}/background:acolyte')

# Let's make more use of the css select functionality in bs4
soup = BeautifulSoup(res.text, "html.parser")

# bs4 CSS Selectors docs
# https://beautiful-soup-4.readthedocs.io/en/latest/#css-selectors
table_of_contents_refs = soup.select('#toc-list > div > a')

# Going to create a list of feature dicts
features = []

# Each ref in the Table of Contents div
for ref in table_of_contents_refs:
    print(ref)

    # Get the value of the ref attribute
    # This will be the element id of the
    # section header
    element_id = ref['href']
    element = soup.select(element_id)[0]

    # This is SUPPOSED to break on Suggested Characteristics
    # and it does, but what we do next is buggy and needs some
    # more thought because when you get all siblings that are
    # <p> elements it doesn't stop before the next <h2>, so
    # the content of Suggested Characteristics still gets included
    # Should be easy-ish to fix; I'm just trying to hustle through this
    if element.text == 'Suggested Characteristics':
        break

    if element.text != 'Features':
        r = element.find_next_siblings('p')

        # Combine the <p> element siblings we just queried
        # Don't be freaked out about the list comprehension
        # it's just a shorthand for loop
        detail = ' '.join([x.get_text() for x in r])

        # Add the feature name and detail to the features list
        features.append({
            'feature': element.text,
            'detail': detail
        })

print(features)

