# 10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

trimestre1 = float (input("notas primeiro trimestre:  "))
trimestre2 = float (input("notas segundo  trimestre:  "))
trimestre3 = float (input("notas terceiro trimestre:  "))

resultado1 = trimestre1 + trimestre2 + trimestre3

resultado2 = resultado1 / 3

print('media anual: ', resultado2)