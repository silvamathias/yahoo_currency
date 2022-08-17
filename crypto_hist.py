import yfinance as yf
import pandas as pd
import numpy as np
import os
import datetime
import time as tm

col = ['date_time', 'ticker', 'vlr']
currency_list = ['BTC-USD','ETH-USD','DOGE-USD','SHIB-USD','BRL=X','EURBRL=X','EUR=X']

local = os.getcwd() + '//'

k = 0
while k == 0:
    dados = []
    hj = datetime.datetime.now()
    for cur in currency_list:
        ticker = yf.Ticker(cur)
        vlr = ticker.history(period='1d')
        dado = []
        dado.append(str(hj))
        dado.append(cur)
        dado.append(vlr['Close'][0])
        dados += [dado]
        df = pd.DataFrame(np.array(dados), columns = col)
#
    df.to_csv(local + 'base_cur.csv', index = False, header = False, mode = 'a')
    tm.sleep(57)
