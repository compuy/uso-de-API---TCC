import yfinance as yf
import gspread
from google.oauth2 import service_account

json_file = "project-to-web-scraping-e782cbd91f6b.json"

def finances(initial_date, final_date):
    tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "ABEV3.SA", "BBDC3.SA", "KNIP11.SA", "KNCR11.SA", "KNRI11.SA", "HGLG11.SA", "IRDM11.SA", "AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
    date = f'{initial_date[1]}-{initial_date[0]}-01'
    end_date = f'{final_date[1]}-{final_date[0]}-01'

    dados = yf.download(tickers, start=date, end=end_date)["Close"]
    dados = dados.resample('M').last()
    return dados


def login(json_file, scopes):
    credentials = service_account.Credentials.from_service_account_file(
      json_file)
    scoped_credentials = credentials.with_scopes(scopes)
    google_client = gspread.authorize(scoped_credentials)
    return google_client


def write_investimentos_to_spreadsheet(coins, table, json_file=json_file):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    try:
        google_client = login(json_file, scopes)
        worksheet = google_client.open('tcc-api').worksheet(table)

        # Reset the index and rename the index column
        coins = coins.reset_index()
        coins = coins.rename(columns={'index': 'date'})

        # Convert the date column to strings
        coins['Date'] = coins['Date'].dt.strftime('%d-%m-%Y')

        # Clear the worksheet
        worksheet.clear()
        coins = coins.astype(str)
        
        # Append the column names
        worksheet.append_row(coins.columns.tolist())

        # Append the data
        worksheet.insert_rows(coins.values.tolist(), 2)

        return print("Planilha atualizada com sucesso.")
    
    except Exception as e:
        return print(f"Erro ao atualizar planilha: {str(e)}")


im = str(input("Informe o mês de início: "))
iy = str(input("Informe o ano de início: "))
fm = str(input("Informe o mês final: "))
fy = str(input("Informe o ano final: "))

initial_date = [im, iy]
final_date = [fm, fy]

investimentos = finances(initial_date, final_date)

write_investimentos_to_spreadsheet(coins=investimentos, table="investimentos")