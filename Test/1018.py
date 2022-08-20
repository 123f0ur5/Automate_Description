#True
"""beecrowd | 1018
Cedulas
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia um valor inteiro. A seguir, calcule o menor numero de notas possiveis (cedulas) no qual o valor pode ser decomposto. As notas consideradas sao de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relacao de notas necessarias.
Entrada
O arquivo de entrada contem um valor inteiro N (0 < N < 1000000).
Saida
Imprima o valor lido e, em seguida, a quantidade minima de notas de cada tipo necessarias, conforme o exemplo fornecido. Nao esqueca de imprimir o fim de linha apos cada linha, caso contrario seu programa apresentara a mensagem: "Presentation Error".
Exemplo de Entrada Exemplo de Saida
576
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
11257
11257
112 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
0 nota(s) de R$ 1,00
503
503
5 nota(s) de R$ 100,00
0 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
0 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00"""
import math
a = int(input())
print(a)
print("{:.0f} nota(s) de R$ 100,00".format(math.floor(a/100)))
print("{:.0f} nota(s) de R$ 50,00".format(math.floor(a%100/50)))
print("{:.0f} nota(s) de R$ 20,00".format(math.floor(a%100%50/20)))
print("{:.0f} nota(s) de R$ 10,00".format(math.floor(a%100%50%20/10)))
print("{:.0f} nota(s) de R$ 5,00".format(math.floor(a%100%50%20%10/5)))
print("{:.0f} nota(s) de R$ 2,00".format(math.floor(a%100%50%20%10%5/2)))
print("{:.0f} nota(s) de R$ 1,00".format(math.floor(a%100%50%20%10%5%2)))