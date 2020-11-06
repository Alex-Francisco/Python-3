## Exercício 35 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-a na tela na ordem inversa à ordem
de leitura."""

L = []

for i in range (0, 10):
    x = int(input("Digite um número inteiro: "))
    L.append(x)
L.reverse()

print("\n")
print("A lista em ordem inversa fica assim -> {}".format(L))

