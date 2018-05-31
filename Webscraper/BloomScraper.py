import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import lxml

# specify the url
page = 'http://www.bloomberg.com/quote/SPX:IND'


# get the html page of the url declared
page = urllib.request.urlopen(page)
# parse the html using beautiful soup
soup = BeautifulSoup(page, 'lxml')

name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip() # strip is used to remove starting and trailing

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text

print(name, price)

# with open('index.csv', 'a') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([name, price, datetime.now()])