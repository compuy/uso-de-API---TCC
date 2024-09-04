from googlesheet import write_coins_to_spreadsheet
import apicoingekco

im = 5 #int(input("Informe o mês de início: "))
iy = 2023 #int(input("Informe o ano de início: "))
fm = 7 #int(input("Informe o mês final: "))
fy = 2023 #int(input("Informe o ano final: "))
initial_date = [im, iy]
final_date = [fm, fy]

coins = apicoingekco.date_coins(initial_date, final_date)

print(write_coins_to_spreadsheet(coins=coins, table="criptomoedas"))
