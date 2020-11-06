## Exercício 47 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia do teclado duas matrizes de dimensões 2x2 e mostre na tela a multiplicação dessas duas matrizes. """

from random import randint
Lin = 2
Col = 2

M1 = []
M2 = []

i = 0
ident1 = 1
ident2 = 1
ident3 = 1

print("=="*29)
print("Digite 4 números inteiros para formar a 1ª matriz de 2x2.")
print("=="*29)
print("\n")

while i < Lin:
    M1.append([])
    j = 0
    while j < Col:
        M1[i].append(int(input("O nº inteiro digitado será o {}º nº da {}ª coluna da {}ª linha da 1ª matriz: ".format(ident1, ident2, ident3))))
        while ident2 <= 1:
            ident2 += 1
        j += 1
    if ident2 == 2:
        ident2 = 1
        ident3 += 1
        ident1 += 1
    i += 1

print("\nEsta é a lista gerada")
print('M1 =', M1)

print("\nExibindo como matriz fica assim")
i = 0
while i < Lin:
    j = 0
    print('|', end='')
    while j < Col:
        print("{0:4}".format(M1[i][j]), end='')
        j += 1
    print(' |')
    i += 1

i = 0
ident1 = 1
ident2 = 1
ident3 = 1

print("\n")
print("=="*29)
print("Digite 4 números inteiros para formar a 2ª matriz de 2x2.")
print("=="*29)
print("\n")

while i < Lin:
    M2.append([])
    j = 0
    while j < Col:
        M2[i].append(int(input("O nº inteiro digitado será o {}º nº da {}ª coluna da {}ª linha da 2ª matriz: ".format(ident1, ident2, ident3))))
        while ident2 <= 1:
            ident2 += 1
        j += 1
    if ident2 == 2:
        ident2 = 1
        ident3 += 1
        ident1 += 1
    i += 1

print("\nEsta é a lista gerada")
print('M2 =', M2)

print("\nExibindo como matriz fica assim")
i = 0
while i < Lin:
    j = 0
    print('|', end='')
    while j < Col:
        print("{0:4}".format(M2[i][j]), end='')
        j += 1
    print(' |')
    i += 1

print("\n")
print("=="*29)
print("A multiplicação das duas matrizes resulta em;")
print("=="*29)
print("\n")


i = 0
while i < Lin:
    j = 0
    print('|', end='')
    while j < Col:
        print("{0:4}".format(M1[i][j]*M2[i][j]), end=' ')
        j += 1
    print(' |')
    i += 1
