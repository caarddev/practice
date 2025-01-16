import math
cat_oposto = int(input('Digite a medida do cateto oposto: '))
cat_adj = int(input('Digite a medida do cateto adjacente: '))
pitagoras = (cat_oposto ** 2) + (cat_adj ** 2)
hip = math.sqrt(pitagoras)
print('A hipotenusa vale {:.0f}'.format(hip))