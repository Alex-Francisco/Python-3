## Exercício 27 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que calcule os N primeiros termos de uma PG com razão R e o primeiro termo P1 fornecidos pelo usuário. Também deve ser calculada e
apresentada a soma desses N termos."""

p1 = int(input("Digite um número inteiro que será o 1º termo: "))
r = int(input("Digite um número inteiro que será a razão: "))
qtde = int(input("Digite um número inteiro que será a quantidade de termos exibida: "))

cont = 0
soma = 0

print("")

while cont < qtde:
    
    print(p1, end=" ")
    soma += p1 
    p1 += r
    cont += 1

print("\nA soma de todos os termos é igual a {}".format(soma))
    

    
    
