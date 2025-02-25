#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = (float(input("Digite a kilometragem da viagem percorrida: ")))
preco_viagem_curta = (distancia * 0.50)
preco_viagem_longa = (distancia * 0.45)
if distancia <= 200:
    print(f"Você pagará pela viagem de {distancia:.0f}, o valor de R${preco_viagem_curta:.2f}!")
else:
    print(f"Você fez {distancia:.0f}kms, e você pagará R${preco_viagem_longa:.2f}!")