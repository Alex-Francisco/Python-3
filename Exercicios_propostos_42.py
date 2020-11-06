## Exercício 42 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia um número N obrigatoriamente entre 0 e 50 e, em seguida, defina uma lista V preenchendo-a com
N números inteiros aleatórios (utilizar a função randint). Exiba-a na tela. Inicie um laço no qual será feita a leitura de um
número X e que termina quando X for zero. Pesquise se X está ou não na lista V e, caso esteja, elimine todas as sua ocorrências."""

from random import randint

N = -1

while N < 0 or N > 50:
    try:
        N = int(input("Você deve digitar um número entre 0 e 50: "))
    except:
        print("\n")
        print("=="*19)
        print("Digite um número inteiro!")
        print("=="*19)
        print("\n")

V = []

for i in range(0, 20):
    V.append(randint(1, 100))

print("\nUma lista 'V' foi gerada automaticamente, ela contém os valores abaixo;\n{}".format(V))

X = 1
while X != 0:
    try:
        print("\n")
        print("=="*25)
        print("O programa termina quando 0 for digitado!")
        print("=="*25)
        X = int(input("\nDigite um nº inteiro que será usado p/ verificar se ele está na lista 'V' ou não, se estiver será deletado: "))
    except:
        print("Digite um número inteiro!")
    if X not in V and X > 0:
        print("\n")
        print("=="*16)
        print("O nº lido não está na lista 'V'!")
        print("=="*16)
        print("\n")
    elif X == 0:
        print("Número 0 inserido. Programa encerrado!")
        break
    else:
        if X in V and X >0:
            contagem = V.count(X)
        while X in V and X > 0:
            V.remove(X)
        print("O valor {} estava na lista {} vez(es) e foi removido!".format(X, contagem))
        print("\n")
        print("A lista 'V' foi atualizada e ficou assim;\n{}".format(V))
    
