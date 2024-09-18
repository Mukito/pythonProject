#Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

conv = float(input('Informe a temperatura °C '))
f = ((9 * conv) / 5) + 32
print('A temperatura de {} °C corresponde a {} °F!!'.format(conv, f))
