## Exercício 06 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Refaça o exercício 5 alterando-o de modo que a base e a altura do triângulo sejam lidas do
teclado. Considere-as números reais."""

Base = float(input("Digite o valor da base: "))
Altura = float(input("Digite o valor da altura: "))
Area = Base * Altura

print("Sendo a base = {0} e altura = {1}, a area resulta em {2}".format(Base, Altura, Area))
