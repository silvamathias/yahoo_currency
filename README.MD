# Yahoo_Currency

1. [media_movel.py](#media_movel)
2. [crypto_hist.py](#crypto_hist)
3. [dados_yahoo.py](#dados_yahoo)
4. [calc_carteira.py](#calc_carteira)


## Descrição:

Este repositório usa unicamente os dados do [Yahoo Finance](https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD) através da biblioteca [yfinance](https://pypi.org/project/yfinance/)


## Principais arquivos

<a id="media_movel"></a>

### media_movel.py

#### Para que serve?

cria uma média móvel para uma determinada criptomoeda alterando 'btc' em `pp = ['btc']` pelo código de outra cripto.


#### Configurar intervalo de tempo

No trecho abaixo é possível escolher o intervalo de tempo e de duas formas possíveis conforme descrito

~~~python
#exemplo: para pegar dados dos últimos 5 anos (ano - 5); para últimos 5 mesês (mes - 5); para últimos 5 dias (dia - 5)
d_1 = dtm(ano-1, mes, dia)

#>>>>caso queira usar período inicial e final<<<<-------------------------------
#papeis = yf.download(pp,start = d_1, end = hj, group_by = 'ticker')
#-------------------------------------------------------------------------------
~~~


#### Configurar médias

Configure os períodos da média móvel em `medias = [2,3,4,5]` 

Uma sugestão para este trecho é `medias = [5,7,10,15,30,60]`

<a id="crypto_hist"></a>

### crypto_hist.py

#### Para que serve?

Baixa o preço de uma lista de criptomoedas predeterminadas em intervalo de tempo regular e salva no arquivo *base_cur.csv*


#### Lista de criptomoedas

Inclua ou retire códigos das moédas em `currency_list = ['BTC-USD','ETH-USD','DOGE-USD','SHIB-USD','BRL=X','EURBRL=X','EUR=X']`


#### Configurando o intervalo de tempo

Informe os segundo que deseja de intervalo entre as consultas em `tm.sleep(57)`

No trecho acima os dados são baixados a cada 57 segundos

<a id="dados_yahoo"></a>

### dados_yahoo.py

#### Para que serve?

Baixa o preço de uma lista de criptomoedas predeterminadas em intervalo de tempo regular e salva nos arquivo:

1. *df_adj.csv* armazena os dados dos preços ajustados;
2. *df_index.csv* armazena os dados ajustados em forma de índice (n / n-1). 


#### Lista de criptomoedas

Inclua ou retire códigos das moédas em `pp = ['BTC-USD','ETH-USD','DOGE-USD','SHIB-USD','BRL=X','EURBRL=X','EUR=X']`


#### Configurar intervalo de tempo

No trecho abaixo é possível escolher o intervalo de tempo e de duas formas possíveis conforme descrito

~~~ python
#exemplo: para pegar dados dos últimos 5 anos (ano - 5); para últimos 5 mesês (mes - 5); para últimos 5 dias (dia - 5)
d_1 = dtm(ano, mes - 3, dia)
papeis = yf.download(pp,start = d_1, end = hj, group_by = 'ticker')
#--------------------------------------------------------------------------
#----dados por período-----------------------------------------------------
#para pegar dados dos por período (1mo = 1 mes; 3mo = 3 meses; etc)--------
#papeis = yf.download(pp,period = '1mo', group_by = 'ticker')
#--------------------------------------------------------------------------
~~~

<a id="calc_carteira"></a>

### calc_carteira.py

#### Para que serve?

Usa os dados do arquivo *df_index.csv* para criar uma carteira hipotética e calcula os indicadores:

1. Risco carteira diário
2. Retorno esperado carteira(retorno por ação * proporção
3. Índice de sharpe da carteira;


#### Taxa SELIC

Atualise a taxa SELIC em `SELIC = 0.1375`

No exemplo acima representa uma SELIC igual à 13,75% (tx em 07/09/2022)

#### Criptomoedas de interesse

Informe em `lista_cur = ['BTC-USD', 'ETH-USD', 'DOGE-USD', 'SHIB-USD']`as moédas de interesse lembrando que ela deve estar no arquivo *df_index.csv*

#### Proporções em cada moéda

Ajuste a proporção percentual para cada moéda em `prop = (0.27, 0.40, 0.13, 0.20)` onde a soma tem que ser 1 (100%)


