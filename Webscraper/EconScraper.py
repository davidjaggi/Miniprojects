from bs4 import BeautifulSoup
import requests
import lxml

pages = ['currencies','stocks','commodities','bonds']
tabels = ['FX','']

def requestor(page):
    request = requests.get(f'https://tradingeconomics.com/{page}')
    return request

currencies = requestor(pages[0])

soup = BeautifulSoup(currencies.content, 'lxml')
currencies = soup.find_all('div',class_ = 'table-responsive')

for currency in currencies:
    currency.find_all('td')
