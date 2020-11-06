## Exercício 32 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que contenha um laço que será executado enquanto o número digitado for diferente de zero. Para cada número
digitado pelo usuário, mostrar na tela apenas os que forem divisíveis por 2 e por 3."""


continua = 's'
cont = 0

print("=="*36)
print("Quando o número digitado por divisível por 2 e por 3, uma mensagem será exibida")
print("=="*36)


while continua == 's':
    numX = float(input("Digite um número: "))

    if numX == 0:
        continua = 'n'
        if cont == 0:
            print("\nNão há nada para se fazer, o zero foi o primeiro número inserido!")
    else:
        cont += 1

        if numX % 2 == 0 and numX % 3 ==0:
            print("=="*25)
            print("O número {} é divisível por 2 e por 3!".format(numX))
            print("=="*25)

    if numX == 0 and cont > 0:
        print("Zero digitado. Programa encerrado!")
