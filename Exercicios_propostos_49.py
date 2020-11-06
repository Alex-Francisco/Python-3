## Exercício 48 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que recebe um número inteiro como parâmetro de entrada e retorna o texto 'PAR' ou 'ÍMPAR' """

def Par_Impar(X):
    if X % 2 == 0:
        print("O número digitado foi {}\nO retorno é PAR!".format(X))
    else:
        print("O número digitado foi {}\nO retorno é ÍMPAR!".format(X))

try:
    Par_Impar(X = int(input("Digite um número inteiro: ")))
except:
    print("Você não digitou um número inteiro!")
    
