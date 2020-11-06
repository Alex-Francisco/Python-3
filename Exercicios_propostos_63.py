## Exercício 63 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva um programa que contenha duas funções de ordenação diferentes: uma que implemente o algoritmo Bubble Sort
e outra que implemente o algoritmo Quicksort (criada no Exercício 62). Escreva um programa que gere uma lista com um
tamanho bem grande e utilize-a para testar o desempenho das duas funções.
Sugestões:
Faça esse programa gerar a lista grande contendo Q elementos, na qual Q é digitado pelo usuário. Esse valor Q deve ser
bem grande, por exemplo, de 10 a 50 mil elementos, ou mais, dependendo da capacidade de seu computador."""

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

L = list(range(0, 100000))
random.shuffle(L)
antes = time.time()
quicksort(L, 0, len(L)-1)
depois = time.time()
total = (depois-antes)*1000

print(L)
print("\nO tempo total de execução do quicksort foi de %0.2f ms" % total)

random.shuffle(L)
def bubble(Lista):
        Trocou = 1
        while Trocou:
                Trocou = 0
                i = 0
                while i < len(L) - 1:
                        if L[i] > L[i+1]:
                                L[i], L[i+1] = L[i+1], L[i]
                                Trocou = 1
                        i += 1
                
        print("\nSituação final - ordem crescente")
        return L

print(bubble(L))
print("\nO tempo total de execução do bubble foi de %0.2f ms" % total)
