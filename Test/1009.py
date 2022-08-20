#True
"""beecrowd | 1009
Salario com Bonus
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Faca um programa que leia o nome de um vendedor, o seu salario fixo e o total de vendas efetuadas por ele no mes (em dinheiro). Sabendo que este vendedor ganha 15% de comissao sobre suas vendas efetuadas, informar o total a receber no final do mes, com duas casas decimais.
Entrada
O arquivo de entrada contem um texto (primeiro nome do vendedor) e 2 valores de dupla precisao (double) com duas casas decimais, representando o salario fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.
Saida
Imprima o total que o funcionario devera receber, conforme exemplo fornecido.
Exemplos de Entrada Exemplos de Saida
JOAO
500.00
1230.30
TOTAL = R$ 684.54
PEDRO
700.00
0.00
TOTAL = R$ 700.00
MANGOJATA
1700.00
1230.50
TOTAL = R$ 1884.58"""
nome = input()
salario = float(input())
comissao = float(input())
print("TOTAL = R$ {:.2f}".format(salario+comissao*0.15))