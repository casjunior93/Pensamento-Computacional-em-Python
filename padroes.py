# IDENTIFICAÇÃO DE PADRÕES

'''
->Ação de descrever o qua vai acontecer com base em eventos anteiores;
->Na computação, é comum utilizar estruturas de repetição, por exemplo, para blocos de código semelhantes que se repetem de alguma forma;
'''
arroz_kg = 7.00
feijao_kg = 9.00
carne_kg = 35.00

for i in range(3):
    print('Valor do produto:')
    valor = float(input())
    if valor <= 10.00:
        print('Posso comprar')
    else:
        print('Não posso comprar')
