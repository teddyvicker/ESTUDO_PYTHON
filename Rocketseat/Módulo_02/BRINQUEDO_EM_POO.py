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

#Herança

class Carrinho:  # Molde do carrinho genérico
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

    def andar(self):
        print(f"O carrinho {self.marca} está andando!")

#Criar a Classe Derivada

class CarrinhoDeCorrida(Carrinho):  # CarrinhoDeCorrida herda de Carrinho
    def __init__(self, cor, marca, motor_turbo):
        super().__init__(cor, marca)  # Usa o molde do Carrinho
        self.motor_turbo = motor_turbo  # Adiciona algo novo
    def acelerar(self):  # Novo método só do CarrinhoDeCorrida
        print(f"O carrinho {self.marca} está acelerando com motor turbo {self.motor_turbo}!")

#Usar o Carrinho de Corrida 

meu_carro_de_corrida = CarrinhoDeCorrida("vermelho", "Ferrari", "V8")

print(meu_carro_de_corrida.cor)  # Vai mostrar: vermelho
print(meu_carro_de_corrida.marca)  # Vai mostrar: Ferrari
print(meu_carro_de_corrida.motor_turbo)  # Vai mostrar: V8

meu_carro_de_corrida.andar()  # Vai mostrar: O carrinho Ferrari está andando!
meu_carro_de_corrida.acelerar()  # Vai mostrar: O carrinho Ferrari está acelerando com motor turbo V8!

#O que Aconteceu Aqui?
#Herança: A classe CarrinhoDeCorrida herdou tudo da classe Carrinho (atributos e métodos).
#Adicionou algo novo: O CarrinhoDeCorrida tem um motor turbo e um método acelerar que o carrinho genérico não tem.

