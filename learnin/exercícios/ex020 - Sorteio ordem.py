import random

n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')

ordem = random.sample([n1, n2, n3, n4], 4)

print('A ordem de apresentação dos alunos será: {}'.format(ordem))