# Criando o Molde (classe)
class Carrinho:  # Isso é o molde do carrinho
    def __init__(self, cor, marca):  # Isso é o que o carrinho tem (atributos)
        self.cor = cor  # O carrinho tem uma cor
        self.marca = marca  # E uma marca

    def andar(self):  # Isso é o que o carrinho faz (método)
        print(f"O carrinho {self.marca} está andando!")

#Criando o brinquedo (objeto)
meu_carrinho = Carrinho("vermelho", "Ferrari")  # Criamos um carrinho vermelho da Ferrari

# Usando o brinquedo 
print(meu_carrinho.cor)  # Vai mostrar: vermelho
print(meu_carrinho.marca)  # Vai mostrar: Ferrari
meu_carrinho.andar()  # Vai mostrar: O carrinho Ferrari está andando!

#Resumindo
#Classe: É o molde (ex.: molde de carrinho ou boneca).
#Objeto: É o brinquedo que a gente cria (ex.: carrinho vermelho ou boneca Ana).

#Atributos: São as características (ex.: cor, marca, nome).
#Métodos: São as ações (ex.: andar, falar).

class Boneca:
    def __init__(self, nome, cor_do_cabelo):
        self.nome = nome
        self.cor_do_cabelo = cor_do_cabelo

    def falar(self):
        print(f"{self.nome} diz: Olá, meu cabelo é {self.cor_do_cabelo}!")

minha_boneca = Boneca("Maria", "loiro")  # Criamos uma boneca chamada Ana com cabelo loiro

print(minha_boneca.nome)  # Vai mostrar: Ana
print(minha_boneca.cor_do_cabelo)  # Vai mostrar: loiro
minha_boneca.falar()  # Vai mostrar: Maria diz: Olá, meu cabelo é loiro!