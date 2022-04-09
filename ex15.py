#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
km = float(input("Quantos quilômetros foi percorrido durante a viagem? "))
dia = float(input("Quantos dias foram de aluguel? "))
valorkm  = km * 1.25
valordia = dia * 60
valort   = valorkm + valordia
print("Valor em dias R${:.2f} valor em Km R${:.2f} Total a pagar: R${:.2f}".format(valordia,valorkm,valort))



