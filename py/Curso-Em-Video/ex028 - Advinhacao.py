from random import randint
from time import sleep

pc = randint(0, 5)
adv = int(input('Tente advinhar um número de 1 a 5: '))
print('E o número que pensei está E...')
sleep(2.5)
if adv == pc:
    print(f'EXATO! Você acertou. O número que pensei foi {pc}!')
else:
    print(f'ERRADO! O número que pensei foi {pc} e não {adv}!\n')

