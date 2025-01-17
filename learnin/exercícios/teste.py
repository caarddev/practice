import random

# Pergunte os nomes dos alunos
nomes = []
for i in range(4):
    nome = input(f'Digite o nome do aluno {i+1}: ')
    nomes.append(nome)

# Embaralhe a lista de nomes
random.shuffle(nomes)

# Imprima a ordem de apresentação
print('A ordem de apresentação dos alunos será:')
for i, nome in enumerate(nomes, start=1):
    print(f'{i}. {nome}')