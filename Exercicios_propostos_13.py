## Exercício 13 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Altere o programa da PA para exibir em cada linha uma frase como a seguir (exemplo: supondo que
primeiro_termo = 5, razao = 3 e quant_elementos = 3).
Termo 1 da PA = 5
Termo 2 da PA = 8
Termo 3 da PA = 11"""

primeiro_termo = int(input("Digite um número inteiro para ser o primeiro termo: "))
razao = int(input("Digite um número inteiro para ser a razão: "))
quant_elementos = int(input("Digite um número inteiro para ser a quantidade de elemntos exibida: "))

soma, cont = 0, 0

print("")

while cont < quant_elementos:
    print("Termo {} da PA = {}".format(cont+1, primeiro_termo))
    soma += primeiro_termo
    primeiro_termo += razao
    cont += 1

print("")
print("A soma de todos os termos é igual a {}".format(soma))
    

