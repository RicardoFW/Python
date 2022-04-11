'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.'''
import math
angulo = float(input("Digite u valor do angulo: "))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print("o angulo de {} tem o sendo de {:.2f} e cosseno de {:.2f} e sua tangente de {:.2f} \n".format(angulo,seno,coseno,tang))

  #             ou

from math import radians, sin,cos ,tan

angulo = float(input("Digite o angulo que você deseja: "))
seno = sin(radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}".format(angulo,seno))
coseno = cos(radians(angulo))
print("O angulo de {} tem o COSSENO de {:.2f}".format(angulo,coseno))
tang = tan(radians(angulo))
print("O angulo de {} tem sua TANGENTE de {:.2f}".format(angulo,tang))