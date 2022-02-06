#var_verdade = True
#var_falso = False

#Comparações : == != > < >= <=
#Comparações : and / or

#a = 50
#b = 20

#if a > b and 'abacaxi' == 'abacaxi':
#    print(a, 'é maior que', b)
#else:
#    print('Não deu certo o if')

print('Times:\n1 = Flamengo\n2 = Vasco\n3 = Fluminense\n4 = Botafogo')

opcao = input('Escolha um time:')

if opcao == '1':
    print('Ok, vamos lá flamenguista !')
elif opcao == '2':
    print('Vambora vascaino sofredor !')
elif opcao == '3':
    print('Vamo nessa tricolor bambi')
elif opcao == '4':
    print('Show botafoguense safado')
else:
    print('Opção inválida!')