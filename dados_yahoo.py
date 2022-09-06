import yfinance as yf
import pandas as pd
import datetime as dt
from datetime import datetime as dtm
import os

pp = ['BTC-USD','ETH-USD','DOGE-USD','SHIB-USD','BRL=X','EURBRL=X','EUR=X']


B3 = 0
n = len(pp)

local = os.getcwd()

if B3 ==1:
    for k in range(n):
        pp[k] += '.SA'

#pp = ['^BVSP'] + sorted(pp)


#para pegar dados dos últimos 365 dias (ano - 1)---------------------------
hj = dtm.today()
ano = hj.year
mes = hj.month
dia = hj.day

d_1 = dtm(ano, mes-3, dia)
papeis = yf.download(pp,start = d_1, end = hj, group_by = 'ticker')
#--------------------------------------------------------------------------

#para pegar dados dos por período (1mo = 1 mes; 3mo = 3 meses; etc)--------
#papeis = yf.download(pp,period = '1mo', group_by = 'ticker')
#--------------------------------------------------------------------------


df_adj = pd.DataFrame()
n = 0
for papel in pp:
    df_adj.insert(n,papel, papeis[papel]['Adj Close'])
    n += 1

print('----valores\n')
print('-' * 70)
print(df_adj)
df_index = pd.DataFrame()

n=0
for papel in pp:
    df_index.insert(n, papel, (df_adj[papel] / df_adj[papel].shift(1))-1)
    n += 1

print('----index\n')
print('-' * 70)
print(df_index)
print('----correlação\n')
print('-' * 70)
print(df_index.corr())

df_adj.to_csv(local + '//df_adj.csv')
df_index.to_csv(local + '//df_index.csv')
