## Exercício 52 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba um número inteiro N e retorne uma lista com os bits 0 e 1, que representam N convertido para
binário. Não use nenhuma função Python de conversão para binários. Em vez disso, elabore uma lógica baseada no processo de
divisões sucessivas. """

from math import trunc

binario = []

def convBin(x):
    if x == 0:
        binario.append(x)
    while x >= 1:
        bit = x % 2
        binario.append(trunc(bit))
        x /= 2
    binario.reverse()

convBin(x = int(input("Digite um número inteiro e veja como ele é em binário: ")))
print("\nO número digitado fica assim quando convertido p/ binário: ")
print(binario)
