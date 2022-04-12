''''Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle
n1 = str(input('Digite o nome do Primeiro Aluno(a): '))
n2 = str(input('Digite o nome do Segundo Aluno(a): '))
n3 = str(input('Digite o nome do teceiro Aluno(a): '))
n4 = str(input('Digite o nome do Quato Aluno (a): '))
lista = [n1,n2,n3,n4]
shuffle (lista)
print('A Ordem de Apresentação é: {}'.format(lista))