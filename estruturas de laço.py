lista = ['arrascaeta', 'rodinei', 'vitinho', 'felipe luis']

for nome in lista:
    print(nome)

print('=' * 35)

lista_num = range(5)

for item in lista_num:
    print(item)

print('=' * 35)

i = 0

while i <= 10:
    print('i ainda é menor do que 10 : {}'.format(i))
    i += 1

print('Acabou o while: {}'.format(i))

print('=' * 35)

numero = 0

while True:
    print(numero)
    if numero == 10:
        break
    numero += 1