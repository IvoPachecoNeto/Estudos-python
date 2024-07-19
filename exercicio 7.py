#7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.

numeros_logicos1= input('valor borleanos 1: ')
numeros_logicos2= input('valor borleanos 2: ')

valor_logico1 = numeros_logicos1.lower() == 'true'
valor_logico2 = numeros_logicos2.lower() == 'true'

if valor_logico1 and valor_logico2:
    print('Ambos são VERDADEIRO.')
elif not valor_logico1 and not valor_logico2:
    print('Ambos são FALSO.')
else:
    print('Um é VERDADEIRO e o outro é FALSO.')



