while True:
    print("CALCULADORA DE IMC")
    peso = float(input("Digite o seu peso em KG: "))
    altura = float(input("Digite a sua altura em M: "))
    calculo_imc = (peso / (altura ** 2))
    print(calculo_imc)

    if calculo_imc < 18.5:
        print("Baixo peso")
    elif calculo_imc >= 18.5 and calculo_imc <= 24.99:
        print("Normal")
    elif calculo_imc >= 25 and calculo_imc <= 29.99:
        print("Sobrepeso")
    else:
        print("obeisdade")
