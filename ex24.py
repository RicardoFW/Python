#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome de uma Cidade: ')).strip()
separa = cidade.split()
print(('Santos') in separa[0])

print(cidade [:6].upper()=='SANTOS')


