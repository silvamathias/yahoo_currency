import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd 
import datetime as dt
from datetime import datetime as dtm
import os

pp = ['btc']
b3 = 0
n = len(pp)
local = os.getcwd()

if b3 == 1:
    for k in range(n):
        pp[k] += '.SA'

else:
    for k in range(n):
        pp[k] += '-USD'

hj = dtm.today()
ano = hj.year
mes = hj.month
dia = hj.day

#exemplo: para pegar dados dos últimos 5 anos (ano - 5); para últimos 5 mesês (mes - 5); para últimos 5 dias (dia - 5)
d_1 = dtm(ano-1, mes, dia)

#>>>>caso queira usar período inicial e final<<<<-------------------------------
#papeis = yf.download(pp,start = d_1, end = hj, group_by = 'ticker')
#-------------------------------------------------------------------------------

papeis = yf.download(pp,period = '30d', group_by = 'ticker')
n = 0
df = pd.DataFrame()
df.insert(n, pp[0], papeis['Adj Close'])

plt.plot(df.index,df[pp[0]])

medias = [2,3,4,5]
for m in medias:
    n += 1
    pp += ['media_' + str(m)]
    df.insert(n, 'media_' + str(m),  papeis['Adj Close'].rolling(m).mean())
    plt.plot(df.index,papeis['Adj Close'].rolling(m).mean())

print(df)
plt.legend(pp)
plt.show()