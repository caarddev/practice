from math import hypot
cat_oposto = float(input('Digite a medida do cateto oposto: '))
cat_adj = float(input('Digite a medida do cateto adjacente: '))
hip = hypot(cat_oposto, cat_adj)
print(f'A hipotenusa vale {hip:.2f}')