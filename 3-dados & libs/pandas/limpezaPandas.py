import os , pandas as pd

df = pd.read_csv(r"C:\Users\Cliente\Documents\ESTUDOS LOCAL\EXEMPLOS\PYTHON\3-dados & libs\pandas\clientes.csv")

print(df.isnull().sum()) #valores nulos
df["renda"] = df["renda"].fillna(df["renda"].mean()) #Preencher valores ausentes (exemplo: preencher renda nula com a média da renda. fillna(preencher pelo o que):
#coluna renda; transforma valor nulo por media de renda
df = df.dropna() #remover linhas com nulos
df = df.drop_duplicates() # remove linhas repetidas

df["idade"] = df["idade"].astype(int)       # força idade como inteiro
df["renda"] = df["renda"].astype(float)     # força renda como float


#corrige nome das colunas
df["cidade"] = df["cidade"].str.strip().str.lower()
df["profissao"] = df["profissao"].str.title()   # primeira letra maiúscula
