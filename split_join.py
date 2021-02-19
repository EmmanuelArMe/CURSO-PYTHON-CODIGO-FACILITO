lenguajes = "Java; Python; C++; php; Ruby"

separador = "; "

resultado = lenguajes.split(separador) #Resutado es una lista

nuevo_string = "_ ".join(resultado)

print(resultado)
print(nuevo_string)