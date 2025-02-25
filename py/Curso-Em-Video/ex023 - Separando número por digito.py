num = int(input('Digite um numero: '))
print(f'''
      Analisando o número {num} temos:
      Unidade: {num//1 % 10}
      Dezena: {num//10 % 10}
      Centena: {num//100 % 10}
      Milhar: {num//1000 % 10}''')