#True
"""beecrowd | 1007
Diferenca
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferenca do produto de A e B pelo produto de C e D segundo a formula: DIFERENCA = (A * B - C * D).
Entrada
O arquivo de entrada contem 4 valores inteiros.
Saida
Imprima a mensagem DIFERENCA com todas as letras maiusculas, conforme exemplo abaixo, com um espaco em branco antes e depois da igualdade.
Exemplos de Entrada Exemplos de Saida
5
6
7
8
DIFERENCA = -26
0
0
7
8
DIFERENCA = -56
5
6
-7
8
DIFERENCA = 86"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
diferenca = (a*b - c*d)
print("DIFERENCA = {}".format(diferenca))