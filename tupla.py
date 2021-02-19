tupla = (1, 2, 3, 4)

elemento1 = tupla[3]
elemento2 = tupla[-1]

print(elemento1, elemento2)

sub = tupla[:3:2]

print(sub)

uno, dos, tres,  cuatro = tupla[0], tupla[1], tupla[2], tupla[3]

print(uno)
print(dos)
print(tres)
print(cuatro)

uno, dos, tres,  cuatro = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)

# Si la tupla estuviera mas elementos se le coloca al ultimo un *
# para asignarle al la ultima variable los que resten
# con la funciòn list podemos convertir una tupla a list sin modificar sus valores,
#teniendo en cuenta que las tuplas son imutables , con la funciòn tuple podemos convertir una lista
#a una tupla sin ser modificados sus valores.
#podemos convertir una cadena en lista o en tupla con la funcion lis y tuple