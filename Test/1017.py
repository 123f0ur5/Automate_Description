#True
"""beecrowd | 1017
Gasto de Combustivel
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Joaozinho quer calcular e mostrar a quantidade de litros de combustivel gastos em uma viagem, ao utilizar um automovel que faz 12 KM/L. Para isso, ele gostaria que voce o auxiliasse atraves de um simples programa. Para efetuar o calculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade media durante a mesma (em km/h). Assim, pode-se obter distancia percorrida e, em seguida, calcular quantos litros seriam necessarios. Mostre o valor com 3 casas decimais apos o ponto.
Entrada
O arquivo de entrada contem dois inteiros. O primeiro e o tempo gasto na viagem (em horas) e o segundo e a velocidade media durante a mesma (em km/h).
Saida
Imprima a quantidade de litros necessaria para realizar a viagem, com tres digitos apos o ponto decimal
Exemplo de Entrada Exemplo de Saida
10
85
70.833
2
92
15.333
22
67
122.833"""
a = int(input())
b = int(input())
print("{:.3f}".format(float((a*b)/12)))