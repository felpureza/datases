### Manipulando a base de dados para obter o dataframe em que cada observação é um dia

### Pacotes externos
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Baixando a base de dados da internet
url = 'https://datasets.saude.go.gov.br/coronavirus/casos_confirmados.csv'
urllib.request.urlretrieve(url, 'C:/Users/Pichau/Documents/GitHub/datases/casos.csv')

### Transformando o arquivo .csv em um data frame
df = pd.read_csv("casos.csv", sep=';')
print(df.head(5))

### Excluindo as variáveis que não vou utilizar
df = df[['data_notificacao','data_inicio_sintomas','codigo_ibge','municipio']]
print(df.head(5))

### Valores registrados como de janeiro de 2020 são registrados como janeiro de 2020
df = df.replace([20200101],20210101)
df = df.replace([20200102],20210102)
df = df.replace([20200103],20210103)
df = df.replace([20200104],20210104)
df = df.replace([20200105],20210105)
df = df.replace([20200106],20210106)
df = df.replace([20200107],20210107)
df = df.replace([20200115],20210115)
df = df.replace([20200118],20210118)
df = df.replace([20200130],20210130)

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

### Transformando a variável notific em uma data
df['notific']= pd.to_datetime(df['notific'])

### Montando os dataframes para Goiás e para Goiânia
# Criando os dataframes
goias = df
goiania = df[df.codigo_ibge == 520870]

# Gerando a variável de frequência diária
goias['freq'] = goias.groupby('notific')['notific'].transform('count')
goiania['freq'] = goiania.groupby('notific')['notific'].transform('count')

# Mantendo apenas uma linha por dia
goias = df.drop_duplicates(subset=['notific'], keep='last')
goiania = goiania.drop_duplicates(subset=['notific'], keep='last')

# Conferindo se a soma das frequência bate com a quantidade de casos
sum_go = goias['freq'].sum()
sum_gyn = goiania['freq'].sum()

# Ordenando os valores por ordem crescente
goias = goias.sort_values(by='data_notificacao', ascending=True)
goiania = goiania.sort_values(by='data_notificacao', ascending=True)

# Ordenando a série por notific
goias.sort_values(by=['notific'])
goiania.sort_values(by=['notific'])

# Reindexando os dataframes
goias = goias.reset_index(drop=True)
goiania = goiania.reset_index(drop=True)

### Calculando as médias móveis
# Goiás
for i in range(0,goias.shape[0]-6):
    goias.loc[goias.index[i+6],'media'] = np.round(((
        goias.iloc[i,6] + 
        goias.iloc[i+1,6] + 
        goias.iloc[i+2,6] + 
        goias.iloc[i+3,6] + 
        goias.iloc[i+4,6] + 
        goias.iloc[i+5,6] + 
        goias.iloc[i+6,6])/7),6)

# Goiânia
for i in range(0,goiania.shape[0]-6):
    goiania.loc[goiania.index[i+6],'media'] = np.round(((
        goiania.iloc[i,6] + 
        goiania.iloc[i+1,6] + 
        goiania.iloc[i+2,6] + 
        goiania.iloc[i+3,6] + 
        goiania.iloc[i+4,6] + 
        goiania.iloc[i+5,6] + 
        goiania.iloc[i+6,6])/7),6)
    
# Fórmula extraída em:
# https://www.datacamp.com/community/tutorials/moving-averages-in-pandas

### Plotando os gráficos de média móvel
# Goiás
plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(goias['media'])
plt.savefig('goias.png')

    
