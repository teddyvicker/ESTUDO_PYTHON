print("Exemplo de Captura de Exceções")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro: {e}")
