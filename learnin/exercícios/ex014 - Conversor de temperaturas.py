cel = float(input('Digite a temperatura em celsius(°C): '))
fah = cel * 9/5 + 32
kel = cel + 273.15
print('Convertendo {}°C para fahrenheit, ficará {}°F'.format(cel,fah))
print('Agora convertendo {}°C para kelvin, ficará {}°K'.format(cel,kel))