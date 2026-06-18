import os

def limpar_terminal():
    os.system("cls")

limpar_terminal()
numeros = input("Digite números separados por espaço: ")
lista_str = numeros.split()

lista_int = list(map(int, lista_str))

print("Sua lista de números:", lista_int)

def calcular(lista):
    media = sum(lista) / len(lista)
    maior_num = max(lista)
    menor_num = min(lista)
    print ("média: ", media)
    print ("maior número: ", maior_num)
    print ("menor número: ", menor_num)

calcular(lista_int)