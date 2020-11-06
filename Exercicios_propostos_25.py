## Exercício 25 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia um número inteiro N e, em seguida, leia N números reais, calculando a soma de todos os valores positivos fornecidos e
ignorando os negativos."""

soma = 0
num_real_x = 0
continuar = "s"

num_int_X = int(input("Digite um número inteiro: "))

while continuar == "s":
    num_real_X = float(input("Digite um número real agora: "))

    if num_real_X >= 0:
        soma += num_real_X

    if num_int_X >= 0:
        total = soma + num_int_X
    else:
        total = soma

    print("\nA soma dos valores até agora, excluindo os números negativos é igual a {}\n".format(total))   
    continuar = input("Deseja continuar somando? Digite s ou n: ")
    
    
