'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print("Seu nome em letras maísuculas é:{} ".format(nome.upper()))
print('Seu nome em letras minusculas é:{} '.format(nome.lower()))
print("Seu nome é: {} e tem:{} letras".format(nome,len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e contém {} letras'.format(separa[0], len(separa [0])))
print('Seu nome completo é: {} e seu nome do meio é {} e tem {} letras'.format(nome,separa [1], len(separa [1])))
print('Seu Sobre nome é: {}'.format(separa[1]))
print(nome [16::])
