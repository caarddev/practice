from math import hypot
cat_oposto = float(input('Digite a medida do cateto oposto: '))
cat_adj = float(input('Digite a medida do cateto adjacente: '))
hip = hypot(cat_oposto, cat_adj)
print('A hipotenusa vale {:.2f}'.format(hip))