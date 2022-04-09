#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input("Digite um valor: "))
print("O Número Digitado foi {} e sua parte inteira é {}".format(num, math.trunc(num)))
# ou
from math import trunc
num = float(input("Digite um valor: "))
print("O Número Digitado foi {} e sua parte inteira é {}".format(num,trunc(num)))
# ou
num = float(input("Digite um valor: "))
print("O Número Digitado foi {} e sua parte inteira é {}".format(num,int(num)))


