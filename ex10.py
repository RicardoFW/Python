#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
print("Seu Saldo é R$ 89,69 Reais \n")

vr = float(input("Digite o valor do Seu Saldo e veja quantos Dolares você pode comprar R$ "))

dolar = vr / 4.65
euro = vr / 5.08

print("Com o R$ {} reais voce pode comprar US$ {:.2f} Dolares ".format(vr,dolar))
print("Com o R$ {} reais voce pode comprar  $E {:.2f}  Euros ".format(vr,euro))
