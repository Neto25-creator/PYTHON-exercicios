import os 
os.system("cls")
palavra = input("Digite uma palavra: ")


def inverte_string(string):
    invertida = "".join(reversed(string))
    if string == invertida:
        print(f"A palavra '{string}' é um palíndromo")
    else:
        print(f"A palavra '{string}' não é um palíndromo")

inverte_string(palavra)
