medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{} metros convertidos são\n{:.2f} quilômetros(km)\n{:.2f} hectômetros(hm)\n{:.1f} decâmetros(dam)'.format(medida,km,hm,dam))
print('{:.0f} decimetros(dm)\n{:.0f} centímetros(cm)\n{:.0f} milímetros(mm)'.format(dm,cm,mm))