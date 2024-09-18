import math

an = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(an))
print('O Angulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O Angulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))
