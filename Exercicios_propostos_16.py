## Exercício 16 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Uso de condições mistas: considerando os valores fornecidos, avalie cada condição e informe se o resultado é
falso (false) ou verdadeiro (true). 
Para A = 10, B = 15 e C = 4 -> condição = A < B and A < C or C != 0
Para A = 10, B = 15 e C = 4 -> condição = A < B and (A < C or C !=0)
Para A = 1, B = 9 e C = 0 -> condição = not (A >= 0 and B == C)
Para A = 1, B = 9 e C = 9 -> condição = not (A > = 0) and not (B == C)
Para A = 1, B = 9 e C = 0 -> condição (A >= 0 or B == C) and B > A
Para A = -2, B = 0 e C = 2 -> condição not (A <= B) or C > B
Para A = -2, B = 0 e C = 2 -> condição not (A <= 0 or C > B)
Para A = 0, B = 1 e C = 0 -> condição A == 0 and B != 0 and C == 0
Para A = 5, B = 0 e C = 0 -> condição A == 0 and B != 0 and C == 0
Para A = 5, B = 0 e C = 0-> condição A == 0 pr B != 0 or C == 0
"""

a = 10
b = 15
c = 4
r = a < b and a < c or c != 0

print("Para A = 10, B = 15 e C = 4, a condição = A < B and A < C or C != 0 retorna {}".format(r))
print("")

r = a < b and (a < c or c != 0)

print("Para A = 10, B = 15 e C = 4, a condição = A < B and (A < C or C !=0) retorna {}".format(r))
print("")

a = 1
b = 9
c = 0
r = not (a >= 0 and b == c)

print("Para A = 1, B = 9 e C = 0, a condição = not (A >= 0 and B == C) retorna {}".format(r))
print("")

c = 9
r = not (a >= 0) and not (b == c)

print("Para A = 1, B = 9 e C = 9, a condição = not (A >= 0) and not (B == C) retorna {}".format(r))
print("")

c = 0
r = (a >= 0 or b == c) and b > a

print("Para A = 1, B = 9 e C = 0, a condição (A >= 0 or B == C) and B > A retorna {}".format(r))
print("")

a = -2
b = 0
c = 2
r = not (a <= b) or c > b

print("Para A = -2, B = 0 e C = 2, a condição not (A <= B) or C > B retorna {}".format(r))
print("")

r = not (a <= 0 or c > b)

print("Para A = -2, B = 0 e C = 2, a condição not (A <= 0 or C > B) retorna {}".format(r))
print("")

a = 0
b = 1
c = 0
r = a == 0 and b != 0 and c == 0

print("Para A = 0, B = 1 e C = 0, a condição A == 0 and B != 0 and C == 0 retorna {}".format(r))
print("")

a = 5
b = 0
r = a == 0 and  b != 0 and c == 0

print("Para A = 8, B = 0 e C = 0, a condição A == 0 and B != 0 and C == 0 retorna {}".format(r))
print("")

r = a == 0 or b != 0 or c == 0

print("Para A = 5, B = 0 e C = 0, a condição A == 0 and B != 0 and C == 0 retorna {}".format(r))
