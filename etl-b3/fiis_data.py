import yfinance as yf

# Símbolo do FII que você deseja obter os dados
simbolo_fii = 'HGLG11.SA'

# Defina as datas de início e fim do período desejado
data_inicio = '2018-01-01'
data_fim = '2023-05-23'

# Obtenha os dados do FII
dados_fii = yf.download(simbolo_fii, start=data_inicio, end=data_fim, auto_adjust=True)

# Calcule os indicadores
dados_fii['Valor_Patrimonial_por_Cota'] = dados_fii['Close'] / dados_fii['Close']
dados_fii['Volume_Negociacao'] = dados_fii['Volume'].rolling(window=30).mean()
dados_fii['Taxa_Vacancia'] = 1 - dados_fii['Close'] / dados_fii['Close']

# Calcular Dividend Yield
dados_fii['Dividend_Yield'] = (dados_fii['Close'] - dados_fii['Close'].shift(1)) / dados_fii['Close'].shift(1)

# Imprima os dados obtidos
print(dados_fii)
