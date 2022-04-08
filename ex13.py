#exercício Python 013: Faça um algoritmo que leia o salário de um
#funcionário e mostre seu novo salário, com 15% de aumento.

sl = float(input("Qual é o valor do Seu Salário? R$:"))
dsc = sl + (sl *15/100)
print ("Seu salario atual é: {} Teve um reajuste  de 15% seu novo salário é R$:{:.2f}\n".format(sl,dsc))


vp = float(input("Digite o valor do seu produto: R$"))
avista = vp - (vp*18/100)
aprazo = vp + (vp*15/100)
dscc = (vp*15/100)
print("o valor atual do produto é R$:{}\nPagamento avista você ganha  18%  de desconto R$:{:.2f} \nem aprazo aumento de 15% R$:{:.2f}"
.format(vp,avista,aprazo))




