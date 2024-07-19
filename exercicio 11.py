# 11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas
# imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado. Para o aluno ser considerado
# aprovado sua média final deve ser maior ou igual a 7.

nome = input('nome do aluno:  ')
bimestre1 = float (input("notas primeiro bimestre:  "))
bimestre2 = float (input("notas segundo  bimestre:  "))
bimestre3 = float (input("notas terceiro bimestre:  "))
bimestre4 = float (input("notas terceiro bimestre:  "))

resultado1 = bimestre1 + bimestre2 + bimestre3 + bimestre4
resultado2 = resultado1 / 4

if resultado2 >= 7.0:
    print('aprovado')
else:
    print('reprovado')