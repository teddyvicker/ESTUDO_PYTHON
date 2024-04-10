print("Exemplo de Captura de Exceções")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de valeu Erro : {e}")
    raise ValueError ("Tipo de Variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operação finalizada")
