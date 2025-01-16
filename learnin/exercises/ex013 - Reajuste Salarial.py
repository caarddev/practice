salario = float(input('Digite seu salário para aumento: '))
aumento = 15
bonus = (salario * aumento)/ 100
salarionovo = salario + bonus
print('Você ganhou um bônus de 15% no seu salário. Seu bônus foi de R${:.2f}'.format(bonus))
print('Seu salário era R${:.2f} e foi aumentado para R${:.2f}.'.format(salario,salarionovo))