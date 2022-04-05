#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print("Preencha os dados requeridos a baixo  para saber quantos litros de tinta você precisara para pinta-la. ")
l = float(input("Digite qual é a largura da parede "))
a = float(input("Digite a altura da parede "))
vl = l*a /2
print("Sua parede tem a dimensão de {} x {} e sua área e de {}m² para pintar essa aréa você precisara de : {:.2f} litros de tinta"
      .format(l,a,a*l,(vl)))
