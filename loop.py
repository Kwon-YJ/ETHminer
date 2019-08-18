import pybithumb, time
#----------------------------------
#15이평선이 60이평선 보다 높을 때
def marketReader(currency, interval):
    df = pybithumb.get_ohlcv(currency, interval)
    ma15 = df['close'].rolling(window=15).mean()
    ma60 = df['close'].rolling(window=60).mean()
    last_ma15 = ma15[-2]
    last_ma60 = ma60[-2]
    print(last_ma15, last_ma60)
    if last_ma15 > last_ma60:
        return 1
    else:
        return 0

def aboveline(currency, interval):
    priceNow = pybithumb.get_current_price(currency)
    df = pybithumb.get_ohlcv(currency, interval)
    ma15 = df['close'].rolling(window=15).mean()
    if priceNow > ma15:
        return 1
    else:
        return 0
#최종적으로는, 현재가격이 15일 이평선보다 1ATR만큼 아래일 때, 추가해야할것 : 현재 atr을 구해서 이평선에서 빼준다. 그값을 프라이스나우와 비교.
def belowline(currency, interval):
    priceNow = pybithumb.get_current_price(currency)
    df = pybithumb.get_ohlcv(currency, interval)
    ma60 = df['close'].rolling(window=60).mean()
    atr = getATR(currency, interval)
    if priceNow <= ma60 - atr:
        return 1
    else:
        return 0

def getATR(currency, interval):
    df = pybithumb.get_ohlcv(currency, interval)
    close = df['close'][-15:-1]
    high = df['high'][-15:-1]
    low = df['low'][-15:-1]
    
    TRs = []
    TRs.append(high[0]-low[0])
    for i in range(1,14):
        TRs.append(max(abs(high[i]-low[i]), abs(high[i]-close[i-1]), abs(low[i]-close[i-1])))
    return sum(TRs) / len(TRs)

def buy(currency, units):
    print("buy")
    pass

def sell(currency, units):
    print("sell")
    pass


#---------------FIELDS-------------
currency = "BTC"
interval = "minute"
positioned = False
con_key = ""
sec_key = ""
balance = 0
buy_price = 0
#----------------------------------
while True:
    if marketReader(currency, interval) and positioned == False:
        buy(currency, 50)
        positioned = True
        

    elif positioned == True and (belowline==1):
        sell(currency, 50)
        positioned = False
    print('tiktok...' , end='')
    time.sleep(1)
    #test