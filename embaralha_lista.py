import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação sera ')
print(lista)
