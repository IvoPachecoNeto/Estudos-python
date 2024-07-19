# 12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a 
# escolha da forma de pagamento pelo comprador e imprima na tela o valor final do produto a ser pago. 
# Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
# Tabela de Código de Condições de Pagamento
# 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
# 2 - À Vista no cartão de crédito, recebe 10% de desconto
# 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
# 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%


nome_do_produto = input('nome do produto:  ')
preço = float (input('preço:  '))
print("(1)credito")
print("(2)pix ou dinheiro")
print("(3)parcelado 2x")
print("(4)parcelado 3x")
pagemento = float (input("forma de pagamento: "))

din_pix1 = preço * 15
din_pix2 = din_pix1 /100
din_pix3 = preço - din_pix2

credito1 = preço * 10
credito2 = credito1 /100
credito3 = preço - credito2

parce3x1 = preço * 10
parce3x2 = parce3x1 /100
parce3x3 = preço + parce3x2 

if pagemento == 1:
    print('valor a pagar', credito3)

elif pagemento == 2:
    print('valor a pagar', din_pix3)

elif pagemento == 3:
    print('valor a pagar', preço)

elif pagemento == 4:
    print('valor a pagar', parce3x3)

print(nome_do_produto)
