import pybithumb, time
#----------------------------------
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
#최종적으로는, 현재가격이 15일 이평선보다 1ATR만큼 아래일 때
def belowline(currency, interval):
    priceNow = pybithumb.get_current_price(currency)
    df = pybithumb.get_ohlcv(currency, interval)
    ma60 = df['close'].rolling(window=60).mean()
    if priceNow <= ma60:
        return 1
    else:
        return 0
    

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