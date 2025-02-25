n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}\nE o seu último nome é {nome[len(nome)-1]}')