print("Importação de um módulo padrão:")
#import math
from math import sqrt
raiz_quadrada = sqrt(25)
print(f"A Raiz quandrada de 25 é: {raiz_quadrada}")

print("\n Exemplo de criação de utilização de um modulo>")
from meu_modulo import saudacao, dobro 
mensagem = meu_modulo.saudacao("Vic")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(resultado_dobro)