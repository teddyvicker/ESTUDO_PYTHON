#Tupla exemplo 
minha_tupla =(1,2,3,4)
print("minha tupla:", minha_tupla)

print("minha tupla(0)", minha_tupla[0])
print("minha tupla(2)", minha_tupla[2])
print("minha tupla(-1)", minha_tupla[-1])

#metodo count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice a primeira ocorrencia do elemento3 :", indice)