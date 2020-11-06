## Exercício 31 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Elabore um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor negativo
seja informado. Ao final, devem ser apresentados o maior e menor valores informados pelo usuário, a quantidade
de valores, a soma e a média de todos. """

cont = 0
continua = 's'
menor = 1
maior = 1
positivos = 0
soma = 0

print("==="*24)
print("O programa só será encerrado quando zero ou um nº negativo for digitado!")
print("==="*24)
print("\n")

while continua == 's':

    num_int = int(input("Digite um número inteiro: "))
    
    if num_int <= 0:
        continua = 'n'
    else:
        soma += num_int
        
        if num_int >= maior:
            maior = num_int

        if num_int >= 1 and cont == 0:
            menor = num_int
            cont = 1

        elif cont == 1 and num_int < menor:
            menor = num_int

        positivos +=1

print("\nForam digitados {} números positivos".format(positivos))
print("O menor número digitado foi {}".format(menor))
print("O maior número digitado foi {}".format(maior))
print("A soma dos valores válidos digitados é igual a {}".format(soma))
print("A média dos valores digitados é igual a {:.2f}".format(soma/positivos))

