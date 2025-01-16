n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
ex = n1 ** n2
print(
    'A soma entre {} e {} no total é {}\njá a multiplicação é {}, a divisao é {}, subtraindo temos {}\n'
    'E a potencializacao é {:.1f}'.format(n1, n2, s, m, d, sub, ex))
