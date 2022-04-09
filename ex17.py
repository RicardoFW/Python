'''Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Cmprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}\n".format(hi))
#     ou
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input('Compromento do cateto adjacente: '))
hi = math.hypot(co,ca)
print("A hipotenusa vai medir {:.2f}\n".format(hi))
#     Ou
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input('Compromento do cateto adjacente: '))
hi = hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hi))