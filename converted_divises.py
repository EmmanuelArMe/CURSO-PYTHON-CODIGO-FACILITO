# -*- coding: utf-8 -*-
"""Convertir la cantidad de dólares ingresados por un usuario
a pesos colombianos y mostrar el resultado en pantalla."""

AmmountDolar= input("Ingrese la cantidad de dolares a convertir: \n")

VALUE = 3.896

result = AmmountDolar * VALUE

print("{} dolares equivalen a {} pesos colombianos".format(AmmountDolar, result))