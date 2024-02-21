from bs4 import BeautifulSoup
import requests

stocks = []
collecting_tickers = True

while collecting_tickers:
    tickers = input('Please input the stock tickers you would like to track one at a time. When finished type "exit". ').upper()
    if tickers != "EXIT":
        stocks.append(tickers)
    else:
        collecting_tickers = False


for x in stocks:
    url = f'https://finance.yahoo.com/quote/{x}/'
    r = requests.get(url).text
    soup = BeautifulSoup(r,'html.parser')

    try:
        #Get specific information
        price = soup.find('fin-streamer', {'class': "Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
        change = soup.find('fin-streamer', {'class': "Fw(500) Pstart(8px) Fz(24px)"}).text
        change_percent = soup.find_all('fin-streamer', {"class":"Fw(500) Pstart(8px) Fz(24px)"})[1].text
        ticker = soup.find('h1',{'class':"D(ib) Fz(18px)"}).text

        print("\n",ticker, price, change, change_percent)

    except AttributeError:
        print("\n",f"{x} is not a valid ticker.")


