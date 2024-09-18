ano = int(input('Escreva o Ano: '))
if (ano % 4 == 0 and ano % 100 != 0): #(ano % 400 == 0)
    print(('Bissexto'))
else:
    print('Não é Bissexto')
