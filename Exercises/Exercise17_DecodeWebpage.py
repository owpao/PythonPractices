# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)

titles = soup.find_all('h2', 'css-6h3ud0 esl82me2')
counter = int(1)
for o in titles:
    print("Article {0}: {1}".format(counter, o.string,))
    counter += 1
