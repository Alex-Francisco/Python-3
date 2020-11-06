## Exercício 28 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
"""Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados no intervalo fechado (Min, Max), em que Min e Max são fornecidos
pelo usuário. É obrigatório que o valor Max seja maior que Min e, se isso não ocorrer, o programa deve exibir uma mensagem de aviso ao usuário e inverter
os valores."""

min_dig = int(input("Digite um número inteiro que será o valor mínimo: "))
max_dig = int(input("Digite um número inteiro que será o valor máximo: "))

print("")

while min_dig > max_dig:
    print("Atenção na digitação! O valores min e máx foram digitados invertidos. O programa irá se encarregar de fazer o troca para você.")
    
    min_dig, max_dig = max_dig, min_dig
    
print("")
print("Os números divisíveis por 5 no intervalo de {} até {} são: ".format(min_dig, max_dig), end="")

for i in range(min_dig, max_dig):
    if i % 5 == 0:   
        print(i, end=" ")


    
    
