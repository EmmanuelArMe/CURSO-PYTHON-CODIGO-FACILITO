# -*- coding: utf-8 -*-
cursos = ["python", "php", "java", "c++", "c#"]

curso = cursos[:]

print(curso)

lista = [1.83, 2.45, 5,7,8,12,0,1.2]

#.sort es el metodo para ordenar una lista de orden ascendente.
lista.sort()

print(lista)

#.sort mas el parametro reverse = True es para ordenarla de manera descendente.
lista.sort(reverse = True)

print(lista)

# La funcion min lo que realiza es devolvernos el numero menor de la lista
menor = min(lista)

print(menor)

# La funcion max lo que realiza es devolvernos el numero menor de la lista
mayor = max(lista)

print(mayor)

# La funciòn len nos devuelve la longitud de la lista
longitud = len(lista)

print(longitud)

# In es para saber si ese valor se encuentra o no en la lista
resultado = 10 in lista

print (resultado)

# Index es para saber el indice del valor que le pasemos en la lista
indice = lista.index(8)

print (indice)

# Count es para saber si se encuentra y cuantas veces se encuentra un valor en la lista
contador = lista.count(8)

print (contador)