## Exercício 20 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia três números reais e informe se eles constituem os lados de um triângulo. Em caso afirmativo,
informe se o triângulo é equilátero, isóceles ou escaleno. Para que três números formem um triângulo, a soma dos dois lados
menores deve ser maior que o lado maior. Uma boa solução para esse problema envolve o uso dos operadores and e or."""

lado_a = float(input("Digite o tamanho do lado A: "))
lado_b = float(input("Digite o tamanho do lado B: "))
lado_c = float(input("Digite o tamanho do lado C: "))

if (lado_a + lado_b) > lado_c and (lado_a + lado_c) > lado_b and (lado_b + lado_c) > lado_a:
    if lado_a == lado_b and lado_b == lado_c:
        print("\nTriângulo equilâtero")
    elif (lado_a == lado_b and lado_a != lado_c or lado_b != lado_c) or (lado_a == lado_c and lado_a != lado_b or lado_a != lado_c) or (lado_b == lado_c and lado_b != lado_a or lado_c != lado_a):
        print("\nTriângulo isósceles")
    else:
        print("\nTriângulo escaleno")
else:
    print("Não é possível formar um triângulo.")
    

