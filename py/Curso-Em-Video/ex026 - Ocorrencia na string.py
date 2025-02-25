frase = str(input('Digite uma frase: ')).strip().lower()
print(
    f'''A quantidade de letra A é {frase.count('a')}
A primeira letra A aparece na posicao {frase.find('a')+1}
A última letra A aparece na posicao {frase.rfind('a')+1}''')