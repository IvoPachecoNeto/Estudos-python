#18 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano.
# Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja maior 
# que Sara.

nome1 = input('nome:  ')
autura1 = int(input('autura:  '))
nome2 = input('nome 2:  ')
autura2 = int(input('nome2:  '))

ano = 0

crecimento1 = 2
crecimento = 3

while autura2 < autura1:
    autura1 += crecimento1
    autura2 += crecimento 
    ano += 1
print (nome2, ano, "anos")