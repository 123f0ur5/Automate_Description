#True
"""beecrowd | 1016
Distancia
Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1Dois carros (X e Y) partem em uma mesma direcao. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.
Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilometros do carro X, ou seja, consegue se afastar um quilometro a cada 2 minutos.
Leia a distancia (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distancia do outro carro.
Entrada
O arquivo de entrada contem um numero inteiro.
Saida
Imprima o tempo necessario seguido da mensagem "minutos".
Exemplo de Entrada Exemplo de Saida
30
60 minutos
110
220 minutos
7
14 minutos"""
a = int(input())
print("{} minutos".format(a*2))