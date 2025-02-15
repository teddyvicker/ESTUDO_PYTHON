# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de Classe 
    
    def __init__(self, nome):
        self.nome = nome #Atributo da Instancia
    
    #requer uma instancia para ser chamado
    def metodo_instancia(self):
        return f"Metodo de instancia chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Metodo da classe chamado para valor = {cls.valor}" #recebe a referencia da classe

    @staticmethod   
    def metodo_estatico():
        return "Metodo Estatico chamado!"   #não recebe a referencia da classe

obj = MinhaClasse(nome = "Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuração01 = "Hyundai, creta, 2024"
carro_river = Carro.criar_carro(configuração01)
print(f"\n \nMarca: {carro_river.marca} \nModelo: {carro_river.modelo}\nAno: {carro_river.ano}")

class Mat:
    
    @staticmethod
    def somar(a, b):
        return a + b

print(Mat.somar(a=44, b=99))