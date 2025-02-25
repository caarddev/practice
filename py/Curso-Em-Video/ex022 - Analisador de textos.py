nome = str(input('Digite seu nome: ')).strip()
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
print(f'''Seu nome com letras maiúsculas: {nomeMaiusculo}
Seu nome com letras minúsculas: {nomeMinusculo}
Seu nome tem ao todo {len(nome) - nome.count(' ')} letras
Seu primeiro é {nome.split()[0]} nome tem {len(nome.split()[0])} letras''')