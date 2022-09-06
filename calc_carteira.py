import numpy as np
import pandas as pd
import dbpg as db
import os
#from openpyxl import Workbook
#from openpyxl import load_workbook
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
#base = db.pandas_query("select * from tb_ln_adj_fech where data >= '2017-05-10' and data < '2020-01-01' order by data;")
base = pd.read_excel(dir1 + '\..' + '\carteira_pos_petz.xlsx')
#df = base()
df = base
#print(df)
df.to_csv(dir1 + '/teste_carteira.csv')
#df = df.drop(columns = ['mes_ano', 'mes', 'ano', 'data', 'bvsp_ln_adj_fechamento'])
df = df.drop(columns = ['DT','BVSP'])
print(df)
print('\n---descrições\n')
print('-' * 70)
prop = (0.3448162366582, 0.0819713602615, 0.0185932856427, 0.0023270212108, 0.1196585200066, 0.1653550951056, 0.0684733500113, 0.0781275560181, 0.1206775750851)
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
med = df.mean()
media = np.array(med)
print(media)
print('\n---Risco de cada ação (Desvio padrão)')
print('-' * 70)
std = df.std()
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
print('\n---taxa livre de risco(IPCA)')
print('-' * 70)
IPCA = tx_dia(0.0725)
print(IPCA)
#print('Risco carteira anual: ' + str(tx_ano(risco))
print('\n---Índice de sharpe da carteira')
print('-' * 70)
sp = (ret_c - IPCA) / risco
print(sp)

'''

=(N22-N21)/N23
#gráficos atualizados set2021
lg=[]
for n in df.columns:
    #if '_adj_fechamento' in n:
    if n.replace('_adj_fechamento','') in ('oibr3'):
        plt.plot(df.data,df[n])
        lg = lg + [n.replace('_adj_fechamento','')]
plt.legend(lg)

plt.show()
#-
'''
'''
ibov = df.bvsp_ln_adj_fechamento
vale3 = df.vale3_ln_adj_fechamento
itsa3 = df.itsa3_ln_adj_fechamento
bbdc3 = df.bbdc3_ln_adj_fechamento
oibr3 = df.oibr3_ln_adj_fechamento
taee4 = df.taee4_ln_adj_fechamento
petr4 = df.petr4_ln_adj_fechamento
plt.plot(ibov)
plt.plot(vale3)
plt.plot(itsa3)
#plt.show()

plt.plot()
plt.plot(ibov)
plt.plot(ibov)
plt.plot(ibov)
plt.plot(ibov)
'''
'''
tb_cod = pd.read_table('listados_b3.txt',';')

s = 'SeriesPgre/bovExport01.xlsx'
#wb=workbook ()
wb2=load_workbook(s)
#ws=wb2.get_sheet_by_name('bovExport01')
ws=wb2.get_sheet_by_name('Planilha3')
data = ws.values
cols = next(data)[0:]
data = list(data)
#print(cols)
#print(data)

#idx = [r[0] for r in data]
#data = (islice(r, 1, None) for r in data)
df = pd.DataFrame(data, columns=cols)
#print(df)

ini
oi3=df.oibr3
oi4=df.oibr4
plt.plot(oi3)
plt.plot(oi4)
plt.show()

del df['oibr3_1']
del df['oibr4_1']
del df['itsa3_1']
del df['itsa4_1']
fim

print('descrições')
print(df.describe())
print('correlação')
corr = df.corr()
print(corr)
print('Desvio padrão')
std = df.std()
desvpad=np.array(std)
print(desvpad)
print('Multiplicação: A X Bcorrelação X desvio padrão')
mult=np.dot(corr,desvpad)
print(mult)
print('Multiplicação pela transposta do desvio padrão')
beta=np.dot(mult,np.transpose(desvpad))
print('beta')
beta = np.exp(beta) - 1
print(beta)
'''

'''
ini
mcorr=np.array(corr,dtype=np.float64)
m2=np.array([[1],[2],[4],[3]],dtype=np.float64)
print('mcorr+m2')
print(mcorr+m2)
print('np.add(mcorr,m2)')
print(np.add(mcorr,m2))
print('(mcorr-m2)')
print(mcorr-m2)
print('np.subtract(mcorr,m2)')
print(np.subtract(mcorr,m2))
print('mcorr*m2')
print(mcorr*m2)
print('np.multiply(mcorr,m2)')
print(np.multiply(mcorr,m2))
print('np.dot')
print(np.dot(mcorr,m2))
print('')
print(m2)
print('')
print(np.linalg.inv(mcorr))
#corr.style.background_gradient()


k={
('media',np.average(p)),
('moda',np.median(p)),
('mediana',np.mean(p))
}
print(k)
print(k.add('media'))

plt.plot(df)
plt.show()
fim
'''
