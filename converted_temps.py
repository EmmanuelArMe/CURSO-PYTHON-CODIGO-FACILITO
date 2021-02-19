# -*- coding: utf-8 -*-
"""Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit
y mostrar el resultado en pantalla."""

GradosCentigrados = input("Ingrese la cantidad de grados centigrados a convertir: \n")

FARENHEIT = 33.8

result = GradosCentigrados * FARENHEIT

print("{} Grados centigrados son {} Fahrenheit".format(GradosCentigrados, result))