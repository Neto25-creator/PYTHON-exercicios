import numpy as np                # NumPy: cálculos numéricos
import matplotlib.pyplot as plt   # Matplotlib: gráficos

# Dados fictícios: horas de estudo (x) e notas (y)
x = np.array([1, 2, 3, 4, 5, 6])  # variável independente (horas de estudo)
y = np.array([2, 4, 5, 4, 5, 7])  # variável dependente (nota do aluno)

# Regressão linear do zero 
x_mean = np.mean(x)   # média de x
y_mean = np.mean(y)   # média de y

# coeficiente angular (a): inclinação da reta
# fórmula: cov(x,y) / var(x)
a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)

# coeficiente linear (b): intercepto da reta
# fórmula: média de y - a * média de x
b = y_mean - a * x_mean

print("Coeficientes (do zero): a =", a, ", b =", b)

#  Comparação com numpy.polyfit 
coef_polyfit = np.polyfit(x, y, 1)   # ajusta polinômio de grau 1 (reta)
print("Coeficientes (polyfit):", coef_polyfit)

#  Plotar dados e reta 
plt.scatter(x, y, color="blue", label="Dados")          # pontos originais
plt.plot(x, a*x + b, color="red", label="Reta (manual)") # reta calculada do zero
plt.plot(x, np.polyval(coef_polyfit, x), color="green", linestyle="--", label="Reta (polyfit)") # reta com polyfit
plt.xlabel("Horas de estudo")   # rótulo eixo X
plt.ylabel("Nota")              # rótulo eixo Y
plt.title("Regressão Linear")   # título do gráfico
plt.legend()                    # legenda para diferenciar as retas
plt.show()                      # exibe o gráfico