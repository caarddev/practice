dias = int(input('Quantos dias você utilizou o carrro? '))
kms = float(input('Quantos Kms voce rodou? '))
diaria = (dias * 60) + (kms * 0.15)
print('Voce usou o carro por {dias:.0f} e andou {kms:.1f}kms, o total a pagar é R${diaria:.2f}')