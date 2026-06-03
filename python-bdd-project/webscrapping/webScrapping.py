import requests
from bs4 import BeautifulSoup


data = requests.get("https://www.selenium.dev/")
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
SpecificData =soup.find('main',{'class':'td-main'})
print(SpecificData.prettify)

AllRows =  SpecificData.find_all('div')
print(AllRows)

for row in AllRows:
    