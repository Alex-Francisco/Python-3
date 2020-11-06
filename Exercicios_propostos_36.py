## Exercício 36 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia do teclado duas lista com tamanho 10, com números inteiros. Em seguida, o programa
deve juntar as duas listas em uma única com o tamanho 20."""

L1 = []
L2 = []

for i in range(0, 10):
    x1 = int(input("Digite um número inteiro para a lista 1: "))
    x2 = int(input("Digite um número inteiro para a lista 2: "))
    L1.append(x1)
    L2.append(x2)

L3 = L1 + L2

print("\n")
print("A 1ª lista contém os valores -> {}".format(L1))
print("=="*33)
print("A 2ª lista contém os valores -> {}".format(L2))
print("=="*33)
print("A junção das duas lista resulta na seguinte lista abaixo;\n{}".format(L3))
