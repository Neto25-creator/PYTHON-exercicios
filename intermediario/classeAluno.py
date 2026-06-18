class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0  
        media = sum(self.notas) / len(self.notas)
        return media

    def situacao(self):
        if self.calcular_media() >= 7:
            return("Aprovado")
        else:
            return("Reprovado")

aluno1 = Aluno("Maria")
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(6)
aluno1.adicionar_nota(9)

print("Nome:", aluno1.nome)
print("Notas:", aluno1.notas)
print("Média:", aluno1.calcular_media())
print("Situação:", aluno1.situacao())
