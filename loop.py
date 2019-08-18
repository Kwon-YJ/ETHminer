import pybithumb

def marketReader(currency, time):
    df = pybithumb.get_ohlcv(currency, time)
    ma15 = df['close'].rolling(window=15).mean()
    ma60 = df['close'].rolling(window=60).mean()
    last_ma15 = ma15[-2]
    last_ma60 = ma60[-2]
    if last_ma15 > last_ma60:
        return 1
    else:
        return 0

