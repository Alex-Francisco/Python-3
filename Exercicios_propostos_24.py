## Exercício 24 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia um número inteiro e, em seguida, apresente na tela a tabuado de 0 a 10 para esse número fornecido. Siga o
formato apresentado a seguir (supondo foi digitado 4):
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40"""

numX = int(input("Digite um número inteiro para ver a sua tabuada: "))
mult = 0

while mult < 11:
    print("{} x {} = {}".format(numX, mult, numX * mult))
    mult += 1
print("")
print("Fim da tabuada")
