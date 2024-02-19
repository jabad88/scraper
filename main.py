from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/quote/GOOG/'
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')

price = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text

print (price)

#Add functionality to get ticker, PE ration, etc.
#Use a list to get data of other stocks