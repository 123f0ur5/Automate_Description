#True
"""beecrowd | 1020
Idade em Dias
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia um valor inteiro correspondente a idade de uma pessoa em dias e informe-a em anos, meses e dias
Obs.: apenas para facilitar o calculo, considere todo ano com 365 dias e todo mes com 30 dias. Nos casos de teste nunca havera uma situacao que permite 12 meses e alguns dias, como 360, 363 ou 364. Este e apenas um exercicio com objetivo de testar raciocinio matematico simples.
Entrada
O arquivo de entrada contem um valor inteiro.
Saida
Imprima a saida conforme exemplo fornecido.
Exemplo de Entrada Exemplo de Saida
400
1 ano(s)
1 mes(es)
5 dia(s)
800
2 ano(s)
2 mes(es)
10 dia(s)
30
0 ano(s)
1 mes(es)
0 dia(s)"""
a = int(input())
ano = int(a/365)
mes = int((a - ano*365) / 30)
dia = a%365%30

print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)")