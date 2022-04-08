#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desco

pd = float(input("Qual é preço do produto R$: "))
dsc = pd - (pd * 5/100)
print("O valor do produto sem disconto é {} e novo valor com desconto é R$: {:.2f}".format(pd,dsc))
