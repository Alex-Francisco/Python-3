## Exercício 17 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia um número inteiro do teclado e diga se esse número é positivo ou negativo."""

try: 
    num_x = int(input("Digite um número inteiro: "))
    if num_x < 0:
        print("O número digitado é negativo")
    else:
        print("o número digitado é positivo")
except:
    print("Você não digitou um número inteiro.")
