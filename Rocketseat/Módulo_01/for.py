print ("\nFor utilizando LISTA!")
lista = [1, 2, 3, 4, 5]
for elementos in lista:
    print(elementos)
    
print ("\nFor utilizando TUPLA!")
tupla = (1, 2, 3, 4, 5,)
for elemento in tupla:
    print(elementos)

print ("\nFor ultilizando DICIONARIO! - Chaves")
pessoa = {"Nome":"Danny", "Idade":30, "Cidade":"Oriximina"}
for chave in pessoa.keys():
    print(chave)

print("\nFor ultilizando DICIONARIO! - VALOR")
for valor in pessoa.values():
    print(valor)

print("\nFor ultilizando DICIONARIO! - ITENS")
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")

#range(): intervalo numerico 
#print(list(range(0,10)))
print("\n Ultilizando a função Range")
for numero in range(5):
    print(numero)

print("\n Ultilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print (lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice]= 0 
print(lista)        

#enumerate()

lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")