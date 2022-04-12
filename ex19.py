'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
from random import choice
a1 = str (input('Digite o nome do primeiro aluno(a): '))
a2 = str(input('Digite o nome do segundo aluno(a): '))
a3 = str(input('Digite o nome do terceiro aluno(a): '))
a4 = str(input('Digite o nome do quarto aluno(a): '))

lista = [a1,a2,a3,a4]
sorteando = choice(lista)
print('O Aluno  sorteado (a) foi: {} Parabéns'.format(sorteando))