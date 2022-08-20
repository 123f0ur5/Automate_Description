#True
"""beecrowd | 1010
Calculo Simples
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Neste problema, deve-se ler o codigo de uma peca 1, o numero de pecas 1, o valor unitario de cada peca 1, o codigo de uma peca 2, o numero de pecas 2 e o valor unitario de cada peca 2. Apos, calcule e mostre o valor a ser pago.
Entrada
O arquivo de entrada contem duas linhas de dados. Em cada linha havera 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
Saida
A saida devera ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaco apos os dois pontos e um espaco apos o "R$". O valor devera ser apresentado com 2 casas apos o ponto.
Exemplos de Entrada Exemplos de Saida
12 1 5.30
16 2 5.10
VALOR A PAGAR: R$ 15.50
13 2 15.30
161 4 5.20
VALOR A PAGAR: R$ 51.40
1 1 15.10
2 1 15.10
VALOR A PAGAR: R$ 30.20"""
a, b, c = input().split()
d, e, f = input().split()
print("VALOR A PAGAR: R$ {:.2f}".format(int(b)*float(c)+int(e)*float(f)))