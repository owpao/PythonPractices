import requests
from bs4 import BeautifulSoup
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")

titles = soup.find_all('p')
for o in titles:
    if(not o.string==None):
        print(o.string)
