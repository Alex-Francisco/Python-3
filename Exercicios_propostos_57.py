## Exercício 57 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba uma lista L e elimine os eventuais elementos repetidos contidos na mesma, deixando na lista
resultante apenas uma ocorrência de cada elemento. Escreva um programa para testar essa função, o qual deve ler do teclado os
elementos que farão parte da lista."""


L = []
Cont = 1

print("=*"*20)
print("Você deve digitar 10 números inteiros. Caso algum número seja repetido, o programa eliminará esse número da lista!")
print("=*"*20)


def EliminaRepetidos(Lista):
    for e in range(0, len(L)):
        if NumDigitado in L:
            while L.count(NumDigitado) > 1:
                L.reverse()
                L.remove(NumDigitado)
                L.reverse()
    return L

while Cont < 11:
    try:
        NumDigitado = int(input('Digite o {}º número inteiro: '.format(Cont)))
        L.append(NumDigitado)
        EliminaRepetidos(L)
        Cont += 1
        
    except:
        print("\nErro! Você não digitou um número inteiro.")

print("\nCaso algum nº tenha sido digitado mais de uma vez, sua próxima ocorrência foi removida. A lista ficou assim: ")
print(EliminaRepetidos(L))



