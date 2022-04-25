#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''numero = int(input('Digite um numero com 4 algarismos: '))
print('Analisando os números {} temos:'.format(numero))
numero = str (numero)
dividido = numero.split()
print('Unidades {}'.format(dividido [0][3]))
print('Dezena {}'.format(dividido [0][2]))
print('Sentena {}'.format(dividido [0][1]))
print('Un.Milhar {}'.format(dividido [0][0]))'''

num = int(input('Digite um numero com 4 algarismos: '))
print('Analisando os números {} temos:'.format(num))
u= num // 1 % 10
d = num //10 % 10
c = num //100 % 10
um = num // 1000 % 10
print('Unidades:{}'.format(u))
print('Dezena:{}'.format(d))
print('Sentena:{}'.format(c))
print('Un.Milhar:{}'.format(um))



