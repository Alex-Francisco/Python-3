## Exercício 33 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Elabore um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N, em que N é um número
digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse requisito). """

soma = 0
N = 0

while N < 100:
    N = int(input("Digite um número inteiro: "))

    if N < 100:
            print("=="*27)
            print("Atenção! O número digitado não pode ser menor que 100.")
            print("=="*27)
    else:
        Aux = N

        print("\n")
        print("*="*35)
        print("Os números pares entre 1 e {} são;".format(N))
        print("*="*35)
        print("\n")
        
        while Aux >= 1:
                if Aux % 2 == 0:
                        print(Aux, end=" ")
                        soma += Aux
                Aux -= 1
                
        print("\n")
        print("*="*35)
        print("A soma de todos os números pares listados acima é igual a {}.".format(soma))
        print("*="*35)
