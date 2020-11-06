## Exercício 40 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia três dados de entrada: o primeiro termo, a razão e a quantidade de termos de uma P.A.,
todos números inteiros. O programa deve calcular todos os termos, colocando-os em uma lista, e exibi-la no final. """

testar_termo = 's'
testar_razao = 's'
testar_qtde = 's'

while testar_termo == 's':
    try:
        termo = int(input("Digite um número inteiro que será o 1º termo: "))
        testar_termo = 'n'
    except:
        print("\n")
        print("Você deve digitar um número inteiro!")
        print("\n")

while testar_razao == 's':
    try:
        razao = int(input("Digite um número inteiro que será a razão: "))
        testar_razao = 'n'
    except:
        print("\n")
        print("Você deve digitar um número inteiro!")
        print("\n")

while testar_qtde == 's':
    try:
        qtde_termo = int(input("Digite um número inteiro que será a quantidade de termo(s): "))
        while qtde_termo < 1:
            print("A quantidade de termos não pode ser menor que 1!")
            qtde_termo = int(input("Digite um número inteiro que será a quantidade de termo(s): "))
        testar_qtde = 'n'
    except:
        print("\n")
        print("Você deve digitar um número inteiro!")
        print("\n")

Lista = []
Lista.append(termo)

qtde_termo -= 1

print("Termos para serem exibidos ->", end=" ")
for i in range (0, qtde_termo):
    termo += razao
    Lista.append(termo)

print(Lista)
    
