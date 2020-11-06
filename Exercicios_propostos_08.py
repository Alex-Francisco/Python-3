## Exercício 08 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva em Python as seguintes expressões aritméticas para as fórmulas a seguir e teste as quatro primeiras
para os valores A = 4, B = 5, C = 1 e a última para os valores x_1 = 1, y_1 = 1, x_2 = 4 e y_2 = 5."""

from math import sqrt

A = 4
B = 5
C = 1

x_1 = 1
y_1 = 1
x_2 = 4
y_2 = 5

exp1 = (A + B) / 2
exp2 = (-B + sqrt(B * B - 4 * A * C)) / (2 * A)
exp3 = (3 * A + 2 * B) / (A + B)
exp4 = 7 * 6 * A - B ** 1.7
exp5 = sqrt((x_1-x_2)**2+(y_1-y_2)**2)

print("R = A + B sobre 2 -> Logo o resultado da expressão é: R = {}".format(exp1))
print("X = -B + Raiz Quadrada de B ao quadrado - 4AC sobre 2A -> Logo o resultado da expressão é: X = {}".format(exp2))
print("R = 3 x A + 2 x B sobre A + B -> Logo o resultado da expressão é: R = {0:2f}".format(exp3))
print("Z = 7 x 6 x A - B elevado a 1,7 -> Logo o resultado da expressão é: Z = {0:2f}".format(exp4))
print("D = Raiz quadrada de x1 - x2 elevado ao quadrado + y1 - y2 ao quadrado -> Logo o resultado da expressão é: {}".format(exp5))
