## Exercício 56 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática

""" Escreva uma função que receba uma lista como parâmetro de entrada e retorne uma tupla contendo quatro valores na seguinte ordem: a
soma, a média, o menor e o maior valor dentre todos os elementos nela contidos. Considere que nessa lista ocorram apenas números reais.
Escreva um programa para testar essa função, exibindo na tela os resultados. Neste exercício, evite utilizar as funções prontas
existentes no Python, como sum, min e max. """


L = []
Cont = 1

print("=*"*20)
print("Você deve digitar 5 números reais!")
print("=*"*20)

while len(L) < 5:
    NumDigitado = float(input('Digite o {}º número real, por exemplo (1.5): '.format(Cont)))
    L.append(NumDigitado)
    Cont += 1

def DadosTupla(Lista):
    T = ()
    Soma = L[0]+L[1]+L[2]+L[3]+L[4]
    Media = Soma / 5
    
    Menor = L[0]
    if L[1] < L[0] and L[1] < L[2] and L[1] < L[3] and L[1] < L[4]:
        Menor = L[1]
    elif L[2] < L[0] and L[2] < L[1] and L[2] < L[3] and L[2] < L[4]:
        Menor = L[2]
    elif L[3] < L[0] and L[3] < L[1] and L[3] < L[2] and L[3] < L[4]:
        Menor = L[3]
    elif L[4] < L[0] and L[4] < L[1] and L[4] < L[2] and L[4] < L[3]:
        Menor = L[4]
    
    Maior = L[0]
    if L[1] > L[0] and L[1] > L[2] and L[1] > L[3] and L[1] > L[4]:
        Maior = L[1]
    elif L[2] > L[0] and L[2] > L[1] and L[2] > L[3] and L[2] > L[4]:
        Maior = L[2]
    elif L[3] > L[0] and L[3] > L[1] and L[3] > L[2] and L[3] > L[4]:
        Maior = L[3]
    elif L[4] > L[0] and L[4] > L[1] and L[4] > L[2] and L[4] > L[3]:
        Maior = L[4]
        
    T = (Soma, Media, Menor, Maior)
    print("\nA tupla abaixo retornou a soma, média, menor e maior valores")
    return T

print(DadosTupla(L))

