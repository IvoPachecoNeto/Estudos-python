#1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma 
# entre A e B é mostre se a soma é menor que C.

valor1 = float (input("valor A:  "))
valor2 = float (input("valor B:  "))
valor3 = float (input("valor C:  "))
simbulo = (input("operaçao:  "))
soma = valor1 + valor2

if valor3 >= soma:
    print("maior que:", soma),
elif valor3 <= soma:
    print(valor3, soma)
    

