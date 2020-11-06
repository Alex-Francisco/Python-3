## Exercício 51 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e retorne 1 se A for divisível
por B e 0 caso contrário. """

def Div(X, Y):
    R = X % Y

    if R == 0:
        print("\nO retorno foi: ", end="")
        return 1
    else:
        print("\nO retorno foi: ", end="")
        return 0

print("Se A for divisível por B, será retornado o valor 1, caso contrário retornará 0\n")

A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))
d = Div(A, B)
print(d)
        
    
