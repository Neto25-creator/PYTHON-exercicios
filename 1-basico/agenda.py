import os
import time

def limpar_terminal():
    os.system("cls")

contatos = {
    "Maria": 54999999999,
    "Jorge": 54999999999,
    "Ana": 54999999999,
    "Rodrigo": 54999999999,
    "Aline": 54999999999,
}

while True:
    limpar_terminal()
    print("SEU DICIONÁRIO DE CONTATOS")
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
            print("SEUS CONTATOS:")
            print("-----------------")
            for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
            print("-----------------")
            input("Enter para voltar ao menu...")
    elif escolha == "2":
        while True: 
            limpar_terminal()
            print("ADICIONAR CONTATO:")
            print("-----------------")
            novo_nome = input("Nome: ")
            novo_numero = input("Número: ")
            contatos.update({novo_nome: novo_numero})
            print("Contato adicionado com sucesso à sua lista!")

            retornar = input("Deseja adicionar outro contato? (s/n): ")
            if retornar.lower() != "s":
                break  
    elif escolha == "3":
         while True:
              limpar_terminal()
              print("REMOVER CONTATOS")
              print("-----------------")
              for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
              print("-----------------")
              remocao = input("Digite o nome do contato a ser excluído: ")
              del contatos[remocao]
              print("Usuário excluído!")
              retornar = input("Deseja adicionar outro contato? (s/n): ")
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