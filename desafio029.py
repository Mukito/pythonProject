vel = float(input('Qual é a velocidade do Carro em KM/H: '))
r = (vel - 80) * 7
if (vel >= 81):
    print('"Acima da Velocidade permitida" - Voce foi Multado')
    print('Valor da Multa R${:.2f} '.format(r))
else:
    print('"Dentro da velocidade permitida"')