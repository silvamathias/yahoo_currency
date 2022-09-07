import numpy as np
import pandas as pd
import dbpg as db
import os
import ipdb
import matplotlib.pyplot as plt

def tx_dia(tx_ano):
    '''retorna a taxa diária referente à taxa anual informada'''
    try:
        txd = ((1 + tx_ano)**(1/252)) - 1
        return txd
    except:
        return 'Não foi possível calcular a taxa diária com o que foi informado'

def tx_ano(tx_dia):
    '''retorna a taxa anual referente à taxa diária informada'''
    try:
        txd = ((1 + tx_dia)**(252)) - 1
        return txd
    except:
        return 'Não foi possível calcular a taxa diária com o que foi informado'


dir1 = os.getcwd()

SELIC = 0.1375

df = pd.read_csv(dir1 + '//df_index.csv')
lista_cur = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'SHIB-USD']
#df = df.drop(columns = ['EURBRL=X','BRL=X','EUR=X'])
df = df[lista_cur]
print(df)
print('\n---descrições\n')
print('-' * 70)
prop = (0.27, 0.40, 0.13, 0.20)
prop = np.array(prop)
print(prop)
print('\n---descrições')
print('-' * 70)
print(df.describe())
print('\n---correlação')
print('-' * 70)
corr = df.corr()
print(corr)
print('\n---Retorno esperado de cada ação(média)')
print('-' * 70)

med = df[lista_cur].mean()
media = np.array(med)
print(media)
print('\n---Risco de cada ação (Desvio padrão)')
print('-' * 70)
std = df[lista_cur].std()
desvpad=np.array(std)

#multiplique o desvio padrão de cada ação pelo
print(desvpad)
desvpad = desvpad * prop
print('\n---Multiplicação: A X Bcorrelação X desvio padrão')
print('-' * 70)
mult=np.dot(corr,desvpad)
print(mult)
print('\n---Multiplicação pela transposta do desvio padrão')
print('-' * 70)
risco=np.dot(mult,np.transpose(desvpad))

risco = np.exp(risco) - 1
media_exp = np.exp(media) -1
media_exp = np.array(media_exp)
print('Risco carteira diário: ' + str(risco))
print('\n---Retorno esperado carteira(retorno por ação * proporção)')
print('-' * 70)
ret_c = np.sum(media_exp * prop)
print(ret_c)
print('\n---taxa livre de risco(SELIC)')
print('-' * 70)
SELIC_ad = tx_dia(SELIC)
print(SELIC)

print('\n---Índice de sharpe da carteira')
print('-' * 70)
sp = (ret_c - SELIC_ad) / risco
print(sp)