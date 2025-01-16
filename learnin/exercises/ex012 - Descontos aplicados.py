valor = float(input('Insira um valor: R$'))
porcentagem = 5
calc = (valor * porcentagem) / 100
total = valor - calc
print('Você ganhou um desconto de 5% de desconto! Você economizou R${:.2f}\nEm vez de pagar R${:.2f}, você pagará R${:.2f}!'
      .format(calc,valor,total))