#True
"""beecrowd | 1019
Conversao de Tempo
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia um valor inteiro, que e o tempo de duracao em segundos de um determinado evento em uma fabrica, e informe-o expresso no formato horas:minutos:segundos.
Entrada
O arquivo de entrada contem um valor inteiro N.
Saida
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
Exemplo de Entrada Exemplo de Saida
556
0:9:16
1
0:0:1
140153
38:55:53"""
a = int(input())
hora = int(a/60/60)
minuto = int((a - hora*60*60) / 60)
segundo = a%60
print(f"{hora}:{minuto}:{segundo}")