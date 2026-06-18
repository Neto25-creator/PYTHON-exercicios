class Animal: 
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico de animal"
    
    
class Cachorro(Animal):
        def emitir_som(self):
            return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
animais = [Cachorro("Rex"), Gato("Mimi"), Animal("Genérico")]
for animal in animais:
    print(f"{animal.nome} diz: {animal.emitir_som()}")
