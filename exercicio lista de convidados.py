print('=' * 12, 'LISTA DE CONVIDADOS', '=' * 12)

num_convidados = input('Informe quantos convidados terão na sua festa: ')
lista_convidados = []

i = 1
while i <= int(num_convidados):
    nome_convidado = input('Digite o nome do convidado #{}: '.format(i))
    lista_convidados.append(nome_convidado)
    i += 1

print('\nSerão ao todo: {} convidados na sua festa!'.format(num_convidados))
print('\nLISTA DE CONVIDADOS:')

for convidado in lista_convidados:
    print(convidado)

