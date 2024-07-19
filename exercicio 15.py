#16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são 
# válidos, determine se o triângulo é equilátero, isósceles ou escaleno.

#ESCALENO TODOS OS LADOS DIFERENTES
#ISOCELES 2 LADOS TEM O MESMO VALOR
#EQUILATERO TODOS OS LADOS SAO IGUAIS 


lado1 = float(input("medida 1:  "))
lado2 = float(input("medida 2:  "))
lado3 = float(input('medida 3:  '))

if lado1 == lado2 == lado3:
    print('equilatero')
elif lado1 == lado2:
    print('isoceles')
elif lado1 == lado3:
    print('isoceles')
elif lado2 == lado3:
    print('isoceles')
else:
    print('escaleno')