## Exercício 12 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Altere o programa da PA para também calcular e mostrar o somatório de todos os termos. Para isso, crie um novo
objeto com o identificador soma, atribuindo a ele o valor inicial 0, e a cada repetição doo laço acrescente a
ele um termo do PA."""

primeiro_termo = int(input("Digite um número inteiro para o primeiro termo: "))
razao = int(input("Digite um número inteiro para a razão: "))
quant_elementos = int(input("Digite um número inteiro para a quantidade de elementos: "))

soma, cont = 0, 0

while cont < quant_elementos:
    print(primeiro_termo)
    soma += primeiro_termo
    primeiro_termo += razao
    cont += 1
print("")
print("A soma de todos os termos é igual a {}".format(soma))
    
