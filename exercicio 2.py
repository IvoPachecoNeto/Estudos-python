#2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar
#  positivo ou negativo.

numero1 = float (input("digite o numero a verificar:   "))
divisor = 2

if numero1 / divisor <= 0:
    print('impar')
elif numero1 / divisor >= 0:
    print('pàr')
    