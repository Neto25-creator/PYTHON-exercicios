import pandas as pd             
import seaborn as sns            # gráficos estatísticos 
import matplotlib.pyplot as plt  

# Exemplo de dataset fictício: notas de alunos
dados = {
    "horas_estudo": [1,2,3,4,5,6,7,8,9,10],   # variável independente: horas de estudo
    "nota_prova1": [2,3,4,5,6,6,7,8,9,10],    # notas da primeira prova
    "nota_prova2": [2,4,5,5,7,7,8,9,9,10],    # notas da segunda prova
    "faltas": [10,9,8,7,6,5,4,3,2,1]          # número de faltas
}
df = pd.DataFrame(dados)   # transforma o dicionário em um DataFrame (tabela)


# 1. Calcular correlação entre variáveis
corr = df.corr()   # calcula a matriz de correlação (coeficiente de Pearson entre todas as colunas numéricas)
print(corr)        # imprime a matriz no console

# 2. Criar heatmap com Seaborn
plt.figure(figsize=(6,4))   # define o tamanho da figura
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
# cria o heatmap:
# - corr = matriz de correlação
# - annot=True → mostra os valores numéricos dentro das células
# - cmap="coolwarm" → cores azul/vermelho para correlação negativa/positiva
# - fmt=".2f" → formata os números com 2 casas decimais
plt.title("Matriz de Correlação")   # título do gráfico
plt.show()                          # exibe o gráfico

