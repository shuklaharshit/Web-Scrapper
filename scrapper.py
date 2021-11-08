from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
import time


url = urllib.request.urlopen('https://www.utas.edu.au/about/campuses').read()
# time.sleep(10)
soup = BeautifulSoup(url, "lxml")
type(soup)

#printing page source 100 char in console
#print(soup.prettify()[:100])

# for link in soup.find_all('a'):
#     print(link.get('href'))


# it will print all text from webpage
# print(soup.get_text())


# it will print all link in console
# for link in soup.find_all('a', attrs=({'href': re.compile("^http")})):
#     print(link)

file = open("parsed_data.txt", "w")
for link in soup.find_all('a', attrs=({'href': re.compile("^http")})):
    soup_link= str(link)
    print(soup_link)
    file.write(soup_link+'\n')
    file.flush()
    file.close