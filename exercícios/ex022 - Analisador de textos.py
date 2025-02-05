nome = input('Digite seu nome completo: ').strip
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])}')