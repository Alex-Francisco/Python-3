## Exercício 45 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Faça um programa que leia um número inteiro N bem grande (acima de 5000). Preencha uma lista de tamanho N com números inteiros
aleatórios positivos. Em seguida, inicie um laço de pesquisa, no qual o valor a ser pesquisado deve ser lido do teclado, e o programa
deve dizer se tal valor está ou não contido na lista, bem como dizer sua posição. No caso de várias ocorrências, exibir todas. O laço
de pesquisa termina quando for digitado 0. Use o algoritmo de busca sequencial. """

from random import randint

continua = 's'
N = 0

while continua == 's':
    try:
        if N < 5000:
            N = int(input("Digite um número inteiro maior que 5000: "))
        else:
            continua = 'n'
    except:
        print("\n")
        print("=="*28)
        print("Você não digitou um número inteiro!")
        print("=="*28)
        print("\n")

Lista = []
for i in range(randint(5, 20)):
    Lista.append(randint(1, 10))

print("\n")
print(Lista)
print("\n")

print("Quando 0 for digitado o prgrama será encerrado.\n")

posicoes = []
try: 
    valPesquisado = int(input("Digite um nº inteiro que será usado para saber se ele está na lista ou não: "))
except:
    print("\n")
    print("=="*28)
    print("Você não digitou um número inteiro!")
    print("=="*28)
    print("\n")

while valPesquisado != 0:
    if valPesquisado in Lista:
       print("\n")
       print("=="*40)
       print("\nO número {} está na lista e se encontra nas posições -> ".format(valPesquisado), end="")
       for n, i in enumerate(Lista):
           if i == valPesquisado:
               print(n, end = ", ")
       print("\n") 
       print("=="*40)
    else:
        print("{} não está na lista".format(valPesquisado))
    valPesquisado = int(input("\nDigite um nº inteiro que será usado para saber se ele está na lista ou não: "))
    if valPesquisado == 0:
        print("Valor 0 inserido. Programa encerrado!")

