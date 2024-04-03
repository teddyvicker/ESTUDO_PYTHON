#if, elif, else 
#Ex IF
idade = int(input("Quantos anos voce tem?"))
print("-----Exemplo de Comando IF-----")
if idade >= 18:
    print("Voce é maior de idade")
elif idade >=12:
    print("Voce é um adolescente:")
else:
    print("Voce é menor de idade")
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Voce não pode se habilitar"
print(mensagem)