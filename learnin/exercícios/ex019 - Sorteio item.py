from random import choice
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

lista = [n1, n2, n3, n4]
escolha = choice(lista)
print("O(a) escolhido(a) pra limpar o quadro foi {}".format(n1,n2,n3,n4,escolha))