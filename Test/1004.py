#True
"""beecrowd | 1004
Produto Simples
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operacao a variavel PROD. A seguir mostre a variavel PROD com mensagem correspondente.   
Entrada
O arquivo de entrada contem 2 valores inteiros.
Saida
Imprima a mensagem "PROD" e a variavel PROD conforme exemplo abaixo, com um espaco em branco antes e depois da igualdade. Nao esqueca de imprimir o fim de linha apos o produto, caso contrario seu programa apresentara a mensagem: "Presentation Error".
Exemplos de Entrada Exemplos de Saida
3
9
PROD = 27
-30
10
PROD = -300
0
9
PROD = 0"""
a = int(input())
b = int(input())
print("PROD = {}".format(a*b))