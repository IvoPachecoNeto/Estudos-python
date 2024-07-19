#17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau 
# Celsius. Imprima na tela as duas temperaturas.
# Fórmula: 

f = int(input('Temperatura em fahrenhent:  '))

C = (5 * (f-32) / 9)

print('temperatura convertida em graus celsius:  ', C)