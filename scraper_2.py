from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
import time


url = urllib.request.urlopen('https://www.utas.edu.au/about/campuses/cradle-coast').read()
# time.sleep(10)
soup = BeautifulSoup(url, "html5lib")

featuredLocation = [] #list of locations

ul = soup.find_all('a', attrs={'class':'content-tabs__link'})

# a_tag = ul.find_all('a', attrs={'class':'content-tabs__link'})

# print(ul.text)


file = open("cradle-coast_location.txt", "w")

for atext in ul:
    strtext = str(atext.text)
    print(strtext)
    file.write(strtext+'\n')
    file.flush()
    file.close

# file = open("webdata.txt", "w")

# for atext in a_tag:
#     strtext = str(atext.text)
#     print(strtext)
#     file.write(strtext+'\n')
#     file.flush()
#     file.close