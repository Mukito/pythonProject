sal = float(input('Digite o valor do seu Salario R$ '))


if (sal > 1250):
    au10 = (sal * 10) /100
    t1 = sal + au10
    print('Aumento de 10%, no valor de R${:.2f}, total = R${:.2f}'.format(au10, t1))
else:
    au15 = (sal * 15) /100
    t2 = sal + au15
    print('Aumento de 15%, no valor de R${:.2f}, total = R${:.2f} '.format(au15, t2))
