medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'{medida} metros convertidos são\n{km:.2f} quilômetros(km)\n{hm:.2f} hectômetros(hm)\n{dam:.1f} decâmetros(dam)')
print(f'{dm:.0f} decimetros(dm)\n{cm:.0f} centímetros(cm)\n{mm:.0f} milímetros(mm)')