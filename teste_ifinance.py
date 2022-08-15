import yfinance as yf

p = yf.Ticker("ETH-USD")

#dados = ['a','b','bq','c','cd','cq','d','e','ed','eq','f','h','i','ih','iin','m','n','o','r','s','st']
dados = []
d = p.dividends
b = p.balance_sheet

bq = p.quarterly_balance_sheet

i = p.info

a = p.actions

h = p.history(period='max')

s = p.splits

f = p.financials

m = p.major_holders

ih = p.institutional_holders

c = p.cashflow

cq = p.quarterly_cashflow

e = p.earnings
eq = p.quarterly_earnings

st = p.sustainability

r = p.recommendations
cd = p.calendar
#ed = p.earnings_dates
iin = p.isin
o = p.options
n = p.news

'''
for dd in dados;
print('-'*4 + dd + '-'*50)
print(dd)
'''
print('-'*4 + 'a' + '-'*50)
print(a)
print('-'*4 + 'b' + '-'*50)
print(b)
print('-'*4 + 'bq' + '-'*50)
print(bq)
print('-'*4 + 'c' + '-'*50)
print(c)
print('-'*4 + 'cd' + '-'*50)
print(cd)
print('-'*4 + 'cq' + '-'*50)
print(cq)
print('-'*4 + 'd' + '-'*50)
print(d)
print('-'*4 + 'e' + '-'*50)
print(e)
#print('-'*4 + 'ed' + '-'*50)
#print(ed)
print('-'*4 + 'eq' + '-'*50)
print(eq)
print('-'*4 + 'f' + '-'*50)
print(f)
print('-'*4 + 'h' + '-'*50)
print(h)
print('-'*4 + 'i' + '-'*50)
print(i)
print('-'*4 + 'ih' + '-'*50)
print(ih)
print('-'*4 + 'iin' + '-'*50)
print(iin)
print('-'*4 + 'm' + '-'*50)
print(m)
print('-'*4 + 'n' + '-'*50)
print(n)
print('-'*4 + 'o' + '-'*50)
print(o)
print('-'*4 + 'r' + '-'*50)
print(r)
print('-'*4 + 's' + '-'*50)
print(s)
print('-'*4 + 'st' + '-'*50)
print(st)
