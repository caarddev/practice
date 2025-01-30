import random

n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

ordem = random.sample([n1, n2, n3, n4], 4)

print(f'A ordem de apresentação dos alunos será: {ordem}')