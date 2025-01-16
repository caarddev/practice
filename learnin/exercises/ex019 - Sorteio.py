import random
n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
sorteio = random.choice([n1,n2,n3,n4])
print("Entre os alunos {}, {}, {} e {}.\nO escolhido pra limpar o quadro foi o {}"
      .format(n1,n2,n3,n4,sorteio))