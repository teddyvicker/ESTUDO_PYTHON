class Animal:
    def fazer_som(self):  # Método genérico para fazer som
        print("Este animal faz um som.")

class Cachorro(Animal):  # Cachorro herda de Animal
    def fazer_som(self):  # Substitui o método fazer_som
        print("O cachorro está latindo: Au Au!")

class Gato(Animal):  # Gato herda de Animal
    def fazer_som(self):  # Substitui o método fazer_som
        print("O gato está miando: Miau!")

meu_cachorro = Cachorro()
meu_gato = Gato()

meu_cachorro.fazer_som()  # Vai mostrar: O cachorro está latindo: Au Au!
meu_gato.fazer_som()  # Vai mostrar: O gato está miando: Miau!

#Polimorfismo: O método fazer_som foi redefinido nas classes Cachorro e Gato, mas ele ainda tem o mesmo nome.

#Ação Única, Comportamentos Diferentes: Apesar de chamarmos o mesmo método (fazer_som), cada animal faz um som diferente. 

#Formas Geométricas
class Forma:
    def calcular_area(self):  # Método genérico para calcular área
        print("Esta forma tem uma área.")

class Circulo(Forma):  # Circulo herda de Forma
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):  # Substitui o método calcular_area
        area = 3.14 * (self.raio ** 2)
        print(f"A área do círculo é {area}.")

class Quadrado(Forma):  # Quadrado herda de Forma
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):  # Substitui o método calcular_area
        area = self.lado ** 2
        print(f"A área do quadrado é {area}.")

meu_circulo = Circulo(5)  # Círculo com raio 5
meu_quadrado = Quadrado(4)  # Quadrado com lado 4

meu_circulo.calcular_area()  # Vai mostrar: A área do círculo é 78.5.
meu_quadrado.calcular_area()  # Vai mostrar: A área do quadrado é 16.