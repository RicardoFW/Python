#Exercício Python #025 - Procurando uma string dentro de outra
nome = str(input('Digite Seu nome Completo: ')).strip()

print('Você tem a palavra Silva no nome? {} '.format('silva' in nome.lower()))
print('A palavra Silva foi encontrada na posição: {}'.format(nome.find('Silva')- nome.count(' ')))
