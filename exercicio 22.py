#21 - Faça um algoritmo que efetue o cálculo do salário líquido de um professor. As informações fornecidas serão: 
# valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário
#  líquido final.

inss = float(input('INSS:  '))
valor_hora = float(input('valor da hora trabalhada:  '))
aulas_no_mes = int(input('quantidade de aulas dadas no mes:  '))

salario_base = valor_hora * aulas_no_mes
salario_liquido = salario_base - inss

print('salario liquido:  ', salario_liquido)
