#declaração
minha_lista = [1, 2, 3, 4, 5, "vicoliveira", True, False]

#Exibindo a lista completa
print("Minha lista de Exemplo", minha_lista)

#Exibindo a lista por indice
print(minha_lista[1:6])

#Alterando a lista
minha_lista[0] = "vic"
print(minha_lista)

#Metodo append(): (adiciona um elemento ao final da lista)
minha_lista.append(6)
print(minha_lista)

#Metodo index
indice = minha_lista.index(6)
print(indice)

#Metodo insert: Insere em um indice especifico

minha_lista.insert(2, 10)
print(minha_lista)

#Metodo pop
elemento_removido = minha_lista.pop(3)
print(elemento_removido)

#Metodo Remove
minha_lista.remove(True)
print("remove (true):", minha_lista)

#Metodo Sort
minha_lista.sort()

