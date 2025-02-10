import time
print('Calculadora de índice de massa corporal.')
time.sleep(1.0)

peso = float(input('Digite seu peso: '))
time.sleep(0.5)
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)
print('Calculando...')
time.sleep(2.0)

print(f'Seu índice de massa corporal é de {imc:.2f}')

if imc < 16:
    print('Você está com magreza severa. Procure um médico para avaliação.')
elif imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal. Parabéns!')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 35:
    print('Você tem obesidade grau I.')
elif imc < 40:
    print('Você tem obesidade grau II.')
else:
    print('Você tem obesidade grau III (mórbida). Recomenda-se acompanhamento médico.')