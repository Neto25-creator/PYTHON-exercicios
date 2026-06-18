dicionario = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : [],
    10 : [],
}

novos_numeros = []

for numero in dicionario:
    tabuada = []
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        tabuada.append(resultado)
    dicionario[numero] = tabuada

    print(dicionario)