import yfinance as yf


fpt_stock = yf.download("FPT.VN", start="2018-08-16", end="2024-08-16", interval="1d")[['Adj Close','Open', 'High', 'Low', 'Close', 'Volume']].round(2)
fpt_stock.to_csv("data/fpt_1d_20180816_20240816.csv")

print(fpt_stock)