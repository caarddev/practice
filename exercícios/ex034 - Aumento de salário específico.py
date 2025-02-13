# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário atual: '))

if salario <= 1250:
    salario = (salario * 15)/100 + salario
    print(f'Você recebeu um aumento de 15%, agora você recebe R${salario:.2f}!')

else:
    salario = (salario * 10)/100 + salario
    print(f'Seu aumento foi de 10%, você receberá R${salario}!')