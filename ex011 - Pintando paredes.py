larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = larg*alt
print('A dimensão da sua parede é de {} x {}, e sua área é de {}'.format(larg,alt,area))
tinta = area/2
print('Você precisará de {}l de tinta para pintar a parede.'.format(tinta))