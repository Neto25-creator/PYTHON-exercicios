import random

numero_aleatorio = random.randint(1, 100) 

contador = 0
while contador < 5 or numero_user != numero_aleatorio:
    print("Você tem 5 tentativas para acertar")
    numero_user = int(input("Escolha um número de 1 a 100: "))

    if numero_user == numero_aleatorio:
        print("Acertou!")
    elif numero_user < numero_aleatorio:
        print("Seu número está abaixo! ")
    else: 
        print("Seu número está acima! ")
    contador += 1