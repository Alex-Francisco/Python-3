## Exercício 14 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Uso de condições simples: considerando os valores fornecidos, avalie cada condição e informe se o resultado é
falso (false) ou verdadeiro (true). 
Para A = 0 e B = -3 -> condição = A > B
Para X = 3.7 -> condição X <= 10.0
Para A = 9 e B = 16 -> condição = A - B >= 0
Para A = 2, B = 4 e N = 10 -> condição = A * B < N
Para A = 3, B = 9 e C = 5 -> condição = 10 * A >= B * C
Para A = 3, B = 6 e C = 5 -> condição = 10 * A >= B * C
Para N = 7 -> Condição = N % 2 == 0
Para N = 8 -> Condição = N % 2 == 0
Para T = 'Morango' -> Condição T == 'Banana'
Para T = 'Morango' -> Condição T > 'Banana'"""

a = 0
b = -3
r = a > b

print("Para A = 0 e B = -3, a condição A > B retorna: {}".format(r))
print("")

x = 3.7
r = x <= 10.0

print("Para X = 3.7, a condição X <= 10.0 retorna: {}".format(r))
print("")

a = 9
b = 16
r = a - b >= 0

print("Para A = 9 e B = 16, a condição A - B >= 0 retorna {}".format(r))
print("")

a = 2
b = 4
n = 10
r = a * b < n

print("Para A = 2, B = 4 e N = 10, a condição A * B < N retorna {}".format(r))
print("")

a = 3
b = 9
c = 5
r = 10 * a >= b * c

print("Para A = 3, B = 9 e C = 5, a condição 10 * A >= B * C retorna {}".format(r))
print("")

a = 3
b = 6
c = 5
r = 10 * a >= b * c

print("Para A = 3, B = 6 e C = 5, a condição 10 * A >= B * C retorna {}".format(r))
print("")

n = 7
r = n % 2 == 0

print("Para N = 7, a condição N % 2 == 0 retorna {}".format(r))
print("")

n = 8
r = n % 2 == 0

print("Para N = 8, a condição N % 2 == 0 retorna {}".format(r))
print("")

t = 'morango'
r = t == 'banana'
print("Para T = Morango, a condição T == Banana retorna {}".format(r))
print("")

t = 'morango'
r = t > 'banana'
print("Para T = Morango, a condição T > Banana retorna {}".format(r))

