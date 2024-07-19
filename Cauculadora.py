
while True:
    valor_1 = float(input('primeiro valor do cauculo: '))
    print('(1) divisao')
    print('(2) multiplicaçao')
    print('(3) soma')
    print('(4) subtraçao')
    sinal = int(input('operaçao desejada:'  ))
    valor_2 = float(input('segundo valor do cauculo: '))

    divisao = valor_1 / valor_2
    multiplicaçao = valor_1 * valor_2
    soma = valor_1 + valor_2
    subtraçao = valor_1 - valor_2

    if sinal == 1:
        print(valor_1,'/',valor_2,'=',divisao)
    elif sinal == 2:
        print(valor_1,'*',valor_2,'=',multiplicaçao)
    elif sinal == 3:
        print(valor_1,'+',valor_2,'=',soma)
    else:
        print(valor_1,'-',valor_2,'=',subtraçao)
    input("tecle enter para continuar")
