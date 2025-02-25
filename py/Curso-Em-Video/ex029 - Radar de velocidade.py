vel = float(input('Digite a velocidade: '))
if vel < 80:
    print('Você está no limite da via, aproveite a viagem.')
else:
    multa = (vel - 80) * 7
    print(f'Você ultrapassou o limite de velocidade em {(vel - 80):.0f}km/h.')
    print(f'Multa aplicada no total de R${multa:.2f}')