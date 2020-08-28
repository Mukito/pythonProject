n = str(input('Escreva seu nome completo: ')).upper().strip()
# faz a contagem das strings
nome = n.split()
# imprime o primeiro nome
print('Seu primeiro nome é {} ' .format(nome[0]))
# imprime o ultimo nome
print('Seu útimo nome é {} '.format(nome[len(nome)-1]))
