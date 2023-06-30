print('Bem Vindo a Loja da Mayara Santos de Castro')
# Informações de compra para cálculo.
produto = float(input('Valor do produto: '))
qtd = int(input('Quantidade do produto: '))
sub_total = produto * qtd

# Cálculo do valor de compra até 9 unidades.
if qtd > 1 and qtd <= 9:
    print('O valor sem desconto foi: R$ {:.2f}'.format(sub_total))
    print('Ganhe desconto a partir de 10 quantidades!')

# Aplicando 5% de desconto a partir de 10 unidades
elif qtd >= 10 and qtd <= 99:
        d1 = sub_total * 0.05
        t1 = (produto * qtd) - d1
        print('O valor sem desconto foi: R$ {:.2f}'.format(sub_total))
        print('O valor com desconto foi: R$ {:.2f} (desconto 5%)'.format(t1))

# Aplicando 10% de desconto a partir de 100 unidades
elif qtd >= 100 and qtd <= 999:
        d2 = sub_total * 0.10
        t2 = (produto * qtd) - d2
        print('O valor sem desconto foi: R$ {:.2f}'.format(sub_total))
        print('O valor com desconto foi: R$ {:.2f} (desconto 10%)'.format(t2))

# Aplicando 15% de desconto a partir de 1000 unidades
elif qtd >= 1000:
        d3 = sub_total * 0.15
        t3 = (produto * qtd) - d3
        print('O valor sem desconto foi: R$ {:.2f}'.format(sub_total))
        print('O valor com desconto foi: R$ {:.2f} (desconto 15%)'.format(t3))

# Saida para zero quantidade.
else:
    print('Erro. Verifique se os valores foram inseridos.')



