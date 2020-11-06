## Exercício 34 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Reescreva o programa do exercício resolvido 3.2 - sequência de Fibonacci fazendo a seguinte alteração: leia N
que será a quantidade de termos a ser exibida e leia um número inteiro adicional chamado Prim. Essa versão do
programa deverá apresentar N termos da sequência de Fibonacci imediatamente maiores que Prim."""

print("Sequência de Fibonacci\n")
print("---"*27)

N = 0

while N < 1: 
    try:
        N = int(input("Digite quantos termos você quer que seja exibido. Digite um nº maior que 1: "))
        Prim = int(input("Ok, você quer ver {} termo(s). O termo(s) exibido(s) deve(m) ser maior que qual nº?: ".format(N)))
        if N < 1: 
            print("\n")
            print("O programa precisa exibir pelo menos um termo!")
            print("\n")
    except:
        print("O dado digitado deve ser um número inteiro.")

A = 0
B = 1

if N == 1:
    N = str("")

print("---"*27)
print("""A sequência de Fibonacci começa com -> 0, 1, sendo assim, o(s) {} primeiro(s) número(s)
seguinte(s) da sequência maior(es) que {} é / são: """.format(N, Prim), end="")

if N == "":
    N = int(1)
    
i = -2
cont = 0
fora = 0

while i < N-2:
    
    C = A + B
    if C <= Prim:
        fora += 1
        i -= fora
    else:
        if cont < N:
            print("{}, ".format(C), end="")
            cont += 1
            
    A = B
    B = C
    i += 1

print("\n\nFim do programa")
    
            
