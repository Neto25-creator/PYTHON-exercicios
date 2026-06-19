import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dataset fictício: notas de alunos em duas provas
dados = {
    "aluno": ["Ana","Carlos","Mariana","João","Fernanda","Pedro","Luciana","Roberto","Patrícia","André"],
    "prova1": [7.5, 8.0, 9.2, 6.0, 8.5, 7.0, 6.8, 5.5, 9.0, 8.7],
    "prova2": [8.0, 7.5, 9.5, 6.5, 9.0, 7.2, 7.0, 6.0, 9.3, 9.0]
}
df = pd.DataFrame(dados)   # transforma o dicionário em um DataFrame (tabela) para facilitar análise


# 1. Gráfico de linha (evolução das notas de um aluno)
plt.figure(figsize=(6,4))   # cria uma nova figura com tamanho 6x4
plt.plot(["Prova 1","Prova 2"], [df.loc[0,"prova1"], df.loc[0,"prova2"]], marker="o")
# plota as notas da primeira aluna (linha 0 do DataFrame), marcando os pontos com "o"
plt.title("Notas da Ana")   # título do gráfico
plt.ylabel("Nota")          # rótulo do eixo Y
plt.show()                  # exibe o gráfico


# 2. Gráfico de barras (notas da Prova 1 por aluno)
plt.figure(figsize=(8,4))   # nova figura, maior para caber os nomes
plt.bar(df["aluno"], df["prova1"], color="skyblue")
# cria barras com os nomes dos alunos no eixo X e notas da prova1 no eixo Y
plt.title("Notas da Prova 1")   # título
plt.xticks(rotation=45)         # gira os nomes para não ficarem sobrepostos
plt.ylabel("Nota")              # rótulo do eixo Y
plt.show()                      # exibe


# 3. Histograma (distribuição das notas da Prova 2)
plt.figure(figsize=(6,4))   # nova figura
plt.hist(df["prova2"], bins=5, color="orange", edgecolor="black")
# cria histograma das notas da prova2, dividindo em 5 intervalos (bins)
plt.title("Distribuição das Notas da Prova 2")   # título
plt.xlabel("Nota")                               # rótulo eixo X
plt.ylabel("Frequência")                         # rótulo eixo Y
plt.show()                                       # exibe


# 4. Scatter plot (comparação Prova 1 vs Prova 2)
plt.figure(figsize=(6,4))   # nova figura
plt.scatter(df["prova1"], df["prova2"], color="green")
# cria pontos mostrando relação entre notas da prova1 (X) e prova2 (Y)
plt.title("Correlação entre Prova 1 e Prova 2")   # título
plt.xlabel("Prova 1")                             # rótulo eixo X
plt.ylabel("Prova 2")                             # rótulo eixo Y
plt.show()                                        # exibe

