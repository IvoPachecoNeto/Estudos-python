#15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias 
# essa pessoa ja viveu. Leve em consideração o ano com 365 dias e o mês com 30 dias.

dia1= int(input("dia de hoje:  "))
mes1= int(input("mes de hoje:  "))
ano1= int(input("ano de hoje:  "))

dia2= int(input("dia de nacimento:  "))
mes2= int(input("mes de nacimento:  "))
ano2= int(input("ano de nacimento:  "))

anos= ano1 - ano2
meses= mes1 - mes2
dias= dia1 - dia2

if dias < 0:
    dias += 30
    meses -= 1

if meses < 0:
    meses += 12
    anos -= 1

print(dias, '/', meses, '/', anos)
