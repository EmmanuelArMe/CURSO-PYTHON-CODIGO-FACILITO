# -*- coding: utf-8 -*-

texto = "  este es un curso de Python 3, Python bàsico  "

#new_string = texto.capitalize() # genera un nuevo string con la primera letra mayuscùla

#new_string2 = texto.swapcase()  # convierte las letras del string que esten en mayuscùlas a minuscùlas y viceversa

new_string = texto.replace("Python", "Java", 1)# El primer parametro el es texto a reemplazar, el segundo es por el cual se va a reemplazar y el tercero es cuantas veces
new_string = texto.strip() # quita los espacios que tenga el texto al inicio y al final
print(new_string)
#print(new_string.isupper())
#print(new_string.islower())
# Los metodos upper y lower son para convertir de mayuscùla a minuscùla
#El metodo title genera un formato de titulo, es decir, Si el titulo es hola mundo lo genera como Hola Mundo

Curso = "Python"
version = 3

#resultado = "Este es el curso de %s %s" %(Curso, version) # lo que realiza es ingresar cada variable en su lugar
resultado = "Este es el curso de {a} {b}".format(a = Curso, b = version)#la ventaja de cambiarte el nombre a las variables
#es que no importa el orden en que las coloque en el format van a tomar el valor donde se desee colocar
print(resultado)