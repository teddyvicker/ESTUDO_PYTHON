from abc import ABC, abstractmethod

class Carro(ABC):  # Classe abstrata
    @abstractmethod
    def ligar(self):  # Método abstrato: não tem implementação aqui
        pass

    @abstractmethod
    def acelerar(self):  # Método abstrato: não tem implementação aqui
        pass

class CarroEsportivo(Carro):  # CarroEsportivo herda de Carro
    def ligar(self):  # Implementa o método abstrato
        print("Carro esportivo ligado!")

    def acelerar(self):  # Implementa o método abstrato
        print("Carro esportivo acelerando a 200 km/h!")

meu_carro = CarroEsportivo()

meu_carro.ligar()  # Vai mostrar: Carro esportivo ligado!
meu_carro.acelerar()  # Vai mostrar: Carro esportivo acelerando a 200 km/h!