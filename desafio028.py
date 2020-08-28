import random
num = int(input('Adivinhe um numero Inteiro de 0 a 5: '))
a = random.randrange(0, 5)
print('Acertou!!! ' if (num == a) else 'Errou! ')
print('o numero sorteado foi {}, e voce escolheu {} '.format(a, num))