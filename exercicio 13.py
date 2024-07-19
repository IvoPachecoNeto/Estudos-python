#13 - Faça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa 
# e se ela é maior ou menor de idade. 

nome = input('nome:  ')
idade = float(input('idade:  '))

if idade >= 18:
    print(nome, "maior de idade")
else:
    print(nome, "menor de idade")