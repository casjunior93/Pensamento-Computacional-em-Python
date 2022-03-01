# DECOMPOSIÇÃO

'''
-> Ação de dividir um problema maior em partes menores;
-> A ideia é resolver as partes do problema para então obter uma resposta do problema maior;
->Na computação, quando escrevemos algum software ou código, geralmente dividimos a escrita em partes mnores que vão sendo construídas aos poucos
'''

descontos = 300.00
salario_fixo = 1600.00
vendas_mes = 50
comissao = 20
valor_total_vendas = vendas_mes * comissao

valor_salario_liquido = (salario_fixo + valor_total_vendas) - descontos

print(' ')
print(valor_salario_liquido)
