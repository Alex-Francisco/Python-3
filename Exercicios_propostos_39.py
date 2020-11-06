## Exercício 39 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominadas A
e B com tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam aceitos
valores repetidos. Em seguida, o programa deve juntar as duas em uma única lista R [resultante], tomando o cuidado
de que R não tenha valores duplicados. Veja o exemplo:

nA = 5
A = [16, 8, 25, 12, 19]

nB = 7
B = [5, 14, 3, 27, 8, 21, 44]

nR = 11
R = [16, 8, 25, 12, 19, 5, 14, 3, 27, 21, 44] """

A = []
B = []

nA_valido = 'n'
nB_valido = 'n'

while nA_valido == 'n':
    try:
        nA = int(input("Digite qual será o tamanho da lista 'A': "))
        nA_valido = 's'
    except:
        print("\n")
        print("=="*20)
        print("Você não digitou um número inteiro!")
        print("=="*20)
        print("\n")
        
while nB_valido == 'n':
    try:
        nB = int(input("Digite qual será o tamanho da lista 'B': "))
        nB_valido = 's'
    except:
        print("\n")
        print("=="*20)
        print("Você não digitou um número inteiro!")
        print("=="*20)
        print("\n")

for i in range(0, nA):
    x1 = int(input("\nDigite um número inteiro para a lista 'A': "))
    if x1 not in A and x1 not in B:
        A.append(x1)
    else:
        print('\n')
        print("***"*20)
        print("O valor digitado está em uma das lista, por isso foi ignorado!")
        print("***"*20)
        print('\n')

for j in range(0, nB):
    x2 = int(input("\nDigite um número inteiro para a lista 'B': "))
    if x2 not in A and x2 not in B:
        B.append(x2)
    else:
        print('\n')
        print("***"*20)
        print("O valor digitado está em uma das lista, por isso foi ignorado!")
        print("***"*20)
        print('\n')

R = A + B

print("\nA lista 'A' ficou assim ->: {}".format(A))
print("A lista 'B' ficou assim ->: {}".format(B))
print("\nA junção das listas resulta na lista abaixo;\n{}".format(R))             

    
