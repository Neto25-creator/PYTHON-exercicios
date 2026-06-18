# Use list comprehensions e dict comprehensions para resolver: gerar quadrados dos pares de 1-50, inverter um dicionário chave↔valor, filtrar palavras longas.

import os
os.system("cls")

quadrados = [n**2 for n in range(1, 51) if n % 2 == 0]
print(quadrados)

dicionario = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in dicionario.items()}

palavras = ["sol", "computador", "lua", "programação", "céu"]
longas = [palavra for palavra in palavras if len(palavra) > 5]


print(quadrados)
print(invertido)
print(longas)
