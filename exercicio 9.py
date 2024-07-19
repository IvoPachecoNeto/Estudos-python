#9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua 
# altura e imprima na tela sua condição 

# cauculo: divide-se o peso do paciente pela sua altura elevada ao quadrado

peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}: Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print(f'Seu IMC é {imc:.2f}: Peso ideal (parabéns)')
elif 25.0 <= imc < 29.9:
    print(f'Seu IMC é {imc:.2f}: Levemente acima do peso')
elif 30.0 <= imc < 34.9:
    print(f'Seu IMC é {imc:.2f}: Obesidade grau I')
elif 35.0 <= imc < 39.9:
    print(f'Seu IMC é {imc:.2f}: Obesidade grau II (severa)')
else:  # imc >= 40
    print(f'Seu IMC é {imc:.2f}: Obesidade grau III (mórbida)')
