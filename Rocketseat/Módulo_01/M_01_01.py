#Declaração
nome = "vic"
sobrenome= "oliveira"
nome_completo = "danny figueiredo"

#Formataçãotermo 

print ("Nome completo (la forma):", nome_completo)
print ("Nome completo (2a forma):" + nome_completo)
print ("Nome completo (3a forma):" + "Gabriel" + "Casemiro")
print ("Nome completo (4a forma):" + "Cabriel", "Casemiro")
print ("Nome completo (5a forma):", nome_completo)
print ("Nome completo (6a forma):", nome_completo)
print("Nome completo (7a forma): %s" % nome_completo)
print ("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print ("Nome completo (10a forma): {}{}" .format(nome, sobrenome))

#booleano 

True 

False 

#condição 

if True:
    print("bloco IF executado")
else:
    print("não será executado")
#Operação logico AND

if True and True:
    print("bloco IF executado")
if True and False :
    print("Bloco nao será executado")
#OR
if True or False:
    print("Bloco será executado")