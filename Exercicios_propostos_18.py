## Exercício 18 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia um número inteiro do teclado e diga se esse número é par ou ímpar. Para saber se um número
é par, deve-se verificar se o resto de sua divisão por 2 é igual a zero. Para calcular o resto da divisão de um número por
outro deve-se utilizar o operador %."""

try:
    num_x = int(input("Digite um número inteiro: "))

    if num_x % 2 == 0:
        print("O número digitado é par!")
    else:
        print("O número digitado é impar!")
except:
    print("Você não digitou um número inteiro!")
