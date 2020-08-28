frase = str(input('Escreva uma frase: ')).upper().strip()
# conta quantas vezes aparece a letra pedida
print('A letra A aparece {} Veses '.format(frase.count('A')))
# mostra a posição da primeira vez aparecida
print('Ela aparece pela 1° vez na posição {} '.format(frase.find('A')+1))
# mostra a posição da ultima vez paracedida
print('Ela aparece pela ultima vez na posição {} '.format(frase.rfind('A')+1))