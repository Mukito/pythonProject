#Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM percorrido? '))
dia = int(input('Quantos Dias Alugado '))
al_d = dia * 60
km_r = km * 0.15
total = al_d + km_r
print('{}KM, Valor por Rodagem R${}, valor de Aluguel {} dia é R${}, Total = R${}'
      .format(km, km_r, dia, al_d, total))
