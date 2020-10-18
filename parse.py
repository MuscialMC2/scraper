from html.parser import HTMLParser
import codecs
from bs4 import BeautifulSoup

file = codecs.open("saves/1028.html", "r", "utf-8")
# print(file.read())

soup = BeautifulSoup(file.read(), 'html.parser')
match = soup.findAll("img")
if len(match) > 0:
    for m in match:
        # imagelist.append(str(m))
        print(m)