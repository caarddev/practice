# beecrowd | 1010

cod1, qtd1, valor1 = input().split()
cod2, qtd2, valor2 = input().split()

qtd1 = int(qtd1)
valor1 = float(valor1)
qtd2 = int(qtd2)
valor2 = float(valor2)

calc = (qtd1 * valor1) + (qtd2 * valor2)

print(f"VALOR A PAGAR: R$ {calc:.2f}")