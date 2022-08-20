#True
"""beecrowd | 1006
Media 2
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia 3 valores, no caso, variaveis A, B e C, que sao as tres notas de um aluno. A seguir, calcule a media do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 ate 10.0, sempre com uma casa decimal.
Entrada
O arquivo de entrada contem 3 valores com uma casa decimal, de dupla precisao (double).
Saida
Imprima a mensagem "MEDIA" e a media do aluno conforme exemplo abaixo, com 1 digito apos o ponto decimal e com um espaco em branco antes e depois da igualdade. Assim como todos os problemas, nao esqueca de imprimir o fim de linha apos o resultado, caso contrario, voce recebera "Presentation Error".
Exemplos de Entrada Exemplos de Saida
5.0
6.0
7.0
MEDIA = 6.3
5.0
10.0
10.0
MEDIA = 9.0
10.0
10.0
5.0
MEDIA = 7.5"""
a = float(input())
b = float(input())
c = float(input())
media = (a*2 + b*3 + c*5) / 10
print("MEDIA = {:.1f}".format(media))