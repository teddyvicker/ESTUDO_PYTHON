#ANIMAL#

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} está fazendo um som.")

class Cachorro(Animal):  # Cachorro herda de Animal
    def __init__(self, nome, raca):
        super().__init__(nome)  # Usa o molde do Animal
        self.raca = raca  # Adiciona algo novo

    def latir(self):  # Novo método só do Cachorro
        print(f"{self.nome} está latindo!")

meu_cachorro = Cachorro("Rex", "Labrador")

print(meu_cachorro.nome)  # Vai mostrar: Rex
print(meu_cachorro.raca)  # Vai mostrar: Labrador

meu_cachorro.fazer_som()  # Vai mostrar: Rex está fazendo um som.
meu_cachorro.latir()  # Vai mostrar: Rex está latindo!

#Herança: É quando uma classe (molde) pega tudo de outra classe e adiciona coisas novas.

#super(): Usamos para chamar o molde da classe base.

#Reutilização de código: A herança ajuda a evitar repetição, porque a gente usa o que já existe e só adiciona o que é novo.