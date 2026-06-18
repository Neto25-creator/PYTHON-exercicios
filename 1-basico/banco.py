import os, time
def limpar_tela():
    os.system("cls")

saldo_atual = 0
extrato = []
while True: 
    limpar_tela()
    print("SUA CONTA BANCARIA")
    print("[1] - Ver saldo")
    print("[2] - Sacar")
    print("[3] - Depositar")
    print("[4] - Ver extrato")
    print("[0] - Sair")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        limpar_tela()
        print(f"Seu saldo atual: R$", saldo_atual)
        input("Pressione enter para continuar...")
    if escolha == "2":
        limpar_tela()
        print("SAQUE")
        saque = float(input("Valor a ser sacado: "))
        saldo_atual = saldo_atual - saque
        extrato.append(f"Saque de R$ {saque}")
        print(f"O valor de R${saque} foi retirado de sua conta!")
        input("Pressione enter para continuar...")
    if escolha == "3":
        limpar_tela()
        deposito = float(input("Valor deseja depositar: "))
        saldo_atual += deposito
        extrato.append(f"Depósito de R$ {deposito}")
        print(f"Uma quantia de ", deposito, "foi adicionado a sua conta! Saldo atual: ", saldo_atual)
        input("Pressione enter para continuar...")    
    if escolha == "4":
        limpar_tela()
        print("SEU EXTRATO:")
        print(extrato)
        input("Pressione enter para continuar...")
    if escolha == "0":
        print("Saindo...")
        time.sleep(2)
        limpar_tela()
        break    