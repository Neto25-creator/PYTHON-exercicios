lista_notas = [4.5, 5, 7.8, 9.2, 9.5, 2.4, 10, 7.1]

def calcular_media(lista):
    media = sum(lista) / len(lista)
    maior_nota = max(lista)
    menor_nota = min(lista)

    print ("número de alunos aprovados: " "de ", len(lista_notas))
    print ("média: ", media)
    print ("maior nota: ", maior_nota)
    print ("menor nota: ", menor_nota)
print(calcular_media(lista_notas)) 
