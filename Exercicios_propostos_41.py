## Exercício 41 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia um número N obrigatoriamente entre 0 e 50 e, em seguida, leia N números reais em uma lista
A. O programa deve separar os valores lidos em A em outras duas listas NEG e POS: a primeira contendo somente os valores
negativos e a segunda contendo os valores positivos e zero. Apresentar na tela as lista NEG e POS e a quantidade de valores
contidos em cada uma. """

N = -1
A = []

while N not in range(0, 51):
    try:
        N = int(input("Digite um valor inteiro enre 0 e 50: "))
    except:
        print("\n")
        print("=="*19)
        print("Você deve digitar um número inteiro!")
        print("=="*19)
        print("\n")

continua = 's'

while continua =='s':
    try:
        X = float(input("Digite um número real: "))
        A.append(X)
    except:
        print("\n")
        print("=="*19)
        print("Você deve digitar um número!")
        print("=="*19)
        print("\n")

    continua = input("Deseja digitar outro número? Digite s ou n: ")

NEG = []
POS = []

for i in A:
    if i < 0:
        NEG.append(i)
    else:
        POS.append(i)
        
print("\n")
print("Todos os valores válidos digitados foram adicionadas a lista 'A' que ficou assim;\n{}".format(A))
print("\nDuas listas, NEG e POS, foram criadas p/ separar valores negativos e positivos contidos em 'A'.")
print("\nA lista 'NEG' contém {} valor(es) e ficou assim;\n{}".format(len(NEG), NEG))
print("\nA lista 'POS' contém {} valor(es) e ficou assim;\n{}".format(len(POS), POS))
