#20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

tabuada_do = int(input('numero:  '))

maior = tabuada_do * 10

stop = 0

while stop < maior:
    stop += tabuada_do
    print(stop)