## Exercício 53 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba como parâmetro de entrada uma lista L de números inteiros e um valor. A função deve retornar
quantas vezes o valor está contido na lista. Caso ele não esteja em L, retorne 0. """

from random import randint

L = []


def ValorNaLista(N):
    cont = 0
    while len(L) < 20:
        x = randint(0, 20)
        L.append(x)
        NumRep = L.count(N)
    if N in L:
        print("\nO retorno é igual a 1. O valor digitado está na lista {} vez(es)".format(NumRep))
    else:
        print("\nO retorno é igual a 0. O valor digitado não está na lista!")
    
    print(L)
    print("\n")

ValorNaLista(N = int(input("N: ")))

