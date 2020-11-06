## Exercício 09 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia do teclado as cordenadas (x1, y1) do ponto 1 e (x2, y2) do ponto 2. Utilizando a expressão
do exercício 8 (exp5 - atribuída a d), determine a distância entre esses dois pontos e exiba-a na tela com três casas
decimais. Teste-o com os dados a seguir;
Para x_1 = 0.0, y_1 = 0.0, x_2 = 3.0 e y_2 = 4.0 o valor de d será 5.000
Para x_1 = 2.0, y_1 = 1.0, x_2 = 0.0 e y_2 = 5.0 o valor de d será 4.472
Para x_1 = -3.0, y_1 = 1.5, x_2 = 7.1 e y_2 = 5.5 o valor de d será 10.863
Para x_1 = 0.0, y_1 = 3.5, x_2 = 0.0 e y_2 = 7.0 o valor de d será 3.500
Para x_1 = 8.2, y_1 = 2.5, x_2 = -5.0 e y_2 = -5.0 o valor de d será 15.182
Para x_1 = 6.9, y_1 = 2.0, x_2 = 16.0 e y_2 = -1.8 o valor de d será 9.862"""

from math import sqrt

x_1 = float(input('Digite a cordenada de x1: '))
y_1 = float(input('Digite a cordenada de y1: '))
x_2 = float(input('Digite a cordenada de x2: '))
y_2 = float(input('Digite a cordenada de y2: '))

d = sqrt((x_1-x_2)**2+(y_1-y_2)**2)

print("Com base nos valores inseridos D é = {:.3f}".format(d))

