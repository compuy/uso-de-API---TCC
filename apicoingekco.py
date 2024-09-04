import requests
import calendar
import coins_search
import datetime
from time import sleep


def date_coins(initial_date, final_date):
  dates = []
  month = initial_date[0]
  year = initial_date[1]
  while (year < final_date[1]) or (year == final_date[1] and month <= final_date[0]):
    day = calendar.monthrange(year, month)[1]
    dates.append(datetime.date(year, month, day).strftime('%d-%m-%Y'))
    if month < 12:
      month += 1
    else:
      month = 1
      year += 1
  return search(dates)


def search(dates):
  coin_cryptos = coins_search.coins
  coins_final = []
  for date in dates:
    cryptos = []
    print(f'Coletando dados do ano {date}...')
    for coin_crypto in coin_cryptos:
      print(f"Crypto - {coin_crypto}")
      try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_crypto}/history?date={date}&localization=pt"
        value = requests.get(url).json()['market_data']['current_price']['brl']
        crypto = {'coin': coin_crypto, 'value': value}
      except:
        crypto = {'coin': coin_crypto, 'value': None}
      cryptos.append(crypto)
      sleep(15)
    coin_final = {'date': date, 'cryptos': cryptos}
    coins_final.append(coin_final)
  return coins_final

