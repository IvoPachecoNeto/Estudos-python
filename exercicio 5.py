#5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos 
# salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

salario_usuario = float (input('valor do salario:'  ))
salario_minimo = 1293.20

qtdsm = salario_usuario / salario_minimo

print("salarios minimos o usuario ganha:  ", qtdsm)