import pyRofex

print("---------------------------")
print("Iniciando sesion en Remarkets")
pyRofex.initialize(
    user = "agupala5130",
    password = "nzdhbT0+",
    account = "REM5130",
    environment = pyRofex.Environment.REMARKET
)
print("Consultando simbolo")
md = pyRofex.get_market_data(
    ticker = "DOOct20",
    entries = [
        pyRofex.MarketDataEntry.BIDS,
        pyRofex.MarketDataEntry.LAST
    ]
)
print(md)