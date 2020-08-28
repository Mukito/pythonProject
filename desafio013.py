#Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário,
# com 15% de aumento.


sal = float(input('Digite o valor do seu salario: R$'))
aum = sal + (sal * 15 / 100)
print('Salário R${:.2f}, com o aumento de 15% fica R${:.2f}'.format(sal, aum))