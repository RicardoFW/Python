#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input("Digite um numero: "))
d = n*2
t = n*3
r= n ** (1/2)

print ("O dobro de {} é {}".format(n,d))
print ("O Triplo de {} é {} e sua raiz quadrada de {} é {:.2f}".format(n,t,n,r))
                           #ou
print ("\nO Dobro de {} é {} O triplo de {} é {} e sua raz quadrada de {} é {} ".format(n,(n*2),n,(n*3),n,(n**(1/2))))