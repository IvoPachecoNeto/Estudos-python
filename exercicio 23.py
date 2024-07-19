#22 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o
#  carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade
#  média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

#12km com um litro
#qunatidade de combustivel
#velocidade
#litros

distancia = float(input('distancia a percorrer em Km:  '))
combustivel = float(input('valor atual do combustuvel:  '))
velocidade = 65
tempo = distancia / velocidade
litros = distancia / 12
valor_gasto = combustivel * litros

print('tempo medio:  ',tempo)
print('velocidade media:  ', velocidade)
print('combustivel necessarios: ',litros)
print('distancia percorrida: ', distancia)
print('autonomia do veiculo: 12kM/h')
print('valor gasto em combustivel', valor_gasto)

