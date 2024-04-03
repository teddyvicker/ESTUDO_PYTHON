#exemplo 
def saudacao(nome):
    print(f"Olá,{nome}")

print("\nChamando a função:")
saudacao("Danny")
saudacao("Vic")

# Retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

resultado_f = int(input("Quero saber o quadrado de: "))
resultado_final = quadrado(resultado_f)
print(f"o quadrado de {resultado_f} quadrado é:", resultado_final)

#função com multiplos parametros 
def soma(numero1, numero2):
    res_tado = numero1 + numero2
    return res_tado

print("\nChama a função soma:")
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
soma_resultado = soma(numero1, numero2)
print("Soma do primeiro %s e o outro numero %s é: %s" % (numero1, numero2, soma_resultado))