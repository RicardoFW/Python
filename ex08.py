#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m =int(input("Escreva uma distância em metros "))
c = m*100
mm = m *1000
dam = m / 10
hm = m /100
km = m / 1000





print("{} Metros tem {} Centimetors e {} Milimetros ".format(m,c,mm))
print ("{} dam e {} hm e {} km".format(dam,hm,km))