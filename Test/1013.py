#True
"""beecrowd | 1013
O Maior
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Faca um programa que leia tres valores e apresente o maior dos tres valores lidos seguido da mensagem "eh o maior". Utilize a formula:
Entrada
O arquivo de entrada contem tres valores inteiros.
Saida
Imprima o maior dos tres valores seguido por um espaco e a mensagem "eh o maior".
Exemplos de Entrada Exemplos de Saida
7 14 106
106 eh o maior
217 14 6
217 eh o maior"""
valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
ab = ((a+b+abs(a-b))/2)
bc = ((ab+c+abs(ab-c))/2)
print("{:.0f} eh o maior".format(bc))