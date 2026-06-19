# Com Pandas: carregue um CSV, explore com head/info/describe, encontre valores nulos, filtre linhas por condição e agrupe dados calculando estatísticas por grupo.

import pandas as pd
import os
os.system("cls")
df = pd.read_csv(r"C:\Users\Cliente\Documents\ESTUDOS LOCAL\EXEMPLOS\PYTHON\3-dados & libs\pandas\clientes.csv")

print(df.head(2)) #Ver primeiras 2 linhas
print(df.info()) #Informações gerais
print(df.describe()) #Estatísticas descritivas
print(df.isnull().sum()) #Encontra valores nulos


#Filtrar por idade
filtro = df[df["idade"] > 30]
print(filtro) 


#Agrupar dados e filtrar
#Exemplo: agrupar por cidade e calcular média de idade.
agrupado = df.groupby("cidade")["idade"].mean()
print(agrupado)

#várias estatísticas de uma vez:
estatisticas = df.groupby("cidade")["idade"].agg(["mean", "max", "min"])
print(estatisticas)
