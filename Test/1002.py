#True
"""beecrowd | 1002
Area do Circulo
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1A formula para calcular a area de uma circunferencia e: area = p . raio2. Considerando para este problema que p = 3.14159:
- Efetue o calculo da area, elevando o valor de raio ao quadrado e multiplicando por p.
Entrada
A entrada contem um valor de ponto flutuante (dupla precisao), no caso, a variavel raio.
Saida
Apresentar a mensagem "A=" seguido pelo valor da variavel area, conforme exemplo abaixo, com 4 casas apos o ponto decimal. Utilize variaveis de dupla precisao (double). Como todos os problemas, nao esqueca de imprimir o fim de linha apos o resultado, caso contrario, voce recebera "Presentation Error".
Exemplos de Entrada Exemplos de Saida
2.00
A=12.5664
100.64
A=31819.3103
150.00
A=70685.7750"""
x = float(input())
n = 3.14159
area = n * pow(x,2)
print("A={:.4f}".format(area))