## Exercício 61 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Dada uma lista contendo números inteiros, escreva uma função recursiva para calcular a multiplicação de todos os
elementos. Exiba o resultado na tela."""

print("Foi pré-definida uma lista abaixo;")
L = [10, 5, 8, 2, 1, 4, 7, 3, 5, 9]
print(L)
print("\n")


def Multiplica(Lista):
        R = 0
        i = 0
        Mult = 1
        for e in L:
                R = L[i]
                i += 1
                Mult *= R
        print("Multiplicando todos os valores da lista, obtemos o seguinte resultado:",end=" ")
        return Mult
                
print(Multiplica(L))


