from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/quote/SPY/'
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')

#Get specific information
price = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
change = soup.find('fin-streamer', {'class': "Fw(500) Pstart(8px) Fz(24px)"}).text
change_percent = soup.find_all('fin-streamer', {"class":"Fw(500) Pstart(8px) Fz(24px)"})[1].text
ticker = soup.find('h1',{'class':"D(ib) Fz(18px)"}).text

print(ticker, price, change, change_percent)


#Add list to get info on other stocks, input from user
#Create a dictionary, csv, json from data.