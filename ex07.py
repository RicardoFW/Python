#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
n = float (input("Digite sua primeira nota "))
n2 = float (input("Digite a Segunda nota "))
m = (n+n2) /2
print ("A sua media entre {} e {} e {:.2f}".format(n,n2,m))


 #ou

print ("\nPrimeira nota {} Segunda nota {} sua média é: {}".format(n,n2,(n+n2)/2))