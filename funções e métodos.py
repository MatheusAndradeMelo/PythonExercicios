def soma (numero1, numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(75, 82)

print(retorno)

print('=' * 30)

def palavra (argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

if palavra([1,2,3,4,5,6,7]):
    print("Tem sete letras")

print('=' * 30)

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

print(maior([1,-2,1.2, 87.2, 1289, -7,0]))

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([1,-2,1.2, 87.2, 1289, -7,0]))