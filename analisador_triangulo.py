print('-='*20)
print('Analisador de Triangulos ')
print('-='*20)

r1 = float(input('1° segmento: '))
r2 = float(input('2° segmento: '))
r3 = float(input('3° segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos acima PODEM Formar triângulo!! ')
else:
    print('Os segmentos acima NÂO PODEM Formar triângulo')


#=======================================================================

'''# -*- coding: utf-8 -*-

class Triangulo(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def validarForma(self):
        pass


# Caso positivo
triangulo = Triangulo(3, 4, 5)
assert triangulo.validarForma()

# Caso negativo
triangulo = Triangulo(1, 4, 5)
assert not triangulo.validarForma()

def validarForma(self):
    if (self.a < (self.b + self.c)):
        if (self.b < (self.a + self.c)):
            if (self.c < (self.a + self.b)):
                return True

    return False
'''
