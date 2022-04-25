'''Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
frase = str(input('Digite Uma Frase: ')).upper().strip()
print('Analisando a frase... {}'.format(frase))
print('Na frase "{}" a Letra A aparece {} vezes'.format(frase,frase.count('A')))
print('e sua primeira posição é: {} '.format(frase.find('A')+1))
print('e sua ultima posição é: {} '.format(frase.rfind('A')+1))