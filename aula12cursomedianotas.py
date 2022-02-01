nome = input ('Olá, bom dia ! Digite o nome do aluno(a) : ')
print('Agora vamos calcular a média final do {} !'.format(nome))
n1 = float ( input ('Informe a nota da primeira prova : '))
n2 = float ( input ('Informe a nota da segunda prova : '))
n3 = float ( input ('Informe a nota da terceira prova : '))
media = n1 + n2 + n3
mediafinal = media /3
print ('A média final do {}, foi : {}'.format(nome, mediafinal))