lar = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
A = lar * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(lar, alt, A))
tinta = A / 2
print('Para pintar essa parede, vôce precisará de {}L de tinta'.format(tinta))