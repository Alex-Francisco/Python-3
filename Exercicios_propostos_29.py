## Exercício 29 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
"""Escreva um programa que leia um número inteiro N e, em seguida, leia N números reais, separando o menor e o maior, apresentando-os na tela."""

num_int = int(input("Digite um número inteiro: "))
continuar = "s"
menor = 0
maior = 0

while continuar == "s":
    num_real = float(input("Digite um número real: "))
    continuar = input("Quer digitar outro número real? Digite s ou n: ")

    while num_real < menor:
        menor = num_real
        if num_int < menor:
            menor = num_int

    while num_real > maior:
        maior = num_real
        if num_int > maior:
            maior = num_int

print("")
print("O maior número digitado foi {} e o menor número digitado foi {}.".format(maior, menor))
    

    
    
