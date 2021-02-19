# -*- coding: utf-8 -*-
"""Dado de los valores ingresados por el usuario (base, altura)
calcular y mostrar en pantalla el área de un triángulo."""

base = input("Ingrese la base del triangulo: \n")
altura = input("Ingrese la altura del triangulo: \n")

result = (base * altura) / 2
print("El area del triangulo es: {}".format(result))