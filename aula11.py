# cores no terminal  ANSI ctrl \
# \033[ style text back m
# style = 0, 1, 4, 7
# text  = 30, 31, 32, 33, 34, 35, 36, 37
# back  = 40, 41, 42, 43, 44, 45, 46, 47,
# abrir e fechar "\033[m"
print('\033[0:30:41mOla Mundo\033[m')
print('\033[4:33:44mOla Mundo')
print('\033[1:35:43mOla Mundo')
print('\033[30:42mOla Mundo')
print('\033[mOla Mundo')
print('\033[7:30mOla Mundo')

