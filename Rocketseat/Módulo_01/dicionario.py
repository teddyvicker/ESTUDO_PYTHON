#criando dicionario

pessoa = {"nome": "danny", "Cidade":"Manaus", "Idade":30 }

#exibir 
print("Meu dicionario:", pessoa)

#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Cidade", pessoa["Cidade"])
print("Idade:", pessoa["Idade"])

pessoa["sobrenome"] = "Figuereido"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"]= 31
print("IDade atualizada", pessoa["idade"])

#Removendo
del pessoa["sobrenome"]
print("Dicionario exemplo:", pessoa)

#Metodo: keys(), valeus(), items()

chaves = list(pessoa.keys())
print("Chave do Dic:", chaves)
print("Primeira Chave:", chaves[0])

#valeus

valores = list(pessoa.values())
print("Valores do dicionários:", valores)
print("primeiro valor do dic:", valores[0])

#metodo itens
itens = list(pessoa.items())
print("Pares de chave de valor:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][2]))