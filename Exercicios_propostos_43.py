## Exercício 43 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente, deve ser maior
que Min. Em seguida, preencher uma lista com todos os valores divisíveis por 7 contidos no intervalo fechado (Min, Max). Exibir
a lista resultante na tela. """

aceitaMin = 'n'

while aceitaMin == 'n':
    try:
        Min = int(input("Digite um número inteiro que será o valor atribuído a 'Min': "))
        aceitaMin = 's'
    except:
        print("\n")
        print("=="*18)
        print("Você não digitou um número inteiro!")
        print("=="*18)
        print("\n")

aceitaMax = 'n'

while aceitaMax == 'n':
    try:
        Max = int(input("Digite um número inteiro que será o valor atribuído a 'Max': "))
        if Max <= Min:
            print("\n")
            print("=="*29)
            print("Você deve atribuir a 'Max' um valor maior que o atribuído a 'Min'!")
            print("=="*29)
            print("\n")
        else:
            aceitaMax = 's'
    except:
        print("\n")
        print("=="*18)
        print("Você não digitou um número inteiro!")
        print("=="*18)
        print("\n")

R = []

for i in range(Min, Max):
    if i % 7 == 0:
        R.append(i)

if len(R) > 0:
    print("\nA lista abaixo apresenta os valores entre 'Min' e 'Max' divisíveis por 7.\n{}".format(R))
else:
    print("Entre 'Min' e 'Max' não existem valores  divisíves por 7!")
        
