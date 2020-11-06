## Exercício 44 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia do teclado uma lista com N elementos. Em seguida, o programa deve eliminar os elementos que estiverem
repetidos, mantendo apenas a primeira ocorrência de cada. Apresentar a lista resultante na tela. Os valores eliminados devem ser
armazenadas em outra lista que também deve ser exibida. """

from random import randint

qtdeElementos = randint(2, 20)
N = []
E = []

print("=="*34)
print("Valores iguais serão eliminados, mantendo apenas sua 1ª ocorrência!")
print("=="*34)
print("\n")

for i in range(0 , qtdeElementos):
    try:
        X = int(input("Digite um número inteiro: "))
        N.append(X)

        if X in N:
            while N.count(X) > 1:
                N.reverse()
                E.append(X)
                N.remove(X)
                N.reverse()
    except:
        print("\n")
        print("=="*16)
        print("Você deve digitar um número inteiro!")
        print("=="*16)
        print("\n")

print("\nA lista atualizada ficou assim;\n{}".format(N))

if len(E) > 0:
    print("\nEsses são os valores que foram eliminados -> {}".format(E))
else:
    print("\nNão havia nenhum valor repetido para ser eliminado!")







