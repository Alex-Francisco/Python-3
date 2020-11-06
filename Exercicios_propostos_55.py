## Exercício 55 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba como parâmetro de entrada dois números reais Min e Max. Essa função deve ler do teclado
um número real e retorná-lo caso esteja dentro do intervalo fechado [Min, Max]. Caso contrário, a função deve exibir uma
mensagem de erro e ler um novo valor. """

def MinMax(Num1, Num2):
    if Num1 > Num2:
        Maximo = Num1
        Minimo = Num2
    else:
        Maximo = Num2
        Minimo = Num1

    print("\n")
    print("==*"*18)
    print("O menor valor digitado foi {} e o maior foi {}".format(Minimo, Maximo))
    print("==*"*18)

    continua = 's'
    
    while continua == 's':
        X = float(input("\nDigite um valor real p/ saber se está dentro do range min / max: "))

        if X >= Minimo and X <= Maximo:
            print("O número {} está dentro do range min / max!\nPrograma encerrado.".format(X))
            continua = 'n'
        else:
            print("O número {} não está dentro do range min / max!".format(X))

MinMax(Num1 = float(input("Digite um valor real: ")), Num2 = float(input("Digite outro valor real: ")))
