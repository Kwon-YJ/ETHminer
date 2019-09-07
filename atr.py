import pybithumb, ohlcv

currency = "BTC"
interval = "minute"



def getATR(currency, interval):
    df = ohlcv.get_ohlcv(currency, interval)
    close = df['close'][-15:-1]
    high = df['high'][-15:-1]
    low = df['low'][-15:-1]
    
    TRs = []
    TRs.append(high[0]-low[0])
    for i in range(1,14):
        TRs.append(max(abs(high[i]-low[i]), abs(high[i]-close[i-1]), abs(low[i]-close[i-1])))
    return sum(TRs) / len(TRs)
    

print(getATR(currency, interval))