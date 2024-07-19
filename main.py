print("Minha esposa nao deixa eu estudar")
#print mostra na tela
resposta_1 = input("ela é má por isso?")
#input mosttra na tela e espera a resposta do  usuario
resposta_2 = int(input("qual a chance de eu estudar o dia inteiro"))
#int converte para numero inteiro 
resposta_3 = float(input("de dia é hj?"))
#float converte numero decimal

print(type(resposta_2))
print(type(resposta_3))
#tipe mostra o tipo de variavel 
 
#contas basicas 
soma = 11 + 2
multiplicaçao = 3 * 4
divisao = 12/4
potencia = 7 ** 2

print("soma", soma)
print("multiplicaçao", multiplicaçao)
print("divisao", divisao)
print("potencia", potencia)

# bloco de instruçao é um tab
# if, elif e else (else nao possui variaçao) sao testes que detende 
# da resposta para ter uma açao
idade = float (input("informe sua idade"))
if idade >= 18:
    print("permitido!")
elif idade < 18 and idade >= 49:
    print("bloqueado!")

#listas podem ser vizualisadas com a []
#listas tbm podem ser alteradas com [] = *

lista_numeros = [1,2,3,4,5,6,7,8,9]

lista_numeros [0] = 23

print(lista_numeros[0])
#listas vazias podem ser preenchidas com .append
#para ver todos os itens da lista se usa len
#para ver o menor valor se usa min
#para ver o maior valor se usa max

print("total:", len(lista_numeros))
print("maior valor", max(lista_numeros))
print("menor valor", min(lista_numeros))

#repetiçao(loop)
#loops definidos pode usar o for
#o x vale é um valor que é alterado a cada loop
#ranger limita o x a uma quantidade especifica

notas = []

for x in range (5):
    codigo = input("Rm: ")
    nota = float(input("nota: "))
    resultado = [codigo, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas))

for n in notas:
    codigo = n[0]
    nota = n[1]
    print("Rm", codigo, "tirou nota", nota)

