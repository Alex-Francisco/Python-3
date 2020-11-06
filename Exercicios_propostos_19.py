## Exercício 19 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia dois números quaisquer e mostre na tela qual é o menor e qual é o maior."""

try:
    num_1 = float(input("Digite um número: "))
    num_2 = float(input("Digite outro número: "))

    if num_1 > num_2:
        print("O primeiro número digitado ({}) é maior que o segundo ({}).".format(num_1, num_2))
    else:
        print("O segundo número digitado ({}) é maior que o primeiro ({}).".format(num_2, num_1))
except:
    print("Os dados inseridos não são válidos!")
