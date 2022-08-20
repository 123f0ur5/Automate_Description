#True
"""beecrowd | 1012
Area
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Escreva um programa que leia tres valores com ponto flutuante de dupla precisao: A, B e C. Em seguida, calcule e mostre:
a) a area do triangulo retangulo que tem A por base e C por altura.
b) a area do circulo de raio C. (pi = 3.14159)
c) a area do trapezio que tem A e B por bases e C por altura.
d) a area do quadrado que tem lado B.
e) a area do retangulo que tem lados A e B.
Entrada
O arquivo de entrada contem tres valores com um digito apos o ponto decimal.
Saida
O arquivo de saida devera conter 5 linhas de dados. Cada linha corresponde a uma das areas descritas acima, sempre com mensagem correspondente e um espaco entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 digitos apos o ponto decimal.
Exemplos de Entrada Exemplos de Saida
3.0 4.0 5.2
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
12.7 10.4 15.2
TRIANGULO: 96.520
CIRCULO: 725.833
TRAPEZIO: 175.560
QUADRADO: 108.160
RETANGULO: 132.080"""
a, b, c = input().split()
print("TRIANGULO: {:.3f}".format(float(a)*float(c)/2))
print("CIRCULO: {:.3f}".format(3.14159*pow(float(c),2)))
print("TRAPEZIO: {:.3f}".format(((float(a)+float(b))*float(c))/2))
print("QUADRADO: {:.3f}".format(float(b)*float(b)))
print("RETANGULO: {:.3f}".format(float(a)*float(b)))