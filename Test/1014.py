#True
"""beecrowd | 1014
Consumo
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Calcule o consumo medio de um automovel sendo fornecidos a distancia total percorrida (em Km) e o total de combustivel gasto (em litros).
Entrada
O arquivo de entrada contem dois valores: um valor inteiro X representando a distancia total percorrida (em Km), e um valor real Y representando o total de combustivel gasto, com um digito apos o ponto decimal.
Saida
Apresente o valor que representa o consumo medio do automovel com 3 casas apos a virgula, seguido da mensagem "km/l".
Exemplo de Entrada Exemplo de Saida
500
35.0
14.286 km/l
2254
124.4
18.119 km/l
4554
464.6
9.802 km/l"""
a = int(input())
b = float(input())
print("{:.3f} km/l".format(a/b))