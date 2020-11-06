## Exercício 62 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Faça uma pesquisa sobre o Algoritmo de Ordenação Quicksort. Implemente uma função recursiva que use algoritmo para
organizar a lista L de forma crescente. Escreva um programa para testar a função. """

import random
import time

def quicksort(v, p, r): # v = vetor, p = início, r = final
        if p < r:
                q = particionar(v, p , r)
                quicksort(v, p, q-1) # ordenar os elementos menores que o pivô
                quicksort(v, q+1, r) # ordenar os elementos maiores que o pivô

def particionar(v, p, r):
        x = v[p]
        i = p
        j = p + 1
        while j <= r:
                if v[j] < x:
                        i += 1
                        trocar(v, i, j)
                j += 1

        trocar(v, p, i)

        return i

def trocar(v, n, m):
        temp = v[n]
        v[n] = v[m]
        v[m] = temp

L = list(range(0, 10000))
random.shuffle(L)
antes = time.time()
quicksort(L, 0, len(L)-1)
depois = time.time()
total = (depois-antes)*1000

print(L)
print("\nO tempo total foi de %0.2f ms" % total)

