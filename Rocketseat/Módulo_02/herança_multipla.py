class animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(animal):
    def amamentar(self):
        return f"{self.nome} Está Amamentando."

class Ave(animal):
    def voar(self):
        return f"{self.nome} está voando."

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrasonicos"

morcego = Morcego(nome="Batman")

#Acessando metodos da classe base animal
print("nome do morcego é", morcego.nome)