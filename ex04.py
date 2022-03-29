#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
#as informações possíveis sobre ele.

nome = input ("Digite algo : ")
print ("O tipo Primitivo desse valor é:",type(nome))
print ("È um Numerico? ",nome.isnumeric())
print("Só tem espaços?",nome.isspace())
print("È alfabetico?",nome.isalpha())
print("È alfanumérico?",nome.isalnum())
print("Está em maiuscula?",nome.isupper())
print("Está em minuscula?",nome.islower())
print("Está Capitalizada?",nome.istitle())
