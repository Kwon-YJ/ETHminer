import pyupbit, time
#----------------------------------
def getATR(currency, interval):
    df = pyupbit.get_ohlcv(currency, interval)
    close = df['close'][-15:-1]
    high = df['high'][-15:-1]
    low = df['low'][-15:-1]
    
    TRs = []
    TRs.append(high[0]-low[0])
    for i in range(1,14):
        TRs.append(max(abs(high[i]-low[i]), abs(high[i]-close[i-1]), abs(low[i]-close[i-1])))
    return sum(TRs) / len(TRs)

#15이평선이 60이평선 보다 atr 만큼 높을 때
def marketReader(currency, interval):# 2요청
    df = pyupbit.get_ohlcv(currency, interval)
    #print('hi')
    #print(df)
    ma2 = df['close'].rolling(window=2).mean()
    ma20 = df['close'].rolling(window=20).mean()
    cur_price = pyupbit.get_current_price(currency)
    last_ma20 = ma20[-2]
    atr = getATR(currency, interval)
    print( "ma2 = {} and ma20 = {} and atr = {}".format(cur_price, last_ma20, atr))
    #print(last_ma2, last_ma20)
    if cur_price > last_ma20:# + atr:
        return 1
    else:
        return 0

def aboveline(currency, interval):
    priceNow = pyupbit.get_current_price(currency)
    df = pyupbit.get_ohlcv(currency, interval)
    ma20 = df['close'].rolling(window=20).mean()
    if priceNow > ma20:
        return 1
    else:
        return 0
#최종적으로는, 현재가격이 15일 이평선보다 1ATR만큼 아래일 때, 추가해야할것 : 현재 atr을 구해서 이평선에서 빼준다. 그값을 프라이스나우와 비교.
def belowline(currency, interval):
    priceNow = pyupbit.get_current_price(currency)
    df = pyupbit.get_ohlcv(currency, interval)
    ma60 = df['close'].rolling(window=60).mean()
    atr = getATR(currency, interval)
    if priceNow <= ma60 - atr:
        return 1
    else:
        return 0



def buy(currency, units):
    print("buy")
    

def sell(currency, units):
    print("sell")
    


#---------------FIELDS-------------
currency = "KRW-TSHP"
interval = "minute1"
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
        

    elif positioned == True and (aboveline == 0):
        sell(currency, 50)
        positioned = False
    print('tiktok...' , end='')
    time.sleep(5)
    #test