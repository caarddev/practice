salario = float(input('Digite seu salário para aumento: '))
aumento = 15
bonus = (salario * aumento)/ 100
salarionovo = salario + bonus
print(f'Você ganhou um bônus de 15% no seu salário. Seu bônus foi de R${bonus:.2f}')
print(f'Seu salário era R${salario:.2f} e foi aumentado para R${salarionovo:.2f}.')