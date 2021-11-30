real = float(input('Quanto você possuí em sua carteira ? R$ '))
dolar = real / 5.52
euro = real / 6.40
libra = real / 7.5
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode compra £{:.2f}'.format(real, libra))