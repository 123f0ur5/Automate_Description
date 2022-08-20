#True
"""beecrowd | 1008
Salario
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Escreva um programa que leia o numero de um funcionario, seu numero de horas trabalhadas, o valor que recebe por hora e calcula o salario desse funcionario. A seguir, mostre o numero e o salario do funcionario, com duas casas decimais.
Entrada
O arquivo de entrada contem 2 numeros inteiros e 1 numero com duas casas decimais, representando o numero, quantidade de horas trabalhadas e o valor que o funcionario recebe por hora trabalhada, respectivamente.
Saida
Imprima o numero e o salario do funcionario, conforme exemplo fornecido, com um espaco em branco antes e depois da igualdade. No caso do salario, tambem deve haver um espaco em branco apos o $.
Exemplos de Entrada Exemplos de Saida
25
100
5.50
NUMBER = 25
SALARY = U$ 550.00
1
200
20.50
NUMBER = 1
SALARY = U$ 4100.00
6
145
15.55
NUMBER = 6
SALARY = U$ 2254.75"""
a = int(input())
b = int(input())
c = float(input())
print("NUMBER = {}".format(a))
print("SALARY = U$ {:.2f}".format(b*c))