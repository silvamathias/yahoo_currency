import yfinance as yf
import pandas as pd
import datetime as dt
from datetime import datetime as dtm
import os

#pp = ['ITUB3', 'ITUB4', 'ITSA3', 'ITSA4', '^BVSP']
pp = ['BTC-USD','ETH-USD','SHIB-USD','DOGE-USD','ADA-USD','XRP-USD','MATIC-USD','SOL-USD','CRO-USD','MANA-USD','LRC-USD','^BVSP']

B3 = 0
n = len(pp)

local = os.getcwd()

if B3 ==1:
    for k in range(n-1):
        pp[k] += '.SA'

print(pp)
hj = dtm.today()
ano = hj.year
mes = hj.month
dia = hj.day

d_1 = dtm(ano-1, mes, dia)
#para pegar dados dos últimos 365 dias-------------------------------------
#papeis = yf.download(pp,start = d_1, end = hj, group_by = 'ticker')
#--------------------------------------------------------------------------

papeis = yf.download(pp,period = '1mo', group_by = 'ticker')


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
