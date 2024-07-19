#6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

valor1 = float(input('valor para reajuste de 5%:  '))

resultado = valor1 * 5
resultado2 = resultado / 100

print('valor ajustado:  ', resultado2 + valor1)