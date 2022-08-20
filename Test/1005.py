#True
"""beecrowd | 1005
Media 1
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia 2 valores de ponto flutuante de dupla precisao A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a media do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto e 11). Assuma que cada nota pode ir de 0 ate 10.0, sempre com uma casa decimal.
Entrada
O arquivo de entrada contem 2 valores com uma casa decimal cada um.
Saida
Imprima a mensagem "MEDIA" e a media do aluno conforme exemplo abaixo, com 5 digitos apos o ponto decimal e com um espaco em branco antes e depois da igualdade. Utilize variaveis de dupla precisao (double) e como todos os problemas, nao esqueca de imprimir o fim de linha apos o resultado, caso contrario, voce recebera "Presentation Error".
Exemplos de Entrada Exemplos de Saida
5.0
7.1
MEDIA = 6.43182
0.0
7.1
MEDIA = 4.84091
10.0
10.0
MEDIA = 10.00000"""
a = float(input())
b = float(input())
media = (a*3.5 + b*7.5) / 11
print("MEDIA = {:.5f}".format(media))