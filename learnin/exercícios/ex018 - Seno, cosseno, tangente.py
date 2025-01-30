from math import sin, cos, tan, radians
angulo = int(input('Insira um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno do angulo {angulo}° é igual a {seno}:.2f}')
print(f'O cosseno do angulo {angulo}° é igual a {cosseno:.2f}')
print(f'A tangente do angulo {angulo}° é igual a {tangente:.2f}')