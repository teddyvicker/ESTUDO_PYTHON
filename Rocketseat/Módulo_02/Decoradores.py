def bateria(func):  # Função decoradora
    def verificar():
        print("Verificando bateria...")  # Nova funcionalidade
        print("Bateria OK!")
        func()  # Chama a função original
    return verificar

@bateria  # Aplica o decorador à função robo
def robo():
    print("O robô está funcionando!")

robo()
# Vai mostrar:
# Verificando bateria...
# Bateria OK!
# O robô está funcionando!