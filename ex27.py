'''Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.'''

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Olá {}!Analisando Seu nome...'.format(n[0]))
print('Seu Primeiro nome é:{}'.format(n[0]))
print('Seu ultimo sobrenome é:{}'.format(n[len(n)-1]))


