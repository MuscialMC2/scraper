from html.parser import HTMLParser
import codecs
from bs4 import BeautifulSoup

file = codecs.open("saves/ibdb/1028.html", "r", "utf-8")

soup = BeautifulSoup(file.read(), 'html.parser')

title = soup.find("h3", class_="title-label")
if (title):
    print(title.string)

# opening = ''
# closing = ''
# performances = ''
# productionStaff = ''
# songs = [] #id="Songs"

songsWrapper = soup.find("div", id="Songs")
print(songsWrapper)

songsSoup = BeautifulSoup(songsWrapper, 'html.parser')
songsWrapperFirstChild = songsSoup.find_all('div')

# print(songsWrapperFirstChild)


# if len(songsWrapper) > 0:
#     songsSoup = BeautifulSoup(songsWrapper, 'html.parser')
#     # songs = songsSoup.div
#     print(songsSoup)
#     for m in match:
#         # imagelist.append(str(m))
#         print(m)