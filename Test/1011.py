#True
"""beecrowd | 1011
Esfera
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Faca um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A formula para calcular o volume e: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
Dica: Ao utilizar a formula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisao entre dois inteiros e outro inteiro.
Entrada
O arquivo de entrada contem um valor de ponto flutuante (dupla precisao), correspondente ao raio da esfera.
Saida
A saida devera ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaco antes e um espaco depois da igualdade. O valor devera ser apresentado com 3 casas apos o ponto.
Exemplos de Entrada Exemplos de Saida
3
VOLUME = 113.097
15
VOLUME = 14137.155
1523
VOLUME = 14797486501.627"""
raio = float(input())
volume = (4/3) * 3.14159 * pow(raio,3)
print("VOLUME = {:.3f}".format(volume))