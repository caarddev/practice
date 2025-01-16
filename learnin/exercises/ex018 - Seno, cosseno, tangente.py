import math
angulo = int(input('Insira um angulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O seno do angulo {} é igual a {}'.format(angulo,seno))
print('O cosseno do angulo {} é igual a {}'.format(angulo,cosseno))
print('A tangente do angulo {} é igual a {}'.format(angulo,tangente))