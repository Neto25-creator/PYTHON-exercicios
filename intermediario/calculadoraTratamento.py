
# Implemente tratamento de exceções em uma calculadora: capture divisão por zero, entradas inválidas e outros erros com mensagens úteis.

import os 
os.system("cls")
def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero!")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida! Use apenas +, -, *, /.")

        print(f"Resultado: {resultado}")

    except ValueError as ve:
        print("Erro de valor:", ve)
    except ZeroDivisionError as zde:
        print("Erro de divisão:", zde)
    except Exception as e:
        print("Ocorreu um erro inesperado:", e)

calculadora()
