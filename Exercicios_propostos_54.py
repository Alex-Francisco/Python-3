## Exercício 54 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva um programa que receba como parâmetro de entrada um número inteiro de 5 dígitos no intervalo fechado [10000, 30000]
que represente códigos de produtos vendidos em uma loja. A função deve calcular e retornar o dígito verificador utilizando
regra de cálculo explicada a seguir.
Considere o código 21853, em que cada dígito é multiplicado por um peso começando em 2, os valores obtidos são somados, e do
total obtido calcula-se o resto de sua divisão por 7.

Dígito           2   1   8   5   3
Peso             2   3   4   5   6
Multiplicação    4   3   32  25  18   

Soma todos = 82
Resto de 82 por 7 = 5"""


def CodVenda(x):
    while x < 10000 or x > 30000:
        print("Erro. O código do produto deve ter 5 dígitos e estar entre 10000 e 30000!!!")
        CodVenda(x = int(input("Digite um número inteiro com 5 dígitos entre 10000 e 30000: ")))
    else:
        if x >= 10000 or x <= 30000:
            Sep = str(x)

    p1 = (int(Sep[0])) * 2
    p2 = (int(Sep[1])) * 3
    p3 = (int(Sep[2])) * 4
    p4 = (int(Sep[3])) * 5
    p5 = (int(Sep[4])) * 6

    digVerif = (p1 + p2 + p3 + p4 + p5) % 7

    print("\n")
    print("*-*"*19)
    print("O dígito verificador p/ o cód. do produto digitado é {}".format(digVerif))
    print("*-*"*19)

CodVenda(x = int(input("Digite um número inteiro com 5 dígitos entre 10000 e 30000: ")))
