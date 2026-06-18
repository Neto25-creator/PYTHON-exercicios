import os

def limpar_tela():
    os.system('cls')

def conversor_temperatura(valor, de, para):
    if de == "C" and para == "F":
        return (9/5 * valor) + 32
    elif de == "F" and para == "C":
        return (5/9) * (valor - 32)
    elif de == "C" and para == "K":
        return valor + 273.15
    elif de == "K" and para == "C":
        return valor - 273.15
    elif de == "F" and para == "K":
        return (5/9) * (valor - 32) + 273.15
    elif de == "K" and para == "F":
        return (9/5) * (valor - 273.15) + 32
    else:
        return None

print("ESCOLHA UMA OPÇÃO:")
print("[1] - Celsius ↔ Fahrenheit")
print("[2] - Fahrenheit ↔ Celsius")
print("[3] - Celsius ↔ Kelvin")
print("[4] - Kelvin ↔ Celsius")
print("[5] - Fahrenheit ↔ Kelvin")
print("[6] - Kelvin ↔ Fahrenheit")
opcao = input("Escolha uma opção: ")
valor = int(input("valor a ser convertido: "))

if opcao == "1":
    print(f"Seu valor transformado:  {conversor_temperatura(valor, 'C', 'F')}")
if opcao == "2":
    print(f"Seu valor transformado:  {conversor_temperatura(valor, 'F', 'C')}")
if opcao == "3":
    print(f"Seu valor transformado:  {conversor_temperatura(valor, 'C', 'K')}")
if opcao == "4":
    print(f"Seu valor transformado:  {conversor_temperatura(valor, 'K', 'C')}")
if opcao == "5":
    print(f"Seu valor transformado:  {conversor_temperatura(valor, 'F', 'K')}")
if opcao == "6":
    print(f"Seu valor transformado:  {conversor_temperatura(valor, 'K', 'F')}")