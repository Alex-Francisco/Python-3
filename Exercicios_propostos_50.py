## Exercício 50 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que exiba uma lista com os N's primeiros números primos, em que N é um número inteiro fornecido pelo usuário. """

def primos(x):
    if x < 1:
        return []
    numeros_primos = [2, 3]
    if x < 3:
        return numeros_primos[:x]
    for i in range(2, x):
        prox_numpri = numeros_primos[-1] + 2
        while any(not(prox_numpri % pn) for pn in numeros_primos):
            prox_numpri += 2
        numeros_primos.append(prox_numpri)
    return numeros_primos

N = input("Digite quantos números primos deseja ver: ")
print("\n")
print("==*"*30)
print("A lista abaixo guarda os primeiros {} números primos".format(N))
print(primos(int(N)))
print("==*"*30)
