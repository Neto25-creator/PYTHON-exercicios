
while True:
    print("Escolha o que deseja fazer com  dois números")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Dividir")
    print("4 - Multiplicar")
    print("0 - Sair")
    escolha = input("Escolha a opção desejada: ")
    if escolha == "0":
        print("saindo...")
        break
    print("Agora digite seus números")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))


    if escolha == "1":
        print("resultado: ", n1 + n2)

    elif escolha == "2":
        print("resultado: ", n1 - n2)
    elif escolha == "3":
        print("resultado: ", n1 / n2)
    elif escolha == "4": 
        print("resultado: ", n1 * n2)
    else:
        print("Escolha inválida")
        
    repetir = input("Deseja fazer outra operação? (s/n): ")
    if repetir.lower() != "s":
        print("Encerrando o programa...")
        break