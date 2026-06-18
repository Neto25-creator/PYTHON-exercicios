import os
import time

def limpar_terminal():
    os.system("cls")

produtos = {
    "Mouse": 80,
    "Teclado": 120,
    "Monitor": 549,
    "Mousepad": 50,
    "Cabo USB C": 24,
}

while True:
    limpar_terminal()
    print("PRODUTOS")
    print("Escolha uma opção")
    print("-----------------")
    print("[1] - Listar")
    print("[2] - Adicionar")
    print("[3] - Remover")
    print("[0] - Fechar")
    print("-----------------")
    escolha = input("Opção: ")

    if escolha == "1":
            limpar_terminal()
            print("PRODUTOS NO CARRINHO:")
            print("-----------------")
            for nome, valor in produtos.items():
                print(f"{nome}: {valor}")
            print("-----------------")
            input("Enter para voltar ao menu...")
    elif escolha == "2":
        while True: 
            limpar_terminal()
            print("ADICIONAR PRODUTO NO CARRINHO:")
            print("-----------------")
            novo_nome = input("Nome: ")
            novo_valor = input("Valor: ")
            produtos.update({novo_nome: novo_valor})
            print("Produto adicionado com sucesso à sua lista!")

            retornar = input("Deseja adicionar outro Produto? (s/n): ")
            if retornar.lower() != "s":
                break  
    elif escolha == "3":
         while True:
              limpar_terminal()
              print("REMOVER produtos")
              print("-----------------")
              for nome, valor in produtos.items():
                print(f"{nome}: {valor}")
              print("-----------------")
              remocao = input("Digite o nome do produto a ser excluído: ")
              del produtos[remocao]
              print("Usuário excluído!")
              retornar = input("Deseja adicionar outro Produto? (s/n): ")
              if retornar.lower() != "s":
                break  
    elif escolha == "0":
         print("Saindo...")
         time.sleep(1.3)
         limpar_terminal()
         break
    else: 
        print("Escolha incorreta")
        time.sleep(1.5)