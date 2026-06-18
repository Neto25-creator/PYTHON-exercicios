import os 

def limpar_tela():
    os.system("cls")

limpar_tela()

dicionario = {}
frase_escrita = input("Sua frase: ")

def conta_letras(frase):
    palavras = frase.split()
    for palavra in palavras:
        dicionario[palavra] = len(palavra)
    print(dicionario)

conta_letras(frase_escrita)