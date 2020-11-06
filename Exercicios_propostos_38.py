## Exercício 38 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia uma lista com N números inteiros, em que N é um número inteiro previamente digitado
pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que, quando essa
situação ocorrer, uma mensagem deve ser dada ao usuário. Por fim, exibir na tela a lista resultante. """

Lista = []
continua = 's'

while continua == 's':
    try:
        N = int(input("Digite um número inteiro: "))
    
        if N in Lista:
            print("O número digitado já está na lista!")
        else:
            Lista.append(N)

        continua = input("Quer continuar? Digite s ou n: ")

    except:
        print("Você deve digitar um número inteiro!")

print("\n")
print("=="*35)
print("A lista resultante é a seguinte -> {}".format(Lista))
print("=="*35)
        
