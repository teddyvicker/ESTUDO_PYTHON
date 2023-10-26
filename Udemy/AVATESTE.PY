#a = 0

#for i in range (30):
#    if a%2 == 0:
#        a += 1
#        continue
#    else:
#        if a%5 == 0:
#            break
#            a +=3
#  print(a)

#class Carro(object): 
#def FaleComigo(self): 
#print ("Sou um carro")

#class Fusca (Carro): 
#def FaleComUmFusca(self): 
#print ("Sou um Fusca") 

#x = Carro() 
#y = Fusca() 

#x.FaleComigo() 
#y.FaleComigo() 

#minha_lista = [0, 5, 10, 20, 25, 30]
#def filtro(numero):
#    if numero > 10:
#        return True
#    return False

#minha_lista_filtrada = filter (filtro,minha_lista)

#print( 
#    f'{minha_lista_filtrada}')

#x = 1 / 2 + 3 // 3 + 4 ** 2
#print(x)
#def foo(n):
#   if n > 1:
#        return n* foo (n-1)
#   return n
#print(foo(4))

#lista = ["cachorro","hamster",["pato", "galinha","porco"],"gato"]
#print(lista[3][2])

#def fc(x,y):
#    s=0
#    a= x.lower()
#    for i in a:
#        if (i==y):
#            s=s + 1
#            return s
#a = 'Aracaju/Sergipe'
#x = fc(a,'a')*100
#y= fc(a,'e')*10
#z = fc(a,'i')
#print(x+y+z)

a, b = 0, 2
while b < 20:
    a, b = b, a+b+1
    print(b)