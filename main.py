from googlesheet import write_coins_to_spreadsheet
import apicoingekco

im = int(input("Informe o mês de início: "))
iy = int(input("Informe o ano de início: "))
fm = int(input("Informe o mês final: "))
fy = int(input("Informe o ano final: "))
initial_date = [im, iy]
final_date = [fm, fy]

coins = apicoingekco.date_coins(initial_date, final_date)

print(write_coins_to_spreadsheet(coins))
