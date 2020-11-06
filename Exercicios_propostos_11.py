## Exercício 11 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Altere o programa da PA para, em vez de dez elementos, apresentar na tela uma quantidade de elementos
lido do teclado (número inteiro)."""

primeiro_termo = int(input("Digite um número inteiro que será o primeiro termo: "))
razao = int(input("Digite um número inteiro que será a razão: "))
quant_elementos = int(input("Digite um número inteiro que será a quantidade de elementos mostrado: "))

cont = 0

while cont < quant_elementos:
    print(primeiro_termo)
    primeiro_termo += razao
    cont += 1
