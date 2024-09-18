dist = float(input('Qual a distância a ser percorido em KM: '))
v1 = dist * 0.50
v2 = dist * 0.45
if (dist <=200):
    print('O valor é da viagem é R${:.2f} '.format(v1))
else:
    print('Viagem mais longa - Valor Promocional R${:.2f} '.format(v2))
