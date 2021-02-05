### Pacotes externos
import urllib.request
import pandas as pd
import numpy as np

### Baixando a base de dados da internet
url = 'https://datasets.saude.go.gov.br/coronavirus/casos_confirmados.csv'
urllib.request.urlretrieve(url, 'C:/Users/Pichau/Documents/GitHub/datases/casos.csv')

### Transformando o arquivo .csv em um data frame
df = pd.read_csv("casos.csv", sep=';')
print(df.head(5))

### Excluindo as variáveis que não vou utilizar
df = df[['data_notificacao','data_inicio_sintomas','codigo_ibge','municipio']]
print(df.head(5))

### Separando os valores dos números das datas de notificação e de primeiros sintomas
# Transformando as variáveis numéricas em variáveis de texto
df['not'] = df['data_notificacao'].astype(str)
df['sint'] = df['data_inicio_sintomas'].astype(str)

# Separando as variáveis
df['not1'] = df['not'].str[0:4]
df['not2'] = df['not'].str[4:6]
df['not3'] = df['not'].str[6:8]

df['sint1'] = df['sint'].str[0:4]
df['sint2'] = df['sint'].str[4:6]
df['sint3'] = df['sint'].str[6:8]

# Juntando as variáveis
df['notific'] = df['not1'] + '-' + df['not2'] + '-' + df['not3']
df['sintom'] = df['sint1'] + '-' + df['sint2'] + '-' + df['sint3']
print(df.head(5))

# Excluindo as variáveis intermediárias
df = df.drop(df.columns[[4, 5, 6, 7, 8, 9, 10, 11]], axis=1)
print(df.head(5))

