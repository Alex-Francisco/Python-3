## Exercício 58 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba duas lista L1 e L2 como parâmetros de entrada
 e retorne uma lista contento todos os elementos de L1 que não estão em L2.
 Escreva um programa para testar essa função."""

L1 = []
L2 = []
L3 = []

print("*="*50)
print("""O programa receberá 10 nº inteiros (5 p/ cada lista), caso os elementos da Lista 1 não estejam na Lista 2, esses nº serão
retornados!""")
print("*="*50)
print("\n")

def RecebeLista(Lista1, Lista2):
    for e in L1:
        if e not in L2:
            L3.append(e)
    return L3

while len(L1) < 5:
    NumDigitado = int(input("Digite um número inteiro que será adicionado a Lista 1: "))
    L1.append(NumDigitado)

print("\n")

while len(L2) < 5:
    NumDigitado = int(input("Digite um número inteiro que será adicionado a Lista 2: "))
    L2.append(NumDigitado)

print("\nUma 3ª terceira lista foi criada, os nº de L1 não presentes em L2, serão adiciondas a L3 e exibidos abaixo;")
print(RecebeLista(L1, L2))


