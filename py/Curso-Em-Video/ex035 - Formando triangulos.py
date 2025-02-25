# Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite um segmento: '))
r2 = float(input('Digite outro segmento: '))
r3 = float(input('Digite mais um segmento: '))

if r1 < r2+r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos {r1}, {r2}, {r3} formam um triangulo.')
else:
    print(f'Nenhum desses segmentos formam um triangulo.')     