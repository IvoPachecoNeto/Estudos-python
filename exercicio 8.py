#8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.
#funcao .sort() é usado do mesmo jeito que append mas ao invez de adicionar ele ordena os numeros dentro de uma lista

lista= []

for x in range (3):
    valor = float (input('valor:  '))
    valores = [valor]
    lista.append(valores)
    lista.sort()

print ('valores veificados', lista)
