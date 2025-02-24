                            # STAR WARS #
import random
# Personagem - Classe mãe 
# Jedi : controlado pelo usuario 
# Sith : adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel()*2, self.get_nivel()*4) #baseada no nivel
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

# Heroi    
class Jedi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel()*5, self.get_nivel()*8) #Dano aumentadoooo
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} causou {dano} de dano!")
#Inimigo 
class Sith(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

#GESTAO DO JOGO 
class Jogo:
    def __init__(self):
        self.jedi = Jedi(nome="Luke Skywalker",vida=100,nivel=5,habilidade="Jedi")
        self.sith = Sith(nome="Anakin Skywalker",vida=100,nivel=4,tipo="Sith")
    
    def iniciar_batalha(self):
        
        
        
        print("\n*--------------------------------------------*")
        print("*----------May the for be with you!-----------*")
        print("*---------------------------------------------*")
        print("\nPrepare-se para a luta!")
        while self.jedi.get_vida() > 0 and self.sith.get_vida()>0:
            print("\nDetalhes dos Lutadores: ")
            print(self.jedi.exibir_detalhes())
            print(self.sith.exibir_detalhes())
            
        
            input("Pressione [Enter] para atacar... ")
            escolha = input("1 - Ataque de Sabre\n2 - Ataque Especial!")
            
            if escolha == '1':
                self.jedi.atacar(self.sith)
            elif escolha == '2':
                self.jedi.ataque_especial(self.sith)
            else:
                print("\nEscolha inválida. Tente novamente.")

            if self.sith.get_vida() > 0:
                #Inimigo ataca
                self.sith.atacar(self.jedi)
        if self.jedi.get_vida() > 0:
            print("\n\n Parabéns! Você é um verdadeiro Jedi!")
        else:
            print("\n\n Voce é um verdadeiro Sith, bem vindo ao Darkside!")

#Criar instancia do jogo iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()        


