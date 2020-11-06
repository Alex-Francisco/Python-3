## Exercício 15 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Uso de condições compostas: considerando os valores fornecidos, avalie cada condição e informe se o resultado é
falso (false) ou verdadeiro (true).

Para A = 10, B = 15 e C = 4 -> condição = A < B and A < C
Para A = 10, B = 15 e C = 4 -> condição = A < B or A < C
Para A = 1, B = 9 e C = 0 -> condição = A >= 0 and B == C
Para A = 1, B = 9 e C = 9 -> condição = A >= 0 and B == C
Para A = 1, B = 9 e C = 0 - > condição = A >= 0 or B == C
Para A = 1, B = 9 e C = 9 -> Condição = A >= 0 or B == C
Para A = 0, B = 0 e C = 0 -> Condição = B != 0 and A != C
Para A = 0, B = 0 e C = 25 -> Condição = B != 0 and A != C
Para A = 0, B = 0 e C = 0 -> Condição = B != 0 or A != C
Para A = 0, B = 0 a C = 25 -> Condição = B != 0 or A != C
"""

a = 10
b = 15
c = 4
r = a < b and a < c

print("Para A = 10, B = 15 e C = 4, a condição A < B and A < C retorna {}".format(r))
print("")

a = 10
b = 15
c = 4
r = a < b or a < c

print("Para A = 10, B = 15 e C = 4, a condição A < B or A < C retorna {}".format(r))
print("")

a = 1
b = 9
c = 0
r = a >= 0 and b == c

print("Para A = 1, B = 9  e C = 0, a condição A >= 0 and B == C retorna {}".format(r))
print("")

a = 1
b = 9
c = 9
r = a >= 0 and b == c

print("Para A = 1, B = 9 e C = 9, a condição A >= 0 and B == C retorna {}".format(r))
print("")

a = 1
b = 9
c = 0
r = a >= 0 or b == c

print("Para A = 1, B = 9 e C = 0, a condição A >= 0 or B == C retorna {}".format(r))
print("")

a = 1
b = 9
c = 9
r = a >= 0 or b == c

print("Para A = 1, B = 9 e C = 9, a condição A >= 0 or B == C retorna {}".format(r))
print("")

a = 0
b = 0
c = 0
r = b != 0 and a != c

print("Para A = 0, B = 0 e C = 0, a condição B != 0 and A != C retorna {}".format(r))
print("")

a = 0
b = 0
c = 25
r = b != 0 and a != c

print("Para A = 0, B = 0 e C = 25, a condição B != 0 and A != C retorna {}".format(r))
print("")

a = 0
b = 0
c = 0
r = b != 0 or a != c

print("Para A = 0, B = 0 e C = 0, a condição B != 0 or A != C retorna {}".format(r))
print("")

a = 0
b = 0
c = 25
r = b != 0 or a != c

print("Para A = 0, B = 0 e C = 25, a condição B != 0 or A != C retorna {}".format(r))
