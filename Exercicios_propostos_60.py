## Exercício 60 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva um programa que leia um número inteiro Q e exiba na tela os Q primeiros termos da sequência de Fibonacci,
utilizando uma função recursiva para determinar o elemento da sequência a ser exibido."""

print("Os dez primeiros termos da sequência de Fibonacci são: 0, 1, 1, 2, 3, 5, 8, 13, 21 e 34.")

Q = 0

while Q < 2:
        try:
            Q = int(input("\nDigite Q(>1): "))
            if Q < 2:
                print("\nDigite Q >= 2")
        except:
            print("O dado digitado deve ser um número inteiro.")

def Fibonacci(QuantTermos):
    L = [0, 1]
    for i in range(Q-2):
        L.append(L[i] + L[i+1])          
    return L

print(Fibonacci(Q))


