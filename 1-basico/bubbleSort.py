import os 
def limpar_tela():
    os.system("cls")

limpar_tela()
numeros = [20, 10, 42, 123, 13, 543, 63, 23, 124, 432, 21, 23]

def ordena_numeros(lista):
     for i in range(len(lista)):
        for numero in range(len(lista) - 1):
            if lista[numero] > lista[numero+1]:
                lista[numero], lista[numero+1] = lista[numero+1], lista[numero]
                print(numeros)


ordena_numeros(numeros)