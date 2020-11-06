## Exercício 26 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia valores numéricos inteiros e totalize separadamente os positivos e os negativos até que o usuário digite 0. Ao final, mostre
na tela esses dois totais."""

num_digitado = 1
total_pos = 0
total_neg = 0
cont = 0

while num_digitado != 0:
    num_digitado = int(input("Digite um número inteiro positivo ou negativo para somar ou 0 para sair do programa: "))
    cont += 1
        
    if num_digitado > 0:
        total_pos += num_digitado
        
    else:
        total_neg += num_digitado
        
    if cont < 2:
        msg = "\nNúmero 0 inserido como 1º valor! Não há nada para ser calculado...\nPrograma encerrado."
    else:
        msg = "\nA soma dos números inteiros positivos digitados é igual a {}\nA soma dos números inteiros negativos digitados é igual a {}".format(total_pos, total_neg)

print(msg)


    
    
