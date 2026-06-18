# Escreva uma classe Pilha e uma classe Fila do zero (sem usar deque). Implemente push/pop e enqueue/dequeue com validação.

import os
os.system("cls")

class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if len(self.itens) == 0:
            print("Erro: Pilha vazia!")
            return None        
        return self.itens.pop() 


class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if len(self.itens) == 0:
            print("Erro: Fila vazia!")
            return None
        return self.itens.pop(0)


# Testando Pilha
p = Pilha()
p.push(10)
p.push(20)
print(p.pop())  # 20
print(p.pop())  # 10
print(p.pop())  # Erro: Pilha vazia!

# Testando Fila
f = Fila()
f.enqueue("A")
f.enqueue("B")
print(f.dequeue())  # A
print(f.dequeue())  # B
print(f.dequeue())  # Erro: Fila vazia!
