#Exercício Python 014: Escreva um programa que converta uma temperatura digitando
#em graus Celsius e converta para graus Fahrenheit.
c = float(input("Inofrme a temperatura em ºC "))
f = ((c * 9)/5) +32
print("A temperatua em {}ºC corresponde a temperatura {}ºF".format(c,f))