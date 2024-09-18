num1 = int(input('Digite 1° numero: '))
num2 = int(input('Digite 2° numero: '))
num3 = int(input('Digite 3° numero: '))

lista = [num1, num2, num3]
maior = max(lista)
menor = min(lista)
print('o maior é {} e o menor é {} '.format(maior, menor) )

#=====================================================================
#if (num1 > num2 and num1 > num3):
#    print('O numero maior é {} '.format(num1))
#elif (num2 > num1 and num2 > num3):
#    print('O numero maior é {} '.format(num2))
#else:
#    print('o numero maior é {} '.format(num3))
#=====================================================================
#achando o numero maior
#maior = num1
#if (num2 > maior):
#    maior = num2
#    if (num3 > maior):
#        maior = num3
#       print('Maior: ', maior)

#achando o numero menor
#menor = num1
#if (num2 < menor):
#    menor = num2
#    if (num3 < menor):
#        menor = num3
#        print('Menor: ', menor)
#====================================================================
#num1 = int(input('Digite 1° numero: '))
#num2 = int(input('Digite 2° numero: '))
#num3 = int(input('Digite 3° numero: '))

#if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
#    print('PODEM formar Triangulo')
#else:
#    print('NAO PODEM formar Triangulo')
