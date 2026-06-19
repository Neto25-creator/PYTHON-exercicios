import numpy as np

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

soma = mat1 + mat2
produto = np.dot(mat1, mat2)  # multiplicação matricial

# matriz aleatória 5x5
matriz = np.random.randint(1, 100, (5, 5))
media = np.mean(matriz)
desvio = np.std(matriz)
indices_maiores = np.argsort(matriz, axis=None)[-5:]  # pega os 5 maiores
coords = np.unravel_index(indices_maiores, matriz.shape) #coordenada

print(indices_maiores)