import requests
import coins_mercadobitcoin
import googlesheet

methods = ['ticker', 'orderbook', 'trades']


def api_criptos():
  result_criptos1 = []
  result_criptos2 = []
  result_criptos3 = []
  for coin in coins_mercadobitcoin.coins:
    url1 = f"https://www.mercadobitcoin.net/api/{coin}/{methods[0]}/"
    url2 = f"https://www.mercadobitcoin.net/api/{coin}/{methods[1]}/"
    url3 = f"https://www.mercadobitcoin.net/api/{coin}/{methods[2]}/"
    try:
      result_cripto1 = requests.get(url1).text
      result_criptos1.append(result_cripto1)
    except:
      None

    try:
      result_cripto2 = requests.get(url2).text
      result_criptos2.append(result_cripto2)
    except:
      None

    try:
      result_cripto3 = requests.get(url3).text
      result_criptos3.append(result_cripto3)
    except:
      None

  return googlesheet.writer(result_cripto1, result_cripto2, result_cripto3)
