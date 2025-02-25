valor = float(input('Insira um valor: R$'))
porcentagem = 5
calc = (valor * porcentagem) / 100
total = valor - calc
print(f'Você ganhou um desconto de 5% de desconto! Você economizou R${calc:.2f}\nEm vez de pagar R${valor:.2f}, você pagará R${total:.2f}!')