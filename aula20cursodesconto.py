preco = float (input('Informe o preço do produto : R$'))
desconto = preco * (5/100)
total = preco - desconto
print ('O valor do produto é : R${:.2f}, após o desconto de 5% o valor fica em R${:.2f}'.format(preco, total))