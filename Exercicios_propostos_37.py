## Exercício 37 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes tamanhos nA e nB,
respectivamente. Em seguida, o programa deve juntar as duas em uma única lista com o tamanho nA + nB. Exibir na tela a
lista resultante. Veja o exemplo:

nA = 5
A = [16, 8, 25, 12, 19]

nB = 7
B = [5, 14, 3, 27, 8, 21, 44]

nR = 12
R = [16, 8, 25, 12, 19, 5, 14, 3, 27, 8, 21, 44]"""

print("=="*22)
print("|| O programa gera lista(s) aleatória(s) ||")
print("=="*22)
print("\n")

from random import randint

A, B = [], []
nA, nB = randint(0,10), randint(0,10)

for i in range(0, nA):
    x1 = randint(0, 50)
    A.append(x1)

for j in range(0, nB):
    x2 = randint(51, 100)
    B.append(x2)

C = A + B

print("A lista 'A' tem o tamanho {} e ficou assim -> {}".format(nA, A))
print("A lista 'B' tem o tamanho {} e ficou assim -> {}".format(nB, B))
print("\n")
print("=="*38)
print("A junção das duas listas resulta na lista abaixo;\n{}".format(C))
print("=="*38)
