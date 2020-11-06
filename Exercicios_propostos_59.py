## Exercício 59 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba como parâmetro de entrada uma lista L e retorne uma lista organizada em ordem crescente.
Para fazer a ordenação, use o algoritmo de ordenação bolha (bubble sort). Crie uma segunda versão dessa função que retorne
uma lista organizada em ordem decrescente.

Escreva um programa para testar essas duas funções. Esse programa deve ler um número inteiro N e gerar uma lista com N
números inteiros aleatórios utilizando a função randint(). Use as duas funções de ordenação e exiba na tela as listas
ordenadas crescente e decrescente."""

from random import randint

print("Ordenação Bolha\n")
L = [17, 4, 23, 8, 19, 12]
print("Lista pré-definida:", L)

def OrdemCrescente(Lista):
    Trocou = 1
    while Trocou:
        Trocou = 0
        i = 0
        while i < len(L) - 1:
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                Trocou = 1
            i += 1
        print(" estado parcial de L:", L)
    print("\nSituação final - ordem crescente")
    return L

def OrdemDecrescente(Lista):
    L.sort(reverse=True)
    print("\nSituação final - ordem decrescente")
    return L

print(OrdemCrescente(L))
print(OrdemDecrescente(L))

n = 0
novamente = 's'
print("\n")

while novamente == 's':
    if n < 5 or n > 10:
        n = int(input("Digite um nº inteiro > ou = a 5 e < ou = a 10: "))
    else:
        novamente = 'n'

print("\nUma lista foi gerada automaticamente, ela contém {} números!".format(n))

L = []
while len(L) < n:
    x = randint(0, 5000)
    L.append(x)

print(OrdemCrescente(L))
print(OrdemDecrescente(L))


