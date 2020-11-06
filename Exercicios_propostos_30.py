## Exercício 30 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
"""Escreva um programa que leia um número inteiro N e, em seguida, leia N números reais, separando o menor e o maior e apresentando-os na
tela ignorando os números negativos fornecidos pelo usuário."""

menor = 0
maior = 0
cont = 0
continuar = "s"

try:
    num_int = int(input("Digite um número inteiro: "))

    if (num_int >= 0):
        menor = num_int
        maior = num_int
    else:
        cont += 1

    while (continuar == "s"):
        num_real = float(input("Digite um número real: "))
        continuar = input("Quer digitar outro número real? Digite s ou n: ")

        if (num_real >= 0):
            if (num_real < menor) or (num_real >= menor and cont == 1): 
                menor = num_real
                cont = 0

            if (num_real > maior) or (num_real >= maior and cont == 1):
                maior = num_real
                cont = 0

    if (cont == 1) and (maior == 0) and (menor == 0):
        print("\nNenhum número positivo foi digitado!")
    else:            
        print("\nO menor número digitado foi {}".format(menor))
        print("O maior número digitado foi {}".format(maior))
except:
    print("\nErro. Digite apenas números válidos para cada campo!")
      
    
        
    
        
        
    
    

    
    
