#True
"""beecrowd | 1015
Distancia Entre Dois Pontos
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distancia entre eles, mostrando 4 casas decimais apos a virgula, segundo a formula:
Distancia =
Entrada
O arquivo de entrada contem duas linhas de dados. A primeira linha contem dois valores de ponto flutuante: x1 y1 e a segunda linha contem dois valores de ponto flutuante x2 y2.
Saida
Calcule e imprima o valor da distancia segundo a formula fornecida, com 4 casas apos o ponto decimal.
Exemplo de Entrada Exemplo de Saida
1.0 7.0
5.0 9.0
4.4721
-2.5 0.4
12.1 7.3
16.1484
2.5 -0.4
-12.2 7.0
16.4575"""
import math
a, b = map(float, input().split())
c, d = map(float, input().split())
print("{:.4f}".format(math.sqrt(pow((a-c),2)+pow((d-b),2))))